import os
import csv
import requests
from datetime import datetime

ACCESS_TOKEN = os.environ.get("LINKEDIN_TOKEN")
AUTHOR_URN = os.environ.get("LINKEDIN_URN")

def get_todays_post(filename):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == today:
                # We are now returning the text and the image link separately!
                return row['Content'], row.get('Image_URL', '')
    return None, None

def post_to_linkedin(text, image_url):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    # Default setting for a text-only post
    share_content = {
        "shareCommentary": {"text": text},
        "shareMediaCategory": "NONE"
    }

    # If an image URL exists, upgrade the post to a rich media card
    if image_url and image_url.strip() != "":
        share_content["shareMediaCategory"] = "ARTICLE"
        share_content["media"] = [
            {
                "status": "READY",
                "originalUrl": image_url.strip()
            }
        ]

    payload = {
        "author": AUTHOR_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": share_content
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Successfully posted to LinkedIn with rich media!")
    else:
        print(f"Failed to post. Status: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    post_text, image_url = get_todays_post("posts.csv")
    if post_text:
        post_to_linkedin(post_text, image_url)
    else:
        print(f"No post scheduled for {datetime.now().strftime('%Y-%m-%d')}.")

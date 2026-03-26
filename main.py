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
                return f"{row['Content']}\n\n{row['Image_URL']}"
    return None

def post_to_linkedin(text):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    payload = {
        "author": AUTHOR_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Successfully posted to LinkedIn!")
    else:
        print(f"Failed to post. Status: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    post_text = get_todays_post("posts.csv")
    if post_text:
        post_to_linkedin(post_text)
    else:
        print(f"No post scheduled for {datetime.now().strftime('%Y-%m-%d')}.")

import os
import csv
import requests
from datetime import datetime

ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")
AUTHOR_URN = os.environ.get("LINKEDIN_URN")

def get_todays_post(filename):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == today:
                return row['Content'], row.get('Image_URL', '')
    return None, None

def upload_image_to_linkedin(image_url):
    """Downloads image from URL and uploads it natively to LinkedIn"""
    if not image_url or image_url.strip() == "":
        return None
        
    print("Downloading image from Unsplash...")
    img_response = requests.get(image_url.strip())
    if img_response.status_code != 200:
        print("Failed to download image.")
        return None
        
    print("Registering upload with LinkedIn...")
    register_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    register_payload = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": AUTHOR_URN,
            "serviceRelationships": [{"relationshipType": "OWNER", "identifier": "urn:li:userGeneratedContent"}]
        }
    }
    
    reg_res = requests.post(register_url, headers=headers, json=register_payload)
    if reg_res.status_code != 200:
        print(f"Failed to register upload. Error: {reg_res.text}")
        return None
        
    upload_data = reg_res.json()
    upload_url = upload_data['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    asset_urn = upload_data['value']['asset']
    
    print("Uploading image bytes to LinkedIn...")
    upload_headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    upload_res = requests.put(upload_url, headers=upload_headers, data=img_response.content)
    
    if upload_res.status_code == 201:
        print("Image successfully uploaded!")
        return asset_urn
    else:
        print("Failed to upload image bytes.")
        return None

def post_to_linkedin(text, image_url):
    # Try to upload the image first
    asset_urn = upload_image_to_linkedin(image_url)

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    # Default to text-only if there is no image
    share_content = {
        "shareCommentary": {"text": text},
        "shareMediaCategory": "NONE"
    }

    # If image upload was successful, attach it as a NATIVE IMAGE
    if asset_urn:
        share_content["shareMediaCategory"] = "IMAGE"
        share_content["media"] = [
            {
                "status": "READY",
                "media": asset_urn
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
    
    print("Publishing final post...")
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("🎉 Successfully posted to LinkedIn with Native Image!")
    else:
        print(f"❌ Failed to post. Status: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    post_text, image_url = get_todays_post("posts.csv")
    if post_text:
        post_to_linkedin(post_text, image_url)
    else:
        print(f"No post scheduled for {datetime.now().strftime('%Y-%m-%d')}.")

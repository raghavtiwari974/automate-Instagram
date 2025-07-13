import requests
import time


ACCESS_TOKEN = 'YOUR_LONG_LIVED_ACCESS_TOKEN'
IG_USER_ID = 'YOUR_IG_BUSINESS_ACCOUNT_ID'
IMAGE_URL = 'https://www.example.com/sample.jpg'  
CAPTION = ' Posted using #Python and the Instagram Graph API!'


create_url = f'https://graph.facebook.com/v20.0/{IG_USER_ID}/media'
create_payload = {
    'image_url': IMAGE_URL,
    'caption': CAPTION,
    'access_token': ACCESS_TOKEN
}
create_resp = requests.post(create_url, data=create_payload)
result = create_resp.json()

if 'id' not in result:
    print(" Error creating media:", result)
    exit()

creation_id = result['id']
print(" Media creation ID:", creation_id)


publish_url = f'https://graph.facebook.com/v20.0/{IG_USER_ID}/media_publish'
publish_payload = {
    'creation_id': creation_id,
    'access_token': ACCESS_TOKEN
}

time.sleep(3)
publish_resp = requests.post(publish_url, data=publish_payload)
publish_result = publish_resp.json()

if 'id' in publish_result:
    print("Post published successfully! Media ID:", publish_result['id'])
else:
    print(" Failed to publish:", publish_result)

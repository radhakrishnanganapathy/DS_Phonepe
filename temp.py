import os
from googleapiclient.discovery import build

api_key = 'AIzaSyB-PAJ9FCeskCnbAAvYHRpEt1B2B3lJaeY'
channel_id = 'UCXJMXPKb4b3FnLulbzzdQyQ'
# Create a YouTube API service
youtube = build('youtube', 'v3', developerKey=api_key)
response = youtube.videoCategories().list(
    part = 'snippet',
    regionCode='IN',
    # id='dQw4w9WgXcQ'
    
)
request = response.execute()
print(request)

# for i in request['items']:
    # category_id = category['id']
    # catogries = category['snippet']['title']
    # print({"id":category_id,"catogries":catogries})
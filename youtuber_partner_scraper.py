import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ""# put in path to your credential json.
# You can download from GCP console from IAM's key section. remember to enable youtube data API 
# Set up the YouTube API client
credentials, _ = google.auth.default()

youtube = build('youtube', 'v3', credentials=credentials)

def get_youtubers(topic):
    try:
        # Search for channels related to the topic
        search_response = youtube.search().list(
            q=topic,
            type='channel',
            part='id,snippet',
            maxResults=50  # you can adjust this as needed
        ).execute()

        channel_ids = []
        for search_result in search_response.get('items', []):
            channel_ids.append(search_result['id']['channelId'])

        # Get the statistics for each channel
        channels_response = youtube.channels().list(
            id=','.join(channel_ids),
            part='id,snippet,statistics'
        ).execute()

        youtubers = []
        for channel_result in channels_response.get('items', []):
            # Check if the channel has more than 10,000 subscribers and 10,000 average monthly views
            if int(channel_result['statistics']['subscriberCount']) >= 10000 and \
               int(channel_result['statistics']['viewCount']) / 30 >= 10000:
                youtubers.append(channel_result['snippet']['title'])

        return youtubers

    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')

# Example usage
topic = 'Jin Yang Pharmaceutical Co Ltd'
youtubers = get_youtubers(topic)

print(f'List of YouTubers related to {topic} with more than 10,000 subscribers and average monthly views of 10,000:')
for youtuber in youtubers:
    print(youtuber)


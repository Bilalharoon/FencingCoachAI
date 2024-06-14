from googleapiclient.discovery import build
import json

CHANNEL_ID = "UCxi42r9Q2RtW6Hq20FtQu6A"
with open("SECRETS.json", 'r') as secrets:
    secrets = json.load(secrets)
    API_KEY = secrets["API_KEY"]

# Function to get all video links from a YouTube channel
def get_all_video_links(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_links = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            type="video"
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['id']['videoId']
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            video_links.append(video_link)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_links

# Function to save video links to a text file
def save_links_to_file(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')


if __name__ == '__main__':
    video_links = get_all_video_links(API_KEY, CHANNEL_ID)
    save_links_to_file(video_links, 'video_links.txt')
    print(f'Total videos found: {len(video_links)}')
    print('Video links have been saved to video_links.txt')

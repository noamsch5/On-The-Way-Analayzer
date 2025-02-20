from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def search_similar_tracks(self, genre):
        try:
            api_key = os.getenv('YOUTUBE_API_KEY')
            if not api_key:
                raise ValueError("YouTube API key not found in environment variables")
                
            youtube = build('youtube', 'v3', developerKey=api_key)
            
            # Search for similar tracks
            search_response = youtube.search().list(
                q=f"{genre} music",
                part='snippet',
                maxResults=5,
                type='video'
            ).execute()
            
            # Format results
            similar_tracks = []
            for item in search_response['items']:
                similar_tracks.append({
                    'title': item['snippet']['title'],
                    'channel': item['snippet']['channelTitle'],
                    'videoId': item['id']['videoId']
                })
            
            return similar_tracks
            
        except Exception as e:
            print(f"Error in YouTube API: {str(e)}")
            return []

    def get_video_details(self, video_id):
        # Implement the logic to retrieve video information
        pass

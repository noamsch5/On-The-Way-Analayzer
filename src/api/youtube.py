from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

def find_similar_tracks(genre: str) -> list:
    """
    Find similar tracks on YouTube based on genre.
    
    Args:
        genre (str): Music genre to search for
        
    Returns:
        list: List of similar track dictionaries
    """
    api_key = os.getenv('YOUTUBE_API_KEY')
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

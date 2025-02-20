def generate_description(genre, related_tracks):
    """
    Generates a YouTube description based on the track's genre and related tracks.
    
    Parameters:
    genre (str): The genre of the track.
    related_tracks (list): A list of related track titles.
    
    Returns:
    str: A formatted description for the YouTube video.
    """
    description = f"Check out this amazing {genre} track! "
    description += "If you love this, you might also enjoy:\n"
    description += "\n".join(f"- {track}" for track in related_tracks)
    description += "\n\nDon't forget to like, share, and subscribe for more great music!"
    return description
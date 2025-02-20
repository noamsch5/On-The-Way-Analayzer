def generate_tags(genre, related_tracks, labels):
    tags = set()

    # Add genre and labels as tags
    tags.add(genre)
    tags.update(labels)

    # Add related track names as tags
    for track in related_tracks:
        tags.add(track)

    return list(tags)
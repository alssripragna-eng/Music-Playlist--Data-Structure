"""
Helper functions and sample data for playlist
"""
import random

# Sample songs data - preloaded for quick testing
SAMPLE_SONGS = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "duration": "3:20"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "duration": "3:54"},
    {"title": "Dance Monkey", "artist": "Tones and I", "duration": "3:30"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "duration": "3:14"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": "5:55"},
    {"title": "Levitating", "artist": "Dua Lipa", "duration": "3:24"},
    {"title": "Stay", "artist": "The Kid Laroi", "duration": "2:21"},
    {"title": "Heat Waves", "artist": "Glass Animals", "duration": "3:58"},
    {"title": "Astronaut in the Ocean", "artist": "Masked Wolf", "duration": "2:13"},
    {"title": "Good 4 U", "artist": "Olivia Rodrigo", "duration": "2:58"},
]

def get_random_song():
    """Get a random song from sample data"""
    return random.choice(SAMPLE_SONGS)

def format_time(seconds):
    """Convert seconds to mm:ss format"""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"

def create_sample_playlist(list_type):
    """Create a playlist with 4 sample songs"""
    from data_structures import SinglyLinkedList, DoublyLinkedList, CircularLinkedList
    
    # Choose correct list type
    if list_type == "Singly Linked List":
        playlist = SinglyLinkedList()
    elif list_type == "Doubly Linked List":
        playlist = DoublyLinkedList()
    else:  # Circular
        playlist = CircularLinkedList()
    
    # Add 4 sample songs
    for i in range(4):
        song = SAMPLE_SONGS[i]
        playlist.add_song(song["title"], song["artist"], song["duration"])
    
    return playlist

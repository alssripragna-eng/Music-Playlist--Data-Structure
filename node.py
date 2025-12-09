"""
SIMPLE SONG NODE STRUCTURE
Each node = One song in playlist
Contains: song data + pointers to next/prev songs
"""
class SongNode:
    def __init__(self, title, artist, duration):
        # Song data
        self.title = title          # Song name
        self.artist = artist        # Artist name  
        self.duration = duration    # Song length (e.g., "3:45")
        
        # Pointers (connections to other nodes)
        self.next = None            # Points to next song
        self.prev = None            # Points to previous song
        
        # For visualization
        self.is_current = False     # Is this currently playing?

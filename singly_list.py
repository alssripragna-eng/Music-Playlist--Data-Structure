"""
SINGLY LINKED LIST
Each node points only to NEXT node
Simple forward-only navigation
"""
from .node import SongNode

class SinglyLinkedList:
    def __init__(self):
        # Basic pointers
        self.head = None      # First song
        self.tail = None      # Last song
        self.current = None   # Now playing
        self.size = 0         # Song count
        
        # For explanation
        self.list_type = "Singly Linked List"
    
    # ------------------- BASIC OPERATIONS -------------------
    
    def add_song(self, title, artist, duration):
        """Add song to END of playlist"""
        # 1. Create new node
        new_song = SongNode(title, artist, duration)
        
        # 2. If playlist is empty
        if self.head is None:
            self.head = new_song
            self.current = new_song
        else:
            # 3. Add to end (tail's next points to new song)
            self.tail.next = new_song
        
        # 4. Update tail to new song
        self.tail = new_song
        
        # 5. Increase size
        self.size += 1
        
        return new_song
    
    def remove_current(self):
        """Remove the currently playing song"""
        # 1. Check if playlist is empty
        if self.current is None:
            return None
        
        # 2. Special case: Removing the first song
        if self.head == self.current:
            self.head = self.current.next
        else:
            # 3. Find the song BEFORE current
            temp = self.head
            while temp and temp.next != self.current:
                temp = temp.next
            
            # 4. Skip current song (connect prev to next)
            if temp:
                temp.next = self.current.next
        
        # 5. Move current to next song (or to head if none)
        self.current = self.current.next or self.head
        
        # 6. Decrease size
        self.size -= 1
        
        return self.current
    
    def next_song(self):
        """Move to next song"""
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current
    
    def prev_song(self):
        """Cannot go back in singly linked list"""
        return self.current  # Stay on same song
    
    # ------------------- UTILITY METHODS -------------------
    
    def get_all_songs(self):
        """Get list of all songs (for display)"""
        songs = []
        temp = self.head
        
        while temp:
            temp.is_current = (temp == self.current)
            songs.append(temp)
            temp = temp.next
            
        return songs
    
    def clear(self):
        """Empty the playlist"""
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
    
    def get_stats(self):
        """Get statistics about playlist"""
        return {
            "type": self.list_type,
            "size": self.size,
            "current": self.current.title if self.current else "None",
            "head": self.head.title if self.head else "None",
            "tail": self.tail.title if self.tail else "None"
        }

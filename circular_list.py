"""
CIRCULAR LINKED LIST
Last node points BACK to first node
Creates continuous loop - infinite playlist!
"""
from .doubly_list import DoublyLinkedList

class CircularLinkedList(DoublyLinkedList):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        self.list_type = "Circular Linked List"
    
    # ------------------- OVERRIDDEN METHODS -------------------
    
    def add_song(self, title, artist, duration):
        """Add song and connect tail to head (circular)"""
        from .node import SongNode
        
        # 1. Create new node
        new_song = SongNode(title, artist, duration)
        
        # 2. If playlist is empty
        if self.head is None:
            self.head = new_song
            self.tail = new_song
            self.current = new_song
            
            # Make it circular: point to itself
            new_song.next = new_song
            new_song.prev = new_song
        else:
            # 3. Add to end with circular connections
            new_song.prev = self.tail
            new_song.next = self.head  # ← CIRCULAR: Points to head
            
            # Update connections
            self.tail.next = new_song
            self.head.prev = new_song  # ← CIRCULAR: Head points back
            
            # Update tail
            self.tail = new_song
        
        # 4. Increase size
        self.size += 1
        
        return new_song
    
    def next_song(self):
        """Always has next song (circular - never ends)"""
        if self.current:
            self.current = self.current.next
        return self.current
    
    def prev_song(self):
        """Always has previous song (circular)"""
        if self.current:
            self.current = self.current.prev
        return self.current
    
    # ------------------- SAFE METHOD OVERRIDE -------------------
    
    def get_all_songs(self):
        """Get songs with circular list detection - SAFE VERSION"""
        songs = []
        
        if not self.head:
            return songs
        
        temp = self.head
        count = 0
        max_songs = 20  # Safety limit
        
        while temp and count < max_songs:
            temp.is_current = (temp == self.current)
            songs.append(temp)
            
            # Move to next
            temp = temp.next
            
            # If we're back at head, stop
            if temp == self.head:
                if count < max_songs - 1:  # Don't add duplicate head
                    songs.append(f"↻ (Circular - back to: {self.head.title})")
                break
            
            count += 1
        
        return songs

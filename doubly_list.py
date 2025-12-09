"""
DOUBLY LINKED LIST
Each node points to BOTH next AND previous
Can move forward AND backward
"""
from .singly_list import SinglyLinkedList

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        self.list_type = "Doubly Linked List"
    
    # ------------------- OVERRIDDEN METHODS -------------------
    
    def add_song(self, title, artist, duration):
        """Add song with BOTH forward and backward pointers"""
        from .node import SongNode
        
        # 1. Create new node
        new_song = SongNode(title, artist, duration)
        
        # 2. If playlist is empty
        if self.head is None:
            self.head = new_song
            self.current = new_song
            self.tail = new_song
        else:
            # 3. Set new song's prev pointer to current tail
            new_song.prev = self.tail
            
            # 4. Set current tail's next pointer to new song
            self.tail.next = new_song
            
            # 5. Update tail to new song
            self.tail = new_song
        
        # 6. Increase size
        self.size += 1
        
        return new_song
    
    def remove_current(self):
        """Remove current song with prev pointer updates"""
        # 1. Check if empty
        if self.current is None:
            return None
        
        # 2. Update previous song's next pointer
        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            # Current is head
            self.head = self.current.next
        
        # 3. Update next song's prev pointer
        if self.current.next:
            self.current.next.prev = self.current.prev
        else:
            # Current is tail
            self.tail = self.current.prev
        
        # 4. Move current pointer
        if self.current.next:
            self.current = self.current.next
        elif self.current.prev:
            self.current = self.current.prev
        else:
            self.current = None
        
        # 5. Decrease size
        self.size -= 1
        
        return self.current
    
    # ------------------- NEW METHOD -------------------
    
    def prev_song(self):
        """Move to previous song (NEW: Works in doubly linked)"""
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current

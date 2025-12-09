"""
Main GUI Application
Connects controls, display, and data structures
"""
import tkinter as tk
from tkinter import ttk, messagebox
from data_structures import SinglyLinkedList, DoublyLinkedList, CircularLinkedList
from utils.helpers import SAMPLE_SONGS
from .controls import Controls
from .display import Display

class PlaylistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Playlist Manager - Data Structures Simulation")
        self.root.geometry("1000x700")
        
        # Current playlist
        self.playlist = None
        
        # Create GUI
        self.setup_gui()
        
        # Initialize with Singly Linked List
        self.change_list_type("Singly Linked List")
        
        # Add some sample songs
        self.add_sample_songs()
    
    def setup_gui(self):
        """Setup the main GUI layout"""
        # Configure root grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Main container
        main_container = ttk.Frame(self.root, padding="5")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_container.columnconfigure(1, weight=1)
        main_container.rowconfigure(0, weight=1)
        
        # ---------- LEFT PANEL: Controls ----------
        left_panel = ttk.Frame(main_container)
        left_panel.grid(row=0, column=0, sticky=(tk.N, tk.S), padx=(0, 5))
        
        # Create controls
        self.controls = Controls(left_panel, self)
        
        # ---------- RIGHT PANEL: Display ----------
        right_panel = ttk.Frame(main_container)
        right_panel.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        right_panel.columnconfigure(0, weight=1)
        right_panel.rowconfigure(0, weight=1)
        
        # Create display
        self.display = Display(right_panel, self)
        
        # Add explanation text at bottom
        explanation = ttk.Label(
            self.root,
            text="💡 Tip: Change Data Structure Type to see how different linked lists work!",
            font=("Arial", 9, "italic"),
            foreground="blue"
        )
        explanation.grid(row=1, column=0, columnspan=2, pady=5)
    
    def add_sample_songs(self):
        """Add 3 sample songs to start"""
        sample_songs = SAMPLE_SONGS[:3]
        for song in sample_songs:
            self.playlist.add_song(song["title"], song["artist"], song["duration"])
        self.update_display()
    
    def change_list_type(self, list_type):
        """Change the linked list type"""
        # Clear current playlist
        songs = []
        if self.playlist:
            songs = self.playlist.get_all_songs()
            current_song = self.playlist.current
        
        # Create new playlist of selected type
        if list_type == "Singly Linked List":
            self.playlist = SinglyLinkedList()
        elif list_type == "Doubly Linked List":
            self.playlist = DoublyLinkedList()
        else:  # Circular Linked List
            self.playlist = CircularLinkedList()
        
        # Re-add songs to new playlist
        for song in songs:
            self.playlist.add_song(song.title, song.artist, song.duration)
        
        # Set current song
        if songs and current_song:
            # Try to find the same song in new list
            for song in self.playlist.get_all_songs():
                if song.title == current_song.title:
                    self.playlist.current = song
                    break
        
        self.update_display()
        
        # Show info message
        if list_type == "Singly Linked List":
            info = "• Only forward navigation (next)\n• Simple pointer structure"
        elif list_type == "Doubly Linked List":
            info = "• Forward & backward navigation\n• Each node has next AND prev pointers"
        else:  # Circular
            info = "• Continuous loop navigation\n• Last node points to first\n• Infinite playlist!"
        
        messagebox.showinfo(f"{list_type} Activated", info)
    
    def add_song(self, title, artist, duration):
        """Add a new song to playlist"""
        if not title or not artist or not duration:
            return
        
        self.playlist.add_song(title, artist, duration)
        self.update_display()
    
    def next_song(self):
        """Move to next song"""
        if not self.playlist or self.playlist.size == 0:
            messagebox.showinfo("Empty", "Playlist is empty!")
            return
        
        current_before = self.playlist.current.title if self.playlist.current else "None"
        self.playlist.next_song()
        current_after = self.playlist.current.title if self.playlist.current else "None"
        
        self.update_display()
        
        # Show movement info
        if current_before != current_after:
            messagebox.showinfo("Next Song", f"Moved from:\n{current_before}\n↓\nTo: {current_after}")
    
    def prev_song(self):
        """Move to previous song"""
        if not self.playlist or self.playlist.size == 0:
            messagebox.showinfo("Empty", "Playlist is empty!")
            return
        
        if self.playlist.list_type == "Singly Linked List":
            messagebox.showinfo("Not Supported", 
                "⚠️ Singly Linked List cannot go backward!\n"
                "Switch to Doubly or Circular Linked List.")
            return
        
        current_before = self.playlist.current.title if self.playlist.current else "None"
        self.playlist.prev_song()
        current_after = self.playlist.current.title if self.playlist.current else "None"
        
        self.update_display()
        
        if current_before != current_after:
            messagebox.showinfo("Previous Song", f"Moved from:\n{current_before}\n↓\nTo: {current_after}")
    
    def play_current(self):
        """'Play' current song (simulation)"""
        if not self.playlist or not self.playlist.current:
            messagebox.showinfo("No Song", "No song to play!")
            return
        
        song = self.playlist.current
        messagebox.showinfo(
            "Now Playing",
            f"🎵 Playing:\n\n"
            f"Title: {song.title}\n"
            f"Artist: {song.artist}\n"
            f"Duration: {song.duration}\n\n"
            f"Playlist Type: {self.playlist.list_type}"
        )
        self.update_display()
    
    def remove_current(self):
        """Remove current song"""
        if not self.playlist or self.playlist.size == 0:
            messagebox.showinfo("Empty", "Playlist is already empty!")
            return
        
        removed_song = self.playlist.current.title if self.playlist.current else "Unknown"
        self.playlist.remove_current()
        
        self.update_display()
        messagebox.showinfo("Song Removed", f"Removed: {removed_song}")
    
    def clear_playlist(self):
        """Clear all songs"""
        if not self.playlist or self.playlist.size == 0:
            messagebox.showinfo("Empty", "Playlist is already empty!")
            return
        
        if messagebox.askyesno("Clear Playlist", "Are you sure you want to clear all songs?"):
            self.playlist.clear()
            self.update_display()
            messagebox.showinfo("Cleared", "Playlist cleared!")
    
    def update_display(self):
        """Update all display elements"""
        if not self.playlist:
            return
        
        # Update visualization
        self.display.draw_linked_list(self.playlist)
        
        # Update now playing
        self.display.update_now_playing(self.playlist.current)
        
        # Update statistics
        self.display.update_stats(self.playlist)

"""
GUI Controls - All buttons, inputs, and user interactions
"""
import tkinter as tk
from tkinter import ttk, messagebox
from utils.helpers import get_random_song

class Controls:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.operations_count = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create all control widgets"""
        # Main control frame
        self.control_frame = ttk.LabelFrame(self.parent, text="Playlist Controls", padding="10")
        self.control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # ---------- List Type Selection ----------
        ttk.Label(self.control_frame, text="Data Structure Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.list_type_var = tk.StringVar(value="Singly Linked List")
        list_types = ["Singly Linked List", "Doubly Linked List", "Circular Linked List"]
        
        self.type_combo = ttk.Combobox(
            self.control_frame, 
            textvariable=self.list_type_var, 
            values=list_types, 
            state="readonly",
            width=25
        )
        self.type_combo.grid(row=0, column=1, pady=5, padx=5)
        self.type_combo.bind('<<ComboboxSelected>>', self.change_list_type)
        
        # ---------- Add Song Section ----------
        ttk.Separator(self.control_frame, orient='horizontal').grid(row=1, column=0, columnspan=3, sticky="ew", pady=10)
        ttk.Label(self.control_frame, text="Add New Song:", font=("Arial", 10, "bold")).grid(row=2, column=0, columnspan=3, pady=5)
        
        # Song title
        ttk.Label(self.control_frame, text="Title:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.title_entry = ttk.Entry(self.control_frame, width=30)
        self.title_entry.grid(row=3, column=1, columnspan=2, pady=2, padx=5)
        self.title_entry.insert(0, "New Song")
        
        # Artist
        ttk.Label(self.control_frame, text="Artist:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.artist_entry = ttk.Entry(self.control_frame, width=30)
        self.artist_entry.grid(row=4, column=1, columnspan=2, pady=2, padx=5)
        self.artist_entry.insert(0, "Artist Name")
        
        # Duration
        ttk.Label(self.control_frame, text="Duration (mm:ss):").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.duration_entry = ttk.Entry(self.control_frame, width=30)
        self.duration_entry.grid(row=5, column=1, columnspan=2, pady=2, padx=5)
        self.duration_entry.insert(0, "3:30")
        
        # Add buttons
        btn_frame = ttk.Frame(self.control_frame)
        btn_frame.grid(row=6, column=0, columnspan=3, pady=10)
        
        ttk.Button(btn_frame, text="Add Song", command=self.add_song, width=12).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Add Random", command=self.add_random_song, width=12).pack(side=tk.LEFT, padx=2)
        
        # ---------- Playback Controls ----------
        ttk.Separator(self.control_frame, orient='horizontal').grid(row=7, column=0, columnspan=3, sticky="ew", pady=10)
        ttk.Label(self.control_frame, text="Playback Controls:", font=("Arial", 10, "bold")).grid(row=8, column=0, columnspan=3, pady=5)
        
        playback_frame = ttk.Frame(self.control_frame)
        playback_frame.grid(row=9, column=0, columnspan=3, pady=5)
        
        # Playback buttons
        ttk.Button(playback_frame, text="⏮ Prev", command=self.prev_song, width=10).pack(side=tk.LEFT, padx=2)
        ttk.Button(playback_frame, text="▶ Play", command=self.play_current, width=10).pack(side=tk.LEFT, padx=2)
        ttk.Button(playback_frame, text="⏭ Next", command=self.next_song, width=10).pack(side=tk.LEFT, padx=2)
        
        # ---------- Playlist Operations ----------
        ttk.Separator(self.control_frame, orient='horizontal').grid(row=10, column=0, columnspan=3, sticky="ew", pady=10)
        ttk.Label(self.control_frame, text="Playlist Operations:", font=("Arial", 10, "bold")).grid(row=11, column=0, columnspan=3, pady=5)
        
        ops_frame = ttk.Frame(self.control_frame)
        ops_frame.grid(row=12, column=0, columnspan=3, pady=5)
        
        # Operation buttons
        ttk.Button(ops_frame, text="Remove Current", command=self.remove_current, width=15).pack(side=tk.LEFT, padx=2)
        ttk.Button(ops_frame, text="Clear All", command=self.clear_playlist, width=15).pack(side=tk.LEFT, padx=2)
        
        # ---------- Stats ----------
        ttk.Separator(self.control_frame, orient='horizontal').grid(row=13, column=0, columnspan=3, sticky="ew", pady=10)
        
        self.ops_label = ttk.Label(self.control_frame, text="Operations: 0", font=("Arial", 9))
        self.ops_label.grid(row=14, column=0, columnspan=3, pady=5)
    
    # ---------- EVENT HANDLERS ----------
    
    def increment_ops(self):
        """Increase operation counter"""
        self.operations_count += 1
        self.ops_label.config(text=f"Operations: {self.operations_count}")
    
    def change_list_type(self, event=None):
        """Change linked list type"""
        self.increment_ops()
        self.app.change_list_type(self.list_type_var.get())
    
    def add_song(self):
        """Add song from input fields"""
        title = self.title_entry.get().strip()
        artist = self.artist_entry.get().strip()
        duration = self.duration_entry.get().strip()
        
        if not title or not artist or not duration:
            messagebox.showwarning("Input Error", "Please fill all fields!")
            return
        
        self.increment_ops()
        self.app.add_song(title, artist, duration)
        
        # Clear inputs
        self.title_entry.delete(0, tk.END)
        self.artist_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.title_entry.insert(0, "New Song")
        self.artist_entry.insert(0, "Artist Name")
        self.duration_entry.insert(0, "3:30")
    
    def add_random_song(self):
        """Add a random sample song"""
        song = get_random_song()
        self.increment_ops()
        self.app.add_song(song["title"], song["artist"], song["duration"])
    
    def next_song(self):
        """Move to next song"""
        self.increment_ops()
        self.app.next_song()
    
    def prev_song(self):
        """Move to previous song"""
        self.increment_ops()
        self.app.prev_song()
    
    def play_current(self):
        """'Play' current song"""
        self.increment_ops()
        self.app.play_current()
    
    def remove_current(self):
        """Remove current song"""
        self.increment_ops()
        self.app.remove_current()
    
    def clear_playlist(self):
        """Clear all songs"""
        self.increment_ops()
        self.app.clear_playlist()

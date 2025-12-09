"""
Display and Visualization of Linked List
Shows nodes, pointers, and connections visually
"""
import tkinter as tk
from tkinter import ttk

class Display:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.canvas = None
        self.stats_label = None
        self.now_playing_label = None
        
        self.create_display()
    
    def create_display(self):
        """Create all display widgets"""
        # ---------- Visualization Canvas ----------
        viz_frame = ttk.LabelFrame(self.parent, text="Linked List Visualization", padding="10")
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Canvas for drawing nodes
        self.canvas = tk.Canvas(viz_frame, bg='white', height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Add scrollbar for many songs
        scrollbar = ttk.Scrollbar(viz_frame, orient="horizontal", command=self.canvas.xview)
        scrollbar.pack(fill=tk.X, pady=(0, 5))
        self.canvas.configure(xscrollcommand=scrollbar.set)
        
        # ---------- Now Playing Display ----------
        now_frame = ttk.LabelFrame(self.parent, text="Now Playing", padding="10")
        now_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.now_playing_label = ttk.Label(
            now_frame, 
            text="No song playing", 
            font=("Arial", 12, "bold"),
            foreground="green"
        )
        self.now_playing_label.pack()
        
        # ---------- Statistics Display ----------
        stats_frame = ttk.LabelFrame(self.parent, text="Linked List Statistics", padding="10")
        stats_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.stats_label = ttk.Label(
            stats_frame, 
            text="Select a data structure to begin",
            font=("Courier", 10)
        )
        self.stats_label.pack()
    
    def draw_linked_list(self, playlist):
        """Draw the linked list visualization"""
        # Clear canvas
        self.canvas.delete("all")
        
        if not playlist or playlist.size == 0:
            self.canvas.create_text(
                300, 150, 
                text="Playlist is empty!\nAdd songs to visualize.",
                font=("Arial", 14),
                fill="gray"
            )
            return
        
        # Get all songs
        songs = playlist.get_all_songs()
        if not songs:
            return
        
        # Calculate positions
        node_width = 120
        node_height = 60
        spacing = 150
        start_x = 50
        y = 100
        
        # Draw nodes
        for i, song in enumerate(songs):
            x = start_x + i * spacing
            
            # Draw node rectangle
            if song.is_current:
                # Current song - highlighted
                self.canvas.create_rectangle(
                    x, y, x + node_width, y + node_height,
                    fill="lightgreen", outline="darkgreen", width=3
                )
                fill_color = "darkgreen"
            else:
                # Normal song
                self.canvas.create_rectangle(
                    x, y, x + node_width, y + node_height,
                    fill="lightblue", outline="blue", width=2
                )
                fill_color = "black"
            
            # Draw song info
            title = song.title[:15] + "..." if len(song.title) > 15 else song.title
            self.canvas.create_text(
                x + node_width/2, y + 15,
                text=title, font=("Arial", 9, "bold"),
                fill=fill_color
            )
            
            self.canvas.create_text(
                x + node_width/2, y + 30,
                text=song.artist, font=("Arial", 8),
                fill=fill_color
            )
            
            self.canvas.create_text(
                x + node_width/2, y + 45,
                text=song.duration, font=("Arial", 8),
                fill=fill_color
            )
            
            # Draw node number
            self.canvas.create_text(
                x + 10, y + 10,
                text=f"#{i+1}", font=("Arial", 8, "bold"),
                fill="red"
            )
            
            # Draw next pointer (→)
            if song.next:
                arrow_start = x + node_width
                arrow_end = x + spacing
                
                # Draw arrow line
                self.canvas.create_line(
                    arrow_start, y + node_height/2,
                    arrow_end - 20, y + node_height/2,
                    arrow="last", width=2, fill="blue"
                )
                
                # Draw arrow head
                self.canvas.create_line(
                    arrow_end - 25, y + node_height/2 - 5,
                    arrow_end - 20, y + node_height/2,
                    arrow_end - 25, y + node_height/2 + 5,
                    fill="blue", width=2
                )
                
                # Label for "next"
                self.canvas.create_text(
                    x + node_width/2 + spacing/2, y + node_height/2 - 15,
                    text="next", font=("Arial", 7),
                    fill="blue"
                )
            
            # Draw prev pointer (←) for doubly/circular
            if hasattr(song, 'prev') and song.prev and playlist.list_type != "Singly Linked List":
                arrow_start = x
                arrow_end = x - spacing + 20
                
                # Draw arrow line
                self.canvas.create_line(
                    arrow_start, y + node_height/2,
                    arrow_end, y + node_height/2,
                    arrow="last", width=2, fill="green", dash=(4, 2)
                )
                
                # Draw arrow head
                self.canvas.create_line(
                    arrow_end + 5, y + node_height/2 - 5,
                    arrow_end, y + node_height/2,
                    arrow_end + 5, y + node_height/2 + 5,
                    fill="green", width=2
                )
                
                # Label for "prev"
                self.canvas.create_text(
                    x - spacing/2, y + node_height/2 - 15,
                    text="prev", font=("Arial", 7),
                    fill="green"
                )
        
        # Update canvas scroll region
        total_width = start_x + len(songs) * spacing + 50
        self.canvas.configure(scrollregion=(0, 0, total_width, 400))
        
        # Add legend
        self.draw_legend()
    
    def draw_legend(self):
        """Draw legend for visualization"""
        # Legend box
        self.canvas.create_rectangle(20, 20, 220, 90, fill="white", outline="gray")
        
        # Title
        self.canvas.create_text(120, 30, text="Legend", font=("Arial", 9, "bold"))
        
        # Current node
        self.canvas.create_rectangle(30, 40, 50, 60, fill="lightgreen", outline="darkgreen")
        self.canvas.create_text(70, 50, text="= Current Song", font=("Arial", 8), anchor="w")
        
        # Normal node
        self.canvas.create_rectangle(30, 60, 50, 80, fill="lightblue", outline="blue")
        self.canvas.create_text(70, 70, text="= Other Songs", font=("Arial", 8), anchor="w")
        
        # Pointer labels
        self.canvas.create_text(130, 50, text="→ = next pointer", font=("Arial", 8), fill="blue", anchor="w")
        self.canvas.create_text(130, 70, text="← = prev pointer", font=("Arial", 8), fill="green", anchor="w")
    
    def update_now_playing(self, song):
        """Update now playing display"""
        if song:
            text = f"▶ NOW PLAYING: {song.title} - {song.artist} ({song.duration})"
            self.now_playing_label.config(text=text, foreground="green")
        else:
            self.now_playing_label.config(text="No song playing", foreground="gray")
    
    def update_stats(self, playlist):
        """Update statistics display"""
        if not playlist:
            self.stats_label.config(text="No playlist loaded")
            return
        
        stats = playlist.get_stats()
        
        stats_text = f"""
        Data Structure: {stats['type']}
        Total Songs: {stats['size']}
        Current Song: {stats['current']}
        First Song: {stats['head']}
        Last Song: {stats['tail']}
        
        Navigation:
        • Singly LL: Only forward (next)
        • Doubly LL: Forward & backward (next/prev)
        • Circular LL: Infinite loop (next → prev → next...)
        """
        
        self.stats_label.config(text=stats_text)

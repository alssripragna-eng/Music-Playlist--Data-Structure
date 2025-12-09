"""
🎵 PLAYLIST MANAGER - DATA STRUCTURES SIMULATION
Main entry point - RUN THIS FILE to start the application

A visual simulation of different linked list data structures:
1. Singly Linked List
2. Doubly Linked List  
3. Circular Linked List

Created for: Data Structures Project Submission
"""
import tkinter as tk
from tkinter import messagebox
from gui import PlaylistApp

def main():
    """Main function to start the application"""
    try:
        # Create main window
        root = tk.Tk()
        
        # Set window icon and title
        root.title("🎵 Playlist Manager - Data Structures Project")
        root.geometry("1000x700")
        
        # Center window on screen
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Create the application
        app = PlaylistApp(root)
        
        # Show welcome message
        show_welcome_message()
        
        # Start the application
        root.mainloop()
        
    except Exception as e:
        print(f"Error starting application: {e}")
        messagebox.showerror("Startup Error", 
            f"Cannot start application:\n{str(e)}\n\n"
            "Make sure all files are in correct folders.")

def show_welcome_message():
    """Show welcome message on startup"""
    welcome_text = """
    🎵 WELCOME TO PLAYLIST MANAGER 🎵
    
    A Data Structures Simulation Project
    
    This application demonstrates three types of Linked Lists:
    
    1. SINGLY LINKED LIST
       • Each node points only to next node
       • Can only move forward
       • Simple and memory efficient
    
    2. DOUBLY LINKED LIST  
       • Each node points to both next AND previous
       • Can move forward and backward
       • More flexible but uses more memory
    
    3. CIRCULAR LINKED LIST
       • Last node points back to first node
       • Continuous loop navigation
       • Perfect for playlists that repeat
    
    HOW TO USE:
    1. Select a data structure type
    2. Add songs using the form
    3. Use playback controls
    4. Watch the visualization update!
    """
    
    messagebox.showinfo("Playlist Manager - Data Structures Project", welcome_text)

if __name__ == "__main__":
    print("Starting Playlist Manager...")
    print("Data Structures: Singly, Doubly, Circular Linked Lists")
    print("Project for: Data Structures Course")
    print("=" * 50)
    main()

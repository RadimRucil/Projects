import tkinter as tk
from tkinter import ttk
import psutil
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")

        # Configure the window
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        # Create and place labels
        self.cpu_label = ttk.Label(root, text="CPU Usage: 0%", font=("Arial", 16))
        self.cpu_label.pack(pady=10)

        self.memory_label = ttk.Label(root, text="Memory Usage: 0%", font=("Arial", 16))
        self.memory_label.pack(pady=10)

        # Update stats every second
        self.update_stats()

    def update_stats(self):
        """Update CPU and memory usage statistics."""
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")

        # Schedule the function to run again after 1000ms (1 second)
        self.root.after(1000, self.update_stats)

def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

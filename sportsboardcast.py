import tkinter as tk
from tkinter import scrolledtext

# Define the Broadcast class

class Broadcast:
    def __init__(self, event_id, event_name, timing, channel, location, duration):
        self.event_id = event_id # unique ID for the event
        self.event_name = event_name  # name of the event (e.g., FIFA World Cup Final)
        self.timing = timing # when the event will be broadcast (date/time)
        self.channel = channel # TV channel broadcasting the event
        self.location = location  # location of the event (e.g., stadium)
        self.duration = duration  # duration of the event (e.g., 2 hours)
        self.rights = None  # Rights information (if applicable)
        
    def __str__(self):
        return (f"Broadcast(ID: {self.event_id}, Event: {self.event_name}, Time: {self.timing}, "
                f"Channel: {self.channel}, Location: {self.location}, Duration: {self.duration}, "
                f"Rights: {self.rights})")

# Define the BroadcastManager class to handle the scheduling tool
class BroadcastManager:
    def __init__(self):
        self.broadcasts = {}
          
    # Add a new broadcast
    def add_broadcast(self, event_id, event_name, timing, channel, location, duration):
        if event_id in self.broadcasts:
            return f"Broadcast with event ID {event_id} already exists."
        else:
            new_broadcast = Broadcast(event_id, event_name, timing, channel, location, duration)
            self.broadcasts[event_id] = new_broadcast
            return f"Broadcast for {event_name} added."

    # View all broadcasts
    def view_all_broadcasts(self):
        if self.broadcasts:
            return "\n".join([str(broadcast) for broadcast in self.broadcasts.values()])
        else:
            return "No broadcasts available."

    # Update an existing broadcast
    def update_broadcast(self, event_id, new_timing=None, new_channel=None):
        if event_id in self.broadcasts:
            broadcast = self.broadcasts[event_id]
            if new_timing:
                broadcast.timing = new_timing
            if new_channel:
                broadcast.channel = new_channel
            return f"Broadcast {event_id} updated."
        else:
            return f"Broadcast with event ID {event_id} not found."

    # Delete an existing broadcast
    def delete_broadcast(self, event_id):
        if event_id in self.broadcasts:
            del self.broadcasts[event_id]
            return f"Broadcast with event ID {event_id} deleted."
        else:
            return f"Broadcast with event ID {event_id} not found."

#Initialize Broadcast Manager
manager = BroadcastManager()

# --- Tkinter GUI Setup ---

# Initialize the main window
root = tk.Tk()
root.title("Sports Broadcast Scheduling Tool")
root.geometry("800x600")

# Add scrolled text area for output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update output area
def update_output(message):
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, message)

# Add a broadcast function
def add_broadcast():
    try:
        event_id = int(event_id_entry.get())  # Ensure event ID is a number
        event_name = event_name_entry.get()
        timing = timing_entry.get()
        channel = channel_entry.get()
        location = location_entry.get()
        duration = duration_entry.get()
        
        result = manager.add_broadcast(event_id, event_name, timing, channel, location, duration)
        update_output(result)
    except ValueError:
        update_output("Event ID must be a number.")

# View all broadcasts function
def view_broadcasts():
    result = manager.view_all_broadcasts()
    update_output(result)

# Update broadcast function
def update_broadcast():
    try:
        event_id = int(event_id_entry.get())  # Ensure event ID is a number
        new_timing = timing_entry.get()
        new_channel = channel_entry.get()
        
        result = manager.update_broadcast(event_id, new_timing, new_channel)
        update_output(result)
    except ValueError:
        update_output("Event ID must be a number.")

# Delete broadcast function
def delete_broadcast():
    try:
        event_id = int(event_id_entry.get())  # Ensure event ID is a number
        result = manager.delete_broadcast(event_id)
        update_output(result)
    except ValueError:
        update_output("Event ID must be a number.")




# Entry labels and inputs
tk.Label(root, text="Event ID:").grid(row=1, column=0, padx=5, pady=5)
event_id_entry = tk.Entry(root)
event_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Event Name:").grid(row=2, column=0, padx=5, pady=5)
event_name_entry = tk.Entry(root)
event_name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Timing:").grid(row=3, column=0, padx=5, pady=5)
timing_entry = tk.Entry(root)
timing_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Channel:").grid(row=4, column=0, padx=5, pady=5)
channel_entry = tk.Entry(root)
channel_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Location:").grid(row=5, column=0, padx=5, pady=5)
location_entry = tk.Entry(root)
location_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Duration:").grid(row=6, column=0, padx=5, pady=5)
duration_entry = tk.Entry(root)
duration_entry.grid(row=6, column=1, padx=5, pady=5)


# Buttons for actions
tk.Button(root, text="Add Broadcast", command=add_broadcast).grid(row=8, column=0, padx=5, pady=5)
tk.Button(root, text="View All Broadcasts", command=view_broadcasts).grid(row=8, column=1, padx=5, pady=5)
tk.Button(root, text="Update Broadcast", command=update_broadcast).grid(row=9, column=0, padx=5, pady=5)
tk.Button(root, text="Delete Broadcast", command=delete_broadcast).grid(row=9, column=1, padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()

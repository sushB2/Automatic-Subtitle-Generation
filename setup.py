import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def generate_subtitles():
    video_path = entry_path.get()
    # Call your subtitle generation function here with video_path

# Create a basic GUI
app = tk.Tk()
app.title("Subtitle Generator")

label = tk.Label(app, text="Select Video File:")
label.pack()

entry_path = tk.Entry(app)
entry_path.pack()

browse_button = tk.Button(app, text="Browse", command=open_file_dialog)
browse_button.pack()

generate_button = tk.Button(app, text="Generate Subtitles", command=generate_subtitles)
generate_button.pack()

app.mainloop()

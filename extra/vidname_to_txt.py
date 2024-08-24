import os

# Directory containing the videos
video_directory = "D:/OSCP/OSCP"

# List to store video names
video_names = []

# Iterate over files in the directory
for filename in os.listdir(video_directory):
    # Check if the file is a video (you may need to adjust this condition based on your file extensions)
    if filename.endswith((".mp4", ".avi", ".mkv")):
        # Add the video name to the list
        video_names.append(filename)

# Path to the text file where you want to save the video names
txt_file_path = "D:/OSCP/OSCP/names.txt"

# Write video names to the text file
with open(txt_file_path, "w") as txt_file:
    for video_name in video_names:
        txt_file.write(video_name + "\n")

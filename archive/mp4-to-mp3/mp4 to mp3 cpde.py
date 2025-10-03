import os
from moviepy.editor import VideoFileClip


# Function to convert MP4 to MP3
def convert_mp4_to_mp3(input_folder):
    # Ensure the output folder exists
    output_folder = r'C:\Users\lenni\PycharmProjects\pythonProject1\mp4 to mp3\output'

    # Loop through each file in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(input_folder, filename)
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            mp3_path = os.path.join(output_folder, mp3_filename)

            # Load video clip
            video = VideoFileClip(mp4_path)

            # Write audio to file
            video.audio.write_audiofile(mp3_path)
            print(f"Converted: {filename} to {mp3_filename}")

    print("All MP4 files have been converted to MP3.")


# Specify the folder containing MP4 files
input_folder = r'C:\Users\lenni\PycharmProjects\pythonProject1\mp4 to mp3\input'

convert_mp4_to_mp3(input_folder)

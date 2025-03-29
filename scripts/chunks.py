import os
import subprocess

def split_video(video_path, chunk_duration=10):
    """Splits a video into chunks of specified duration and stores them in separate folders.

    Args:
        video_path (str): Path to the input video file.
        chunk_duration (int): Duration of each chunk in seconds (default: 10).
    """

    # Create a directory for the chunks
    output_dir = "chunks"
    os.makedirs(output_dir, exist_ok=True)

    # Get video duration using ffprobe
    try:
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of",
                                 "default=noprint_wrappers=1:nokey=1", video_path],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
        video_duration = float(result.stdout)
    except Exception as e:
        print(f"Error getting video duration: {e}")
        return

    num_chunks = int(video_duration // chunk_duration) + 1

    for i in range(num_chunks):
        start_time = i * chunk_duration
        chunk_folder = os.path.join(output_dir, f"chunk_{i+1}")
        os.makedirs(chunk_folder, exist_ok=True)
        output_path = os.path.join(chunk_folder, f"chunk_{i+1}.mp4")

        # Use ffmpeg to extract the chunk
        try:
            subprocess.run(["ffmpeg", "-ss", str(start_time), "-i", video_path, "-t", str(chunk_duration),"-c", "copy", output_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print(f"Created chunk {i+1}/{num_chunks}")
        except Exception as e:
            print(f"Error creating chunk {i+1}: {e}")

if __name__ == "__main__":
    video_path = str(input("Enter the path to the video file: "))
    split_video(video_path)
    print("Video splitting complete.")
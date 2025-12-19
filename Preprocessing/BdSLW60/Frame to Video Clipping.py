import os
import subprocess

# Define the root directory (input) and output directory for saving videos
#root_dir = r'C:\Users\shawo\Desktop\new approach\Word Folders'
root_dir = r"D:\shawon\BdSLW60 Full DataSet Version 2\BdSLW60 FINAL FRAMES FOLDER"
output_root_dir = r"D:\shawon\Min_9 and Max_164\No Frame Rate Corrected Clips"
#output_root_dir = r"C:\Users\shawo\Desktop\new approach\Only Video Clips"

# Function to create video using ffmpeg
def create_video_ffmpeg(trial_path, output_file, frame_rate=30):
    # Sort PNG files by frame number
    images = [img for img in os.listdir(trial_path) if img.endswith(".png")]
    images.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))  # Sort by frame number

    if len(images) == 0:
        print(f"No PNG files found in {trial_path}")
        return
    
    # Create a temporary file to hold the list of images
    with open(os.path.join(trial_path, 'image_list.txt'), 'w') as f:
        for image in images:
            f.write(f"file '{os.path.join(trial_path, image)}'\n")
    
    # FFmpeg command to create the video
    ffmpeg_command = [
        'ffmpeg',
        '-y',  # Overwrite output file if exists
        '-r', str(frame_rate),  # Input frame rate
        '-f', 'concat',  # Concatenate the image list
        '-safe', '0',  # Allow unsafe file paths
        '-i', os.path.join(trial_path, 'image_list.txt'),  # Input image list
        '-vcodec', 'libx264',  # Codec
        '-pix_fmt', 'yuv420p',  # Pixel format for better compatibility
        output_file  # Output video file
    ]
    
    # Run the ffmpeg command
    subprocess.run(ffmpeg_command)
    
    # Remove the temporary file
    os.remove(os.path.join(trial_path, 'image_list.txt'))
    
    print(f"Video saved as {output_file}")

# Loop through the root directory
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    if os.path.isdir(folder_path):
        for user_folder in os.listdir(folder_path):
            user_folder_path = os.path.join(folder_path, user_folder)
            if os.path.isdir(user_folder_path):
                # Create a corresponding directory in the output folder
                output_user_folder = os.path.join(output_root_dir, folder)
                os.makedirs(output_user_folder, exist_ok=True)
                
                for trial_folder in os.listdir(user_folder_path):
                    trial_path = os.path.join(user_folder_path, trial_folder)
                    if os.path.isdir(trial_path):
                        # Output video filename based on user folder and trial
                        output_file_name = f"{user_folder}_{trial_folder}.mp4"
                        output_file_path = os.path.join(output_user_folder, output_file_name)
                        
                        # Create the video using ffmpeg
                        create_video_ffmpeg(trial_path, output_file_path)

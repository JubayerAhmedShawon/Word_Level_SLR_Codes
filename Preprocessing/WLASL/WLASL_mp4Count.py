import os

# Define the root directory containing subdirectories with MP4 files
root_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\2000 Class"

# Define the output file path
output_file = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\mp4_file_counts.doc"

# Dictionary to store class (subdirectory) and MP4 file count
class_file_counts = {}

# Variable to track the total number of MP4 files
total_mp4_count = 0

# Walk through each subdirectory
for subdir, _, files in os.walk(root_directory):
    # Get the class name (last part of the subdirectory path)
    class_name = os.path.basename(subdir)
    
    # Count MP4 files in the current subdirectory
    mp4_count = sum(1 for file in files if file.endswith('.mp4'))
    
    # Add to the total count
    total_mp4_count += mp4_count
    
    # Only save non-zero counts
    if mp4_count > 0:
        class_file_counts[class_name] = mp4_count

# Write the counts to the .doc file
with open(output_file, 'w') as doc:
    doc.write("MP4 File Counts by Class:\n\n")
    for class_name, count in class_file_counts.items():
        doc.write(f"{class_name}: {count} MP4 files\n")
    doc.write("\n")
    doc.write(f"Total MP4 files: {total_mp4_count}\n")

print(f"MP4 file counts and total saved to {output_file}")

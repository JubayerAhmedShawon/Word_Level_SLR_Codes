import os

# Define the paths to the split directories
output_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\WLASL Dataset"
train_dir = os.path.join(output_directory, "train")
val_dir = os.path.join(output_directory, "val")
test_dir = os.path.join(output_directory, "test")

# Get the list of class (gloss) folders in each split
train_classes = set(os.listdir(train_dir))
val_classes = set(os.listdir(val_dir))
test_classes = set(os.listdir(test_dir))

# Find missing classes in the test folder
missing_in_test = (train_classes | val_classes) - test_classes

# Print the results
if missing_in_test:
    print("Classes missing in the test folder:")
    for gloss in missing_in_test:
        print(gloss)
else:
    print("No classes are missing in the test folder.")

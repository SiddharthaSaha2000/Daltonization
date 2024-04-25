import os
import subprocess

# Changes should be only in desired paths and command lines.

input_folder = "/Users/Taneem/daltonize/example_images/original"
output_folder = "/Users/Taneem/daltonize/example_images/deuteranopia"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of image files in the input folder
image_files = [f for f in os.listdir(
    input_folder) if os.path.isfile(os.path.join(input_folder, f))]

# Loop through each image file and run the command
for image_file in image_files:
    input_image_path = os.path.join(input_folder, image_file)
    output_image_path = os.path.join(
        output_folder, image_file[:-4] + "_deuteranope.jpg")
    command = f"python daltonize.py -d -t=d {
        input_image_path} {output_image_path}"
    subprocess.run(command, shell=True)


# The Commands
'''
python daltonize.py -d -t=p [Daltonization for Protanope]
python daltonize.py -s -t=p [Protanope Simulation]

python daltonize.py -d -t=d [Daltonization for Deutranope]
python daltonize.py -s -t=d [Deutranope Simulation]

python daltonize.py -d -t=t [Daltonization for Tritranope]
python daltonize.py -s -t=t [Tritanope Simulation]

'''

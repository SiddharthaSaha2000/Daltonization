import os


def rename_files(directory):
    for filename in os.listdir(directory):
        new_filename = filename.replace(' ', '_')  # Replace spaces with '_'
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        os.rename(old_filepath, new_filepath)


# Update with your data directory
data_dir = '/Users/Taneem/daltonize/example_images/original'
rename_files(data_dir)

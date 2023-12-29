from PIL import Image
import os
'''
# No Crop

folder_path = '/Users/junpeng/Documents/Code/project_website/images/gallery/fulls'
thumb_size = (400, 600)  # Set the desired thumbnail size (width, height)

def resize_and_pad_images_in_folder(folder_path, thumb_size, output_folder=None, background_color=(255, 255, 255)):
    """
    Resizes all JPEG images in the specified folder to fit within the given thumbnail size, 
    maintaining aspect ratio and adding padding to fill the thumbnail.

    :param folder_path: Path to the folder containing images.
    :param thumb_size: Tuple (width, height) for the thumbnail size.
    :param output_folder: Path to the folder where thumbnails will be saved.
                          If None, thumbnails will be saved in the same folder.
    :param background_color: Color used for padding (default is white).
    """
    if output_folder is None:
        output_folder = folder_path

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg")):
            try:
                with Image.open(os.path.join(folder_path, filename)) as img:
                    # Calculate new dimensions to maintain aspect ratio
                    img.thumbnail(thumb_size, Image.Resampling.LANCZOS)

                    # Create a new image with the specified thumbnail size
                    thumb = Image.new('RGB', thumb_size, background_color)

                    # Paste the resized image onto the center of the thumbnail
                    thumb_x = (thumb_size[0] - img.size[0]) // 2
                    thumb_y = (thumb_size[1] - img.size[1]) // 2
                    thumb.paste(img, (thumb_x, thumb_y))

                    # Save the thumbnail
                    output_path = os.path.join(output_folder, filename)
                    thumb.save(output_path, quality=95, optimize=True)

            except IOError:
                print(f"Error processing {filename}. Skipping file.")

    print(f"Thumbnails are saved in {output_folder}")

# Run the function
resize_and_pad_images_in_folder(folder_path, thumb_size)

    # Leaving margins
folder_path = '/Users/junpeng/Documents/Code/project_jojo/images/gallery/thumbs'
crop_size = (400, 600)  # Desired crop size: width x height

def crop_images_to_ratio(folder_path, crop_size, output_folder=None):
    """
    Crops all JPEG images in the specified folder to the given size, maintaining aspect ratio.

    :param folder_path: Path to the folder containing images.
    :param crop_size: Tuple (width, height) for the desired crop size.
    :param output_folder: Path to the folder where cropped images will be saved.
                          If None, images will be saved in the same folder.
    """
   
    if output_folder is None:
        output_folder = folder_path

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg")):
            try:
                with Image.open(os.path.join(folder_path, filename)) as img:
                    # Resize the image, maintaining aspect ratio
                    img.thumbnail((crop_size[0], crop_size[1] * img.size[0] // crop_size[0]), Image.Resampling.LANCZOS)

                    # Calculate cropping coordinates
                    left = (img.width - crop_size[0]) / 2
                    top = (img.height - crop_size[1]) / 2
                    right = (img.width + crop_size[0]) / 2
                    bottom = (img.height + crop_size[1]) / 2

                    # Crop the image to the desired size
                    img_cropped = img.crop((left, top, right, bottom))

                    # Save the cropped image
                    output_path = os.path.join(output_folder, filename)
                    img_cropped.save(output_path, quality=95, optimize=True)

            except IOError:
                print(f"Error processing {filename}. Skipping file.")

    print(f"Cropped images are saved in {output_folder}")

# Run the function
crop_images_to_ratio(folder_path, crop_size)
'''

folder_path = '/Users/junpeng/Documents/Code/project_website/images/gallery/fulls'
output_folder = '/Users/junpeng/Documents/Code/project_website/images/gallery/thumbs'
thumb_size = (400, 600)  # Desired thumbnail size: width x height

def create_cropped_thumbnails(folder_path, thumb_size, output_folder):
    """
    Creates cropped thumbnails for each JPEG image in the specified folder.

    :param folder_path: Path to the folder containing images.
    :param thumb_size: Desired thumbnail size as a tuple (width, height).
    :param output_folder: Path to the folder where thumbnails will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png")):
            with Image.open(file_path) as img:
                # Calculate aspect ratio of the thumbnail
                thumb_aspect = thumb_size[0] / thumb_size[1]
                # Calculate aspect ratio of the original image
                img_aspect = img.size[0] / img.size[1]

                if img_aspect > thumb_aspect:
                    # If image is wider than thumbnail (in aspect ratio sense)
                    scale = thumb_size[1] / img.size[1]
                    new_size = (int(img.size[0] * scale), thumb_size[1])
                else:
                    # If the image is taller than the thumbnail
                    scale = thumb_size[0] / img.size[0]
                    new_size = (thumb_size[0], int(img.size[1] * scale))

                # Resize the image to fit the thumbnail size
                img = img.resize(new_size, Image.Resampling.LANCZOS)

                # Calculate cropping box
                left = (img.size[0] - thumb_size[0]) / 2
                top = (img.size[1] - thumb_size[1]) / 2
                right = (img.size[0] + thumb_size[0]) / 2
                bottom = (img.size[1] + thumb_size[1]) / 2

                # Crop the image to the desired thumbnail size
                img = img.crop((left, top, right, bottom))

                # Save the cropped thumbnail
                img.save(os.path.join(output_folder, filename), quality=95, optimize=True)

    print(f"Thumbnails are saved in {output_folder}")

# Run the function
create_cropped_thumbnails(folder_path, thumb_size, output_folder)


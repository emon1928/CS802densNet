import os

def get_data_paths_list(image_folder, mask_folder):
    """Returns lists of paths to each image and mask."""
    
    print("**** in helper function ***")
    print("Image folder: ",image_folder)
    print("Mask folder: ",mask_folder)
    
    image_paths = [os.path.join(image_folder, x) for x in sorted(os.listdir(
        image_folder)) if x.endswith(".jpg")]
    mask_paths = [os.path.join(mask_folder, x) for x in sorted(os.listdir(
        mask_folder)) if x.endswith(".png")]
    
    
    return image_paths, mask_paths
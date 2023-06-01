import os
import shutil
from PIL import Image

directory = "./Dataset/"
ResizeScale=256
ExportToDataset=True

def check_tags_file(image_name):
    tags_folder = os.path.join(os.path.dirname(image_name), "tags")
    if not os.path.exists(tags_folder):
        os.makedirs(tags_folder)
    tags_file = os.path.join(tags_folder, f"{os.path.basename(image_name)[:-4]}.tags")
    if not os.path.exists(tags_file):
        with open(tags_file, "w") as f:
            pass
    return tags_file

for subdir, dirs, files in os.walk(directory):
    if subdir != directory:
        for file in files:
            filepath = os.path.join(subdir, file)
            if os.path.isfile(filepath) and filepath.endswith(".png"):
                with Image.open(filepath) as img:
                    if img.size != (16, 16):
                        print(filepath)
                    else:
                        tags_file = check_tags_file(filepath)
                        if(ExportToDataset):
                            new_folder = os.path.join("./Plixel/5_Plixel/")
                            if not os.path.exists(new_folder):
                                os.makedirs(new_folder)
                            new_image_path = os.path.join(new_folder, subdir.split("/")[-1]+"_"+os.path.basename(filepath))
                            new_tags_path = os.path.join(new_folder, subdir.split("/")[-1]+"_"+os.path.basename(tags_file)[:-5] + ".txt")
                            shutil.copy2(filepath, new_image_path)
                            shutil.copy2(tags_file, new_tags_path)
                            with Image.open(new_image_path) as new_img:
                                new_img = new_img.resize((ResizeScale, ResizeScale), resample=Image.NEAREST)
                                new_img.save(new_image_path)
            elif filepath.endswith(".tags"):
                pass
            else:
                print(filepath)
print("Data Imported")

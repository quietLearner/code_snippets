import concurrent.futures
import os
import time
from pathlib import Path

from PIL import Image, ImageFilter

script_location = Path(__file__).absolute().parent
file_location = script_location / "images"
processed_img_location = script_location / "processed"

print(file_location)

# filter return iterator
p = filter(Path.is_file, Path(file_location).rglob("*.jpg"))

# for f in p:
#     print(f.name)

# https://unsplash.com/
img_names = [f.name for f in p]
# print(img_names)


t1 = time.perf_counter()

size = (1200, 1200)


# io-bound, good candidate for Multithreading
def process_image(img_name):
    img = Image.open(file_location / img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)

    if not processed_img_location.is_dir():
        processed_img_location.mkdir(parents=True, exist_ok=False)
    img.save(processed_img_location / img_name)
    return f"{img_name} was processed..."


# no thread
# for img in img_names:
#     process_image(img)

with concurrent.futures.ThreadPoolExecutor() as executor:
    features = [executor.submit(process_image, img) for img in img_names]
    for f in concurrent.futures.as_completed(features):
        print(f.result())


t2 = time.perf_counter()

print(f"Finished in {t2-t1} seconds")

from PIL import Image, ImageFilter
from pathlib import Path

size_300 = (300, 300)

script_location = Path(__file__).parent
image_path = script_location / "IMG_3578.jpg"

image = Image.open(image_path)
# image.show()

# image.rotate(-90).show()

# convert to greyscale
image.convert("L").save(script_location / "greyscale.jpg")

image.rotate(-90).save(script_location / "rotated.jpg")

# blur image
image.filter(ImageFilter.GaussianBlur(15)).save(script_location / "blurred.jpg")

rotated_image = Image.open(script_location / "rotated.jpg")

rotated_image.thumbnail(size_300)

rotated_image.save(script_location / "rotated_300.jpg")

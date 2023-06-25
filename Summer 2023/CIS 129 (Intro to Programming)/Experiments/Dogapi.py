import requests
from PIL import Image
from io import BytesIO
import json


response = requests.get("https://dog.ceo/api/breeds/image/random")
json_data = response.json()

image_url = json_data['message']


# Make a request to the image URL and get the image data
image_response = requests.get(image_url)
image_data = image_response.content

# Create a PIL Image object from the image data
image = Image.open(BytesIO(image_data))

# Display the image
image.show()




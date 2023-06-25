import requests

response = requests.get("https://dog.ceo/api/breeds/list/all")

print(response.json())
data = response.json()
array = data['message']
userinput = input("What dog breed do you like to see?")

found_item = None
for item in array:
    if item == userinput:
        found_item = item

if found_item:
    image_url = f"https://dog.ceo/api/breed/{found_item}/images"
    image_response = requests.get(image_url)
    image_data = image_response.json()
    images = image_data['message']
    if images:
        print(f"Here are some images of {found_item}:")
        for image in images:
            print(image)
    else:
        print(f"No images found for {found_item}:")
else:
    print("Breed not found")







# if found_item:
#     print('Found item:', found_item)
# else:
#     print("Item not found in the array.")

# def returnbreed():

    
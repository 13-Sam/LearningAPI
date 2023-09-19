import requests
from PIL import Image
from io import BytesIO

# NASA APOD API endpoint and API key
endpoint = 'https://api.nasa.gov/planetary/apod'
api_key = 'DEMO_KEY'

# Set the query parameters
query_params = {'api_key': api_key, 'date': '2023-09-19'}

# Send a GET request to the API
response = requests.get(endpoint, params=query_params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Check if the media type is an image
    if data['media_type'] == 'image':
        image_url = data['url']
        
        # Download the image
        image_response = requests.get(image_url)
        
        # Open the image using PIL
        if image_response.status_code == 200:
            image_data = BytesIO(image_response.content)
            image = Image.open(image_data)
            
            # Display the image
            image.show()
        else:
            print("Failed to download the image")
    else:
        print("Media type is not an image")
else:
    print("Failed to retrieve data from NASA APOD API")


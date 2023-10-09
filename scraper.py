import requests
from bs4 import BeautifulSoup
import os

    


# Define the URL of the webpage you want to scrape
url = 'https://brickset.com/minifigs/year-2023/page-1'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now, you can extract data from the HTML using BeautifulSoup methods
    # For example, let's extract all the links on the page
    
    img_tags = soup.find_all('img')

    # Print the src attribute of each <img> tag (the image URL)
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            img_url = img_url.strip()
            if not img_url.startswith('http'):
                # Handle relative URLs by appending the base URL
                img_url = url + img_url
                

            # Extract the image filename from the URL
            img_filename = os.path.join('images', os.path.basename(img_url))


            if img_filename == "rlfm-white-logo.png":
                    print("skip!!!")
                    continue
            
            # Send an HTTP GET request to download the image
            img_response = requests.get(img_url)

            

            # Check if the image request was successful (status code 200)
            if img_response.status_code == 200:
                # Save the image to the specified filename
                
                

                
               
               
                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"Saved image: {img_filename}")
            else:
                print(f"Failed to download image: {img_url}")
    # Print the extracted links
    

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



#<img src="/assets/images/misc/rlfm-white-logo.png" alt="Recognised LEGO Fan Media">
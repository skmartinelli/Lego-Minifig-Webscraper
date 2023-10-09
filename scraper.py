import requests
from bs4 import BeautifulSoup
import os

# for year = range(1977,2023)
    # while 


# Check if the page has lego minifigs on it
onValidPage = 1

# First year that has minifigs
year = 1975

# Can edit year to be whatever current year it is, just writing 2099 to futureproof it
for year in range(1975,2099):
    print(f"year is now {year}")
    page = 1
    while onValidPage:
        print(f"page {page}")
        # Define the URL of the webpage you want to scrape
        url = f"https://brickset.com/minifigs/year-{year}/page-{page}" 




        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Create an empty dictionary to store the title-to-filename mapping
            title_to_filename = {}

            # Now, you can extract data from the HTML using BeautifulSoup methods
            # For example, let's extract all the links on the page
            img_tags = soup.find_all('img')
            print (f"images: {len(img_tags)}")
            if len(img_tags) == 1:
                print("No more pages")
                # pageExists = 0
                break

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

                    # If the image is the recognized lego fan media image, skip it
                    if img_filename == "images\\rlfm-white-logo.png":
                        continue

                    # Send an HTTP GET request to download the image
                    img_response = requests.get(img_url)

                    # Check if the image request was successful (status code 200)
                    if img_response.status_code == 200:
                        # Save the image to the specified filename
                        with open(img_filename, 'wb') as img_file:
                            img_file.write(img_response.content)
                        print(f"Saved image: {img_filename}")

                        # Extract the title (alt attribute) from the img tag
                        img_title = img.get('title')

                        # Add the title and filename to the mapping dictionary
                        title_to_filename[img_title] = img_filename
                    else:
                        print(f"Failed to download image: {img_url}")

            # Write the filename-to-title mapping to map.txt
            with open('map.txt', 'a') as map_file:
                for title, filename in title_to_filename.items():
                    map_file.write(f"{filename}: {title}\n")

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        page += 1

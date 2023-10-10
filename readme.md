# Minifig Scraper

This Python script is designed to scrape all minifigure images from the Brickset website for various years and pages. It utilizes concurrent programming to enhance efficiency. It is working as of October 9,2023, and the output will contain roughly 14,000 100kb images of minifigures, and a map.txt mapping the image filename to the full name of the lego minifigure.

## How to Use

1. Clone this repository or download the script to your local machine.

2. Make sure you have the required Python libraries installed. You can install them using pip:

   ```bash
   pip install beautifulsoup4 requests
   ```

3. Run the script using Python:

   ```bash
   python minifig_scraper.py
   ```

4. The script will scrape minifigure images from the Brickset website and save them in the "images" directory. A mapping of filename to minifigure name will be stored in the "map.txt" file.

## Twitter Follow @sammartinelli11 and Tweet License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), provided
that the person follows the Twitter account @sammartinelli11 and posts a tweet
on Twitter that says "Hello and thank you @sammartinelli11" with a link to the
project's repository.

If you meet the requirement of following @sammartinelli11 on Twitter and posting
the specified tweet, you are granted a limited, non-exclusive, revocable license
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, subject to the following conditions:

1. You must follow the Twitter account @sammartinelli11.

2. You must post a tweet on Twitter that says "Hello and thank you @sammartinelli11"
   with a link to the project's repository. The tweet must be visible to the public.

3. You must provide proof of your Twitter follow and the tweet upon request by the
   maintainers of the Software.

4. The above copyright notice and this Twitter Follow and Tweet License notice shall
   be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Note: This license includes a requirement to follow @sammartinelli11 on Twitter and
post a specific tweet as a condition for using the Software. If you do not meet
these requirements, you are not granted the rights to use, copy, modify, merge,
publish, distribute, sublicense, or sell the Software under this license.

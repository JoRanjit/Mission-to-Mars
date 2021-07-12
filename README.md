# Mission-to-Mars

## In this project we created a web app using BeautifulSoup and Splinter to scrape the latest news on the planet Mars.

### We scraped different websites to derive thes key componenets on the website:
  * The latest news relating to Mars
  * A very recent picture from the Mars
  * A table containing different facts related to Earth and Mars
  * Full-resolution images of Mars’s hemispheres 

#### The website also contains a button to scrape the most recent data from these sources and update the content accordingly.

We used MongoDB to store the scraped data for website to use.

Please Note: I tried to toggle between 2 pictures from different websites to be used as the 'Featured Mars Image".

#### This is screenshot of the Mars hemisphere full-resolution urls and their titles being stored in a list of dictionaries:
![Hemisphere urls and titles]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/hemisphere_image_url_list.PNG)


#### Here is screenshot from MongoDB 'Mars' collection with 'hemispheres' data scraped from 'Mars Hemispheres website' using scraping.py:
![MongoDB hemispheres data]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/MongoDB%20hemispheres%20added%20to%20Mars%20collection.PNG)

#### Here is the landing page from the website complete with the button to 'Srape New Data':

*Note - The featured image in this is from a idfferent website than some of the later ones:*
![homepage]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/MissiontoMars%20-%20portal%20page%20%231.PNG)

#### Next we used scraping.py and app.py to upload these images with titles from Mars DB to the website using index.html:
![hemispheres #1]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/MissiontoMars%20-%20portal%20page%20%232.PNG)

#### Then we made some html updates to make sure that the website is mobile compatible:
* iPhone compatible:

![Mobile compatibility-phoen]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/MissiontoMars%20-%20mobile%20compatible%20-%20iphone%20-%20%231.PNG)

* iPad compatible: 

![Mobile compatibility - ipad]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/MissiontoMars%20-%20mobile%20compatible%20-%20ipad.PNG)

#### Finally made some bootstrap formatting on the landing page:
![hemisphere thumbnails]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/Thumbnails%20-%20bootstrap.PNG)

#### Home page title formats, and scraping button color change etc. :
* Scraping button has a lighter blue shade background using 'btn-info'.
* 'Latest Mars News' title is in red font, and centralized.
* 2nd Heading is in blue font using "text-primary".
* The latest news section has light-yellow background.
* The featured Mars image title is centralized with red font.
* The facts table has borders using "table table-bordered" in scraping.py.
* Different 'Featured Image' than the previous screenshot.

![Home page update]( https://github.com/JoRanjit/Mission-to-Mars/blob/main/images/bootstrap%20updates%20to%20formatting.PNG)






# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

#this function initializes the browser, create a data dictionary and
# end the webdriver and return the scraped data

def scrape_all():
    #Initiate headliess driver for deployment
    executable_path = {'executable_path':ChromeDriverManager().install()}
    
    # the "headless" browsing session is when a browser is run without the users seeing it at all.
    browser = Browser('chrome',**executable_path,headless=False)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
            "news_title": news_title,
            "news_paragraph": news_paragraph,
            "featured_image": featured_image(browser),
            "facts": mars_facts(),
            'last_modified':dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    # The optional delay is useful because sometimes dynamic pages take a little while to load, 
    # especially if they are image-heavy.
    browser.is_element_present_by_css('div.list_text',wait_time=1)

    html=browser.html
    news_soup = soup(html,'html.parser')

    # Add try-except for error handling
    try:

        slide_elem = news_soup.select_one('div.list_text')
        # 'div.list_text' pinpoints the <div /> tag with the class of list_text
        # CSS works from right to left, such as returning the last item on the list instead of the first. 
        # Because of this, when using select_one, the first matching element returned will be a <li /> element 
        # with a class of slide and all nested elements within it.

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div',class_='content_title').get_text()
        
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div',class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


### JPL Space Images Featured Image
def featured_image(browser):

    #visit url
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)


    # Find and click the full image button
    full_image_elem=browser.find_by_tag('button')[1]
    full_image_elem.click()


    html=browser.html
    img_soup = soup(html,'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='headerimage fade-in').get('src')
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    
    return img_url

def mars_facts():

    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    # BaseExcepyion is raised when any of the built-in exceptions are encountered and it won't handle any user-defined exceptions.
    except BaseException:
        return None


    df.columns = ['Description', 'Mars','Earth']
    df.set_index('Description',inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":
    # if running as script, print scraped data
    print(scrape_all)

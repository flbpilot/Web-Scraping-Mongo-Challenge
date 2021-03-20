# Import Dependencies
from splinter import Browser, browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import os





def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)
    
def scrape():
    browser = init_browser()

    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)
    
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'lxml')

    mars_results = soup.find('li', class_='slide')

    article_title = mars_results.find('div', class_='content_title').text
    article_body = mars_results.find('div', class_='article_teaser_body').text




    
    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url)
    html = browser.html
   
    soup = bs(html, 'html.parser')
    image = soup.find_all('div', class_='header')[0]

    featured_image = image.find('img', class_='headerimage fade-in')
    featured_image = featured_image.attrs.get('src', None)

    url = os.path.dirname(url)

    featured_image_url = f'{url}/{featured_image}'    




    mars_data_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_data_url)
    mars_df = tables[0]

    mars_data = mars_df.to_html(index = False, header = False)

    
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    
    html = browser.html
    hemisphere_soup = bs(html, 'lxml')
    hemisphere_results = hemisphere_soup.find_all('div', class_='item')

    hemisphere_data = []
    for result in hemisphere_results:      
        hemisphere_info = {}
        title = result.find('h3').text
        hemisphere_info['title'] = title


        base_url = 'https://astrogeology.usgs.gov'
        img_src = result.find('a')['href']
        img_url = f'{base_url}{img_src}'

        picture_url = img_url
        browser.visit(picture_url)
        
        html = browser.html
        soup = bs(html, 'html.parser')

        picture_results = soup.find('img', class_='wide-image')['src']

        full_img_url = f'{base_url}{picture_results}'
    
        hemisphere_info['img_url'] = full_img_url

        hemisphere_data.append(hemisphere_info)




    mars_dict = {
        "article_title": article_title,
        "article_body": article_body,
        "featured_image": featured_image_url,
        "mars_facts": mars_data,
        "hemisphere_data": hemisphere_data
        }

    browser.quit()

    return mars_dict
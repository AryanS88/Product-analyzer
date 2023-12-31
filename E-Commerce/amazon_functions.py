from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import re
from PIL import Image
from io import BytesIO

    # Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'a-price-whole'}).text
        price = price.replace(',', '')  # remove commas from price
    except AttributeError:
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip()
            price = price.replace(',', '')
            price = price.replace('.', '')# remove commas from price
        except:
            price = ""

    return price


# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count



def get_image(soup):
    try:
        img_src=str(soup.find("img", attrs={'class':'a-dynamic-image a-stretch-horizontal'}))
    except AttributeError:
        img_src = " "
    
    return img_src    

def extract_single_image_url_amazon(soup):

    # Find the image source code in the parsed HTML
    try:
        img_src = str(soup.find("img", attrs={'class':'a-dynamic-image a-stretch-horizontal'}))
    except AttributeError:
        img_src = ""

    # If the image source code is empty, return an empty string
    if not img_src:
        return ""

    # Extract the image URL using regular expressions
    pattern = r'"(https://m\.media-amazon\.com/images/.+?\.(jpg|png))"'
    matches = re.findall(pattern, img_src)
    img_url = matches

    return img_url
  
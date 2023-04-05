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
        title = soup.find("span", attrs={"class":'B_NuCI'})
        
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
        price = soup.find("div", attrs={'class': '_30jeq3 _16Jk6d'}).text
        price = price.replace(',', '')  # remove commas from price
    except AttributeError:
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'class': '_30jeq3 _16Jk6d'}).string.strip()
            price = price.replace(',', '')
            price = price.replace('₹', '')# remove commas from price
        except:
            price = ""

    return price


# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("div", attrs={'class':'_3LWZlK'}).text
    
    except AttributeError:
        rating = ""	

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'class':'_2_R_DZ'}).text
        review_count = review_count[:review_count.find("Ratings")+7]
    except AttributeError:
        review_count = ""	

    return review_count

  

def extract_flipkart(soup):
    # Find the image source code in the parsed HTML
    try:
        img_tag = soup.find("img", attrs={'class':"_396cs4 _2amPTt _3qGmMb"})
        if not img_tag:
            return ""
        
        img_src = img_tag.get('src')
    except AttributeError:
        img_src = ""

    # If the image source code is empty, return an empty string
    if not img_src:
        return ""
    
    
    return img_src
  
  
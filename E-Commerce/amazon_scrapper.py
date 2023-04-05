from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import re
from PIL import Image
from io import BytesIO
import csv
from amazon_functions import*
# from search import search

if __name__ == '__main__':
   
    HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
    
    search_text=input("enter the name of the product ")
    # The webpage URL
    amazon_URL = "https://www.amazon.in/s?k="+search_text

    # HTTP Request
    webpage = requests.get(amazon_URL, headers=HEADERS)

    # Soup Object containing all data
    amazon_soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    amazon_links = amazon_soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in amazon_links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[], "img_src":[]}
    
    # Loop for extracting product details from each link 
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

        new_amazon_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_amazon_soup))
        d['price'].append(get_price(new_amazon_soup))
        d['rating'].append(get_rating(new_amazon_soup))
        d['reviews'].append(get_review_count(new_amazon_soup))
        d["img_src"].append(extract_single_image_url_amazon(new_amazon_soup))

    file_name_az="az"+search_text+".csv"   
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("az"+search_text+".csv", header=True, index=False)


# Open the CSV file
with open(file_name_az, 'r') as file:
    reader = csv.reader(file)

    # Skip the header row if necessary
    next(reader)

    # Initialize variables to store the minimum value row
    min_value = None
    min_row = None
    column_index = 1  # replace with the index of the desired column

    # Loop through each row in the CSV file
    for row in reader:
        try:
            # Extract the numeric value from the desired column
            value = float(row[column_index])
        except ValueError:
            # Skip the row if the value is not numeric
            continue

        # Update the minimum value and row if necessary
        if min_value is None or value < min_value:
            min_value = value
            min_row = row

    # Store the values from the minimum row in separate variables
    if min_row is not None:
        title, price, stars, ratings, col5 = min_row  # replace with the desired number of columns
        col5_list = col5_str.split(',')  # convert the comma-separated string to a list
        col5_first_elem = col5_list[0][3:]
        col5_first_elem=col5_first_elem.replace("'",'')
        # remove the '[' character from the beginning of the first element
        print(f"The row with the minimum value of {min_value} is:")
        print(f"title: {title}")
        print(f"price: {price}")
        print(f"stars: {stars}")
        print(f"ratings: {ratings}")
        print(f"image: {col5_first_elem}")
    else:
        print("No valid rows found.")


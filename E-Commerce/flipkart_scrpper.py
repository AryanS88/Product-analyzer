from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import re
from PIL import Image
from io import BytesIO
import csv
from flipkart_functions import *
# from search import Search

fkst=input("enter the name of the product ")
# fkst=Search.entry.get()
if __name__ == '__main__':

    # add your user agent 
   


    HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
    
    # The webpage URL
    flipkart_URL = "https://www.flipkart.com/search?q="+fkst

    # HTTP Request
    webpage = requests.get(flipkart_URL, headers=HEADERS)

    # Soup Object containing all data
    flipkart_soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    flipkart_links = flipkart_soup.find_all("a", attrs={'class': '_1fQZEK'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in flipkart_links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[],"img_src":[]}
    
    # Loop for extracting product details from each link 
    for link in links_list:
        new_flipkart_webpage = requests.get("https://www.flipkart.com" + link, headers=HEADERS)

        new_flipkart_soup = BeautifulSoup(new_flipkart_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_flipkart_soup))
        d['price'].append(get_price(new_flipkart_soup))
        d['rating'].append(get_rating(new_flipkart_soup))
        d['reviews'].append(get_review_count(new_flipkart_soup))
        d['img_src'].append(extract_flipkart(new_flipkart_soup))
    
    flipkart_df = pd.DataFrame.from_dict(d)
    flipkart_df['title'].replace('', np.nan, inplace=True)
    flipkart_df = flipkart_df.dropna(subset=['title'])
    flipkart_df.to_csv("fk"+fkst+".csv", header=True, index=False)


file_name="fk"+fkst+".csv"
# Open the CSV file for reading
with open(file_name, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Get the second row and store the values in separate variables
    try:
        row = next(reader)
        col1, col2, col3, col4, col5 = row[0], row[1], row[2], row[3], row[4]
        print(f"Column 1: {col1}")
        print(f"Column 2: {col2[2:]}")
        print(f"Column 3: {col3}")
        print(f"Column 4: {col4}")
        print(f"Column 5: {col5}")
    except StopIteration:
        print("No rows found.")
    next(reader)

    # Get the second row and store the values in separate variables
    try:
        row = next(reader)
        col11, col12, col13, col14, col15 = row[0], row[1], row[2], row[3], row[4]
        print(f"Column 11: {col11}")
        print(f"Column 12: {col12[2:]}")
        print(f"Column 13: {col13}")
        print(f"Column 14: {col14}")
        print(f"Column 15: {col15}")
    except StopIteration:
        print("No rows found.")
#!/usr/bin/python3

# connect to an API using Python
import requests
import csv

base_url = "https://jsonplaceholder.typicode.com/posts"
# retrieve data from server
response = requests.get(base_url)

def fetch_and_print_posts():
                
        print("Status Code: {}".format(response.status_code))
        # check if the request was successful (status code 200)
        if response.status_code == 200:
            #if response return in JSON, convert to python dict using .json() method
            posts = response.json()
            # iterate through json data and print titles
            for post_dict in posts:
                 print("{}".format(post_dict['title']))
        else:
             print("Failed to retrieve data")

def fetch_and_save_posts():
    if response.status_code == 200:
        # convert json to list of dicts
        posts = response.json()
        
        #define csv column keys
        fieldnames = ['userId', 'id', 'title', 'body']
        
        # write data into a csv file
        with open("posts.csv", mode="w", encoding="utf-8") as csvfile:
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
             writer.writeheader() # write column names
             writer.writerows(posts) #writes all posts at once as rows
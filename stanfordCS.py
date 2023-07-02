import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://web.stanford.edu/class/cs"

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Link"])
    
    for i in range(100,400):  # for numbers 0-1000
        url = base_url + str(i)
        time.sleep(2)  # Wait for 2 seconds
        try:
            response = requests.get(url, timeout=5)  # Timeout after 5 seconds
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a')  # Finds all 'a' tags (links)
                
                for link in links:
                    href = link.get('href')
                    if href:
                        writer.writerow([url, href])
            else:
                print(f"The URL {url} does not exist.")
        except requests.exceptions.RequestException as err:
            print ("Something went wrong: ",err)
            continue
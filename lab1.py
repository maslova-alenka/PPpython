import requests
from bs4 import BeautifulSoup
import os
import re

URL="https://yandex.ru/images/"
HEADERS={"User-Agent":"Mozilla/5.0"}


def get_image(image_url, name, index):
    if not os.path.isdir(name):
        os.mkdir(name)
    picture = requests.get(f"https:{image_url}", HEADERS)
    saver = open(os.path.join(f"{name}/{str(index).zfill(4)}.jpg"), "wb")
    saver.write(picture.content)   
    saver.close()

def download_images(path, key) :
    os.chdir(path)
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    os.chdir("dataset")

    count = 990#  990 960
    page = 33 #   33  32
    
    #for count in range(1000):
    while count < 1000:
        key1=key.replace(" ", "%20")
        url = f'{URL}search?p={page}&text={key}'
        print(f"Fetching URL: {url}")
        
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        images = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
    
        #try:
        if not images:
            print("No images.")
            break
        
        for image in images:
            if count == 1000:
                return
        
            image_url = image.get("src")
            if image_url and not image_url.startswith("data:"):
                get_image(image_url, key, count)
                count += 1
        print(count)
        page += 1
        #except: 
         #   pass
            
def main():
    directory = os.getcwd()
    download_images(directory, 'cat')
    #download_images(directory, 'dog')

if __name__ == "__main__":
    main()


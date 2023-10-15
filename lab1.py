import requests
from bs4 import BeautifulSoup
import os

URL="https://yandex.ru/images/"
headers={"User-Agent": "Mozilla/5.0"}

def download_image(path, key):
    response=requests.get(URL,headers)
    
    soup=BeautifulSoup(response.text, "lxml")
    images=soup.findAll('img', class_='serp-item__thumb justifier__thumb')
    if not images:
        print("No images found")
        

    
    
    
    
   
   
def main():
    directory=os.getcwd()
     
    
if __name__=="__main__":
    main()

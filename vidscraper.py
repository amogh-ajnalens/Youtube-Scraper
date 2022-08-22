import csv
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytube import YouTube

def down(link,storedir):
    yt = YouTube(link)
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download(storedir)
    print("Download completed!!")



def getUrls(searchTerm):

    noOfVideos=3 #Set this to the number of videos you want to download

    if searchTerm in os.listdir():
        ae=True
        print(searchTerm+" already exists.")
    else:
        os.mkdir(searchTerm)

    

    options = webdriver.ChromeOptions()
    #options.add_argument(r"--user-data-dir=C:\Users\amogh\AppData\Local\Google\Chrome\User Data")
    #options.add_argument(r'--profile-directory=Profile 2')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)




    driver.get("https://www.youtube.com/results?search_query="+searchTerm+"&sp=EgIYAw%253D%253D")

    user_data = driver.find_elements(
            by=By.XPATH,
            value='//*[@id="video-title"]'
        )

    links = []
    for i in user_data:
                links.append(i.get_attribute('href'))

    totalLinks=len(links)

    rl=totalLinks-noOfVideos


    print(links)
    nl=[]
    for i in links:
        if i==None:
            links.remove(i)
        else:
            nl.append(i)
    print(nl)
    del nl[-rl:]


    cwd=os.getcwd()+"/"
    
    storedir=cwd+searchTerm+"/"

    for i in nl:
        print(i)
        down(i,storedir)

    sleep(2)


with open('keywords.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        getUrls(row[0])

sleep(2)
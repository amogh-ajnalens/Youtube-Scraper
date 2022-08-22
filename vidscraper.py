from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytube import YouTube

def down(link):
    yt = YouTube(link)
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download()
    print("Download completed!!")


searchTerm = input("Enter Your Search Term : ")
noOfVideos= int(input("Enter Number of Videos you want to Download : "))


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

for i in links:
    if i=="None":
        links.remove(i)

del links[-rl:]



for i in links:
    print(i)
    down(i)

sleep(2)
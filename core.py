import  requests
import lxml
import datetime
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

url = "https://wall.alphacoders.com/by_sub_category.php?id=169958&name=Minecraft+Wallpapers"

page = requests.get(url)

print(page.text)


soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())

##print(soup.find_all('img'))


imgresults = soup.findAll("img")

print(imgresults.__len__())
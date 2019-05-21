from bs4 import BeautifulSoup
import requests

query = 'python'
dict =""
url ='http://www.google.com/search?q='
page = requests.get(url + query)
soup = BeautifulSoup(page.text, 'html.parser')
h3 = soup.find_all("h3",class_="r")
for elem in h3:
    el=elem.contents[0]
    url = el["href"]
    if 'wiki' in url:
        link=("https://www.google.com" + url)
        break
page = requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')
text = soup.find(id="mw-content-text")
p= text.find("p")
while p != None:
	dict+=p.get_text()+"\n"
	p = p.find_next("p")
dict=dict.split()
print(dict)
from bs4 import BeautifulSoup
import requests

def get():
    url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9C%D0%B5%D0%BB%D0%B8%D1%85%D0%BE%D0%B2%D0%BE,_%D0%A7%D0%B5%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD'
    try:
        responce = 'Сервер погоды недоступен'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        elem = soup.find('div', { 'id' : 'archiveString'})
        temp = elem.find('span', {'class' : 't_0'})
        info = elem.find('div', {'class' : 'ArchiveInfo'})
        responce = 'Сейчас ' + temp.text + ', '
        responce += info.contents[0]
        responce += info.contents[1].text
        responce += info.contents[4]
        responce += info.contents[5].text
        responce += info.contents[10]
        return responce
    except:
        return responce
    

#print(get())
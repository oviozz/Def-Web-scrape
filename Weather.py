from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

try:
    user = str(input('Weather Location: '))



    url = requests.get('https://www.google.com/search?q={}+weather'.format(user), headers=headers).text

    soup = BeautifulSoup(url, 'lxml')
    temp = soup.find('span',class_='wob_t q8U8x').text
    info = soup.find('div',class_='wtsRwe').text
    time = soup.find('div',class_='wob_dts').text



    #splits capital letter so i can make a new line
    y = re.findall('[A-Z][^A-Z]*',info)



    #print all the values
    print('************************************************************')
    print(time)
    print('The Temperature is {} °F'.format(temp))
    for i in y:
        print('- {}'.format(i))
    print('************************************************************')

except AttributeError:
    print('Wrong Location')

from bs4 import BeautifulSoup
import requests
import lxml

word = str(input("Definition: "))

#gets def of the word
url = requests.get('https://www.vocabulary.com/dictionary/{}'.format(word)).text
soup = BeautifulSoup(url,'lxml')
before = soup.find('div',class_='word-area')
try:
    after = before.find('p', class_='short').text
    long = before.find('p', class_='long').text

    # gets synonyms
    syn = soup.find('div', class_='defContent')
    final = syn.find('a', class_='word').text

    # prints out
    print(after)
    print('Synonyms: {}'.format(final))
    print('---------------------------------------------------')
    response = str(input("Do you want longer definition: ")).lower()
    if response == 'yes':
        print(long)
    else:
        print('No worries')

except AttributeError:
    print('Not a valid word')

from bs4 import BeautifulSoup
import requests


#Просуммировать все числа из таблицы по адресу ниже
page_url1 = "https://stepik.org/media/attachments/lesson/209723/3.html"
page_url2 = "https://stepik.org/media/attachments/lesson/209723/4.html"
page_url3 = "https://stepik.org/media/attachments/lesson/209723/5.html"

def get_html(url):
    return requests.get(url)
    
def parse_html(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    summ = 0
    for number in soup.find_all('td'):
       summ += int(number.getText())
    
    print(summ)

def main():
    parse_html(get_html(page_url1))
    parse_html(get_html(page_url2))
    parse_html(get_html(page_url3))
    
if __name__ == '__main__':
    main()
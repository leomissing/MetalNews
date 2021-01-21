import requests
from bs4 import BeautifulSoup


def info(info):
    href_post = info.find('a', href=True)
    img_post = info.find('img', src=True)
    title_post = info.find('div', class_='col-5_new').find('a').find('h2').text
    excerpt_post = info.find('div', class_='col-5_new').find('div', class_='excerpt').text.strip()
    text_src = BeautifulSoup(requests.get(href_post['href']).text, 'lxml')
    text_post = text_src.find('div', class_='flexible_content_wrap').text.rstrip()
    return href_post['href'], img_post['src'], title_post, excerpt_post, text_post


url = 'https://rockcult.ru/news/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='teaser_feed_common')


def get_news():
    return info(quotes[0])


def main():
    print(str(info(quotes[0])[2]) + '\n')
    return 0

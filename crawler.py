# -*- coding: utf-8 -*-

import bs4
import re
import requests
import os
import datetime
from data_manager import bulk_insert

#Read categories addresses from a text file provided by user and rettuens addresses for current date
def create_urls():
    filePath = os.path.join(os.path.dirname(__file__), 'categories.txt')
    urls = open(filePath,'r').readlines()
    today = datetime.date.today()
    date_tag = f'/{today.year}/{today.strftime("%b")}/{today.day}'
    urls = [re.sub('\n','', url) + date_tag for url in urls]
    return urls

#Find relevant articles links in each page
def find_articles(url):
    page = requests.get(url)
    page_content = bs4.BeautifulSoup(page.content,'html.parser')
    all_links = page_content.find_all('a')
    articles_links = []
    for link in all_links:
        potential_link = re.findall('https://www.theguardian.com/[a-zA-Z0-9]+-*[a-zA-Z0-9]*/\d+/.*/\d+/(?!all).*',str(link.get('href')))
        if len(potential_link) != 0:
            articles_links.append(potential_link[0])
    return list(set(articles_links))

#Find article fields: link, headline, date, category, and content
def parse_article(link):
    page = requests.get(link)
    page_content = bs4.BeautifulSoup(page.content,'html.parser')
    result = {}

    result['link'] = link
    try:
        category_element = page_content.find('span', class_='label__link-wrapper')
        category = str(category_element.getText(strip=True))#.encode('utf-8')
        result['category'] = category

        headline_element = page_content.find('h1',class_='content__headline ')
        headline = str(headline_element.getText(strip=True))#.encode('utf-8')
        result['headline'] = headline

        date_element = page_content.find('time',itemprop='datePublished')
        date = str(date_element.getText(strip=True))#.encode('utf-8')
        result['date'] = date
    
        post_parts = page_content.find_all('p')
        post = ''
        for part in post_parts:
            text = re.sub('\n',' ',str(part.getText()))
            post += text
        #post = post.encode('utf-8')
        result['post'] = post
    except:
        pass
    return result

def main():
    urls = create_urls()
    article_links = []
    for url in urls:
        article_links += find_articles(url)
    articles_collection = []
    for link in article_links:
        articles_collection.append(parse_article(link))
    bulk_insert(articles_collection)

if __name__ == '__main__': main()
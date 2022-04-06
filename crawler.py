import bs4
import re
import requests
import os
import datetime
from data_manager import bulk_insert

#Read categories addresses from a text file and generates today's links
def create_todays_links():
    filePath = os.path.join(os.path.dirname(__file__), 'categories.txt')
    page_links = open(filePath,'r').readlines()
    today = datetime.date.today()
    date_tag = f'/{today.year}/{today.strftime("%b")}/{today.day:02d}'
    todays_links = [re.sub('\n','', link) + date_tag for link in page_links]
    return todays_links

#Find relevant articles links in each page
def find_article_links(url):
    try:
        page = requests.get(url)
        page_content = bs4.BeautifulSoup(page.content,'html.parser')
    except:
        raise ConnectionError(f'Error in getiing the content of <{url}>.')
    
    all_links = page_content.find_all('a')
    articles = []
    for link in all_links:
        article_link = next(iter(re.findall('https://www.theguardian.com/[a-zA-Z0-9]+-*[a-zA-Z0-9]*/\d+/.*/\d+/(?!all).*',str(link.get('href')))),None)
        if article_link:
            articles.append(article_link)
    unique_article_links = list(set(articles))
    return unique_article_links

#Find article fields: link, headline, date, category, and content
def parse_article(link):
    try:
        page = requests.get(link)
    except:
        raise ConnectionError(f'Error in getting article page: {link}')
    
    page_content = bs4.BeautifulSoup(page.content,'html.parser')
    
    result = {}
    result['link'] = link

    try:
        headline_element = page_content.find("h1",class_="dcr-125vfar")
        headline = str(headline_element.getText(strip=True))
        result["headline"] = headline

        category_element = page_content.find("meta", property="article:section")
        category = category_element.get("content")#.encode('utf-8')
        result["category"] = category

        date_element = page_content.find("summary",class_="dcr-12fpzem")
        date = str(date_element.getText(strip=True))#.encode('utf-8')
        result["date"] = date
    
        post_parts = page_content.find_all('p')
        post = ''.join([re.sub('\n',' ',str(part.getText())) for part in post_parts])
        result["post"] = post
    except:
        pass

    return result

def main():
    page_links = create_todays_links()
    article_links = []
    for url in page_links:
        try:
            article_links = find_article_links(url)
        except ConnectionError as e:
            return {'Status':False,'Message':f'Error in finding the articles links in page <{url}>.'}
        
        articles_collection = []
        for link in article_links:
            try:
                article = parse_article(link)
            except Exception as e:
                return {'Status':False,'message':f'Error in parsing the article: {str(e)}'}
            else:
                if article:
                    articles_collection.append(article)
        
        try:
            bulk_insert(articles_collection)
        except Exception as e:
            return {'Status':False ,'message':str(e)}
    
    return {'Status':True,'message':'Operation finished successfully'}

if __name__ == '__main__':
    result = main()
    print(result['message'])

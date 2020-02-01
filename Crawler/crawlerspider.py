#! /usr/bin/env python

import requests,re,urlparse
#find hiddden files by checking hrefs in the html code

target_url="https://stea1th.tech"
target_links=[]

def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"',response.content)

def crawl(url):
    href_links= extract_links(url)
    for links in href_links:
        link= urlparse.urljoin(url,links)

        if '#' in link:
            link = link.split('#')[0]
        
        if target_url in link and link not in target_links:
            target_links.append(links)
            print(link)
            print("\n")
            crawl(link)

crawl(target_url)
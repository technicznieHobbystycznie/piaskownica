
import requests

url = 'https://www.python.org/downloads/'


def simple_crawler(url):

    site = requests.get(url).text
    links = site.split('href="')
    links_python = []
    for l in links:
        link = l.split('"')[0]
        if 'http' in link:
            links_python.append(link)
    return links_python


links_python = simple_crawler(url)
links_python = list(set(links_python))
in_total = len(links_python)
all_links = links_python.copy()

while links_python:
    link = links_python.pop(0)
    new_links = simple_crawler(link)
    new_links = list(set(new_links))
    new_links_ok = []
    for nl in new_links:
        if nl in all_links:
            pass
        else:
            new_links_ok.append(nl)
            all_links.append(nl)
    in_total += len(new_links_ok)
    links_python.extend(new_links_ok)
    print(len(links_python))
import requests
from xml.dom.minidom import parse
import xml.dom.minidom
import random
from configs import proxy, root_path


def get_one_page(url):
    print('GET', url)
    response = requests.get(url, verify=False, proxies=proxy)
    if response.status_code == 200:
        return response.text
    return None


def parse_arxiv_content(response):
    DOMTree = xml.dom.minidom.parseString(response)
    collection = DOMTree.documentElement
    entrys = collection.getElementsByTagName("entry")
    print('length', len(entrys))
    papers = []
    for e in entrys:
        url_id = e.getElementsByTagName('id')[0].childNodes[0].data
        updated = e.getElementsByTagName('updated')[0].childNodes[0].data
        published = e.getElementsByTagName('published')[0].childNodes[0].data
        title = e.getElementsByTagName('title')[0].childNodes[0].data.replace('\n', ' ')
        summary = e.getElementsByTagName('summary')[0].childNodes[0].data.replace('\n', ' ')
        authors = [a.getElementsByTagName('name')[0].childNodes[0].data for a in e.getElementsByTagName('author')]
        if len(e.getElementsByTagName('category')) > 1:
            categorys = [a.getAttribute('term') for a in e.getElementsByTagName('category')]
        else:
            categorys = [e.getElementsByTagName('category')[0].getAttribute('term')]

        comments =[]
        if len(e.getElementsByTagName('arxiv:comment')) == 1:
            comments = [e.getElementsByTagName('arxiv:comment')[0].childNodes[0].data.replace('\n', ' ')]
        elif len(e.getElementsByTagName('arxiv:comment')) > 1:
            comments = [a.childNodes[0].data.replace('\n', ' ') for a in e.getElementsByTagName('arxiv:comment')]
        papers.append((url_id, updated, published, title, summary, authors, categorys, comments))
    return papers



if __name__ == '__main__':
    url = 'https://export.arxiv.org/api/query?id_list=2201.08845,2202.00181'
    response = get_one_page(url)
    papers = parse_arxiv_content(response)
    print(len(papers))

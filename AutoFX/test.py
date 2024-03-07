import urllib.request as libreq
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=au:del_maestro+AND+ti:checkerboard') as url:
    r = url.read()
print(r)
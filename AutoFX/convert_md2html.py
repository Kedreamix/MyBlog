import markdown

with open('arxiv/2022-02-15/abs.md', 'r', encoding='utf-8') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('arxiv/2022-02-15/abs.html', 'w', encoding='utf-8') as f:
    f.write(html)

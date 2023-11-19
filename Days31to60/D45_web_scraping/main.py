from bs4 import BeautifulSoup
# import lxml

with open('Days31to60/D45_web_scraping/website.html', 'r', encoding='utf-8') as file:
    # Read the entire file
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

# select CSS elements
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name.getText())

headings = soup.select(".heading")
print(headings)

a_tags = soup.find_all(name="a")
print(a_tags)

a_tags_b = soup.a
print(a_tags_b)

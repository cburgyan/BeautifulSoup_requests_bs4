import bs4
import requests
# import lxml


# with open("website.html", encoding="utf8") as file:
#     file_str = file.read()
#
# soup = BeautifulSoup(file_str, "html.parser")
# print(type(soup))
# print(soup.title)
# print(type(soup.title))
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)
# print(soup.prettify())
# print(soup.li)
# print(soup.p)
# print(type(soup.h1.getText()))
# print(soup.h1.getText())
# print(type(soup.h1.string))
# print(soup.h1.string)

# all_anchor_tags = soup.find_all(name="a")
# print(type(all_anchor_tags))

# all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)

# for tag in all_anchor_tags:
    # print(type(tag))
    # print(tag.getText())
    # print(tag.get("href"))

# print(type(soup.find(name="h1", class_="foo38")))
# print(soup.find(name="h1", class_="foo38"))

response = requests.get("https://news.ycombinator.com")

html_response = response.text

soup = bs4.BeautifulSoup(html_response, "html.parser")

# title_str = soup.select_one(".titlelink")
# print(title_str.string)
#
# title_score = soup.select_one(".score")
# print(title_score)
# print(title_score.string)

#
# article_title = soup.find(name="a", class_="titlelink")
# print(article_title.string)
# article_link = article_title.get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score")
# print(article_upvote.string)


articles = soup.find_all(name="a", class_="titlelink")
article_upvote_tags = soup.find_all(name="span", class_="score")
article_upvote_tags2 = soup.find_all(name="td", class_="subtext")
article_texts = []
article_links = []
article_upvotes = []
count = 0
max_score = 0
max_title = ""
max_link = ""
max_number = 0
for article in articles:
    article_texts.append(article.get_text())
    article_links.append(article.get("href"))
    print(f"{count + 1}. Name: {article.get_text()}")
    print(f"\tlink: {article.get('href')}")
    subtext_string_list = article_upvote_tags2[count].get_text().replace('\n', '').split()
    if subtext_string_list[1] == "points":
        if max_score < int(subtext_string_list[0]):
            max_score = int(subtext_string_list[0])
            max_title = article.get_text()
            max_link = article.get('href')
            max_number = count + 1
        print(f"\tscore: {subtext_string_list[0]}")
    else:
        print(f"\tscore: --")
    count += 1
print("\n\n")
print(f"{max_number}. MAX SCORE: Name: {max_title}")
print(f"\tlink: {max_link}")
print(f"\tscore: {max_score}")

    # if len(article_upvote_tags) - 1 < count:
    #     print("NO more upvotes")
    # else:
    #     article_upvotes.append(article_upvote_tags[count].get_text())
    #     print(article_upvote_tags[count].get_text())


# for index in range(len(articles) - 1):
#     print(articles[index].get_text())
#     print(article_upvotes[index].get_text())

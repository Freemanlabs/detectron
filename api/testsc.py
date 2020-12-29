from plagiarism_checker import check_plagiarism

# check_plagiarism(
#     "json/ita.json", "uploads/ITA_Training_Homework_Session_2_-_Charles_Yusuf.txt",
# )
# check_plagiarism(
#     "json/tanya.json", "uploads/tanya.txt",
# )
# print(perc)

# from get_urls import urls
# from scraper import ScraperSpider
# from scrapy.crawler import CrawlerProcess

# with open("uploads/ITA_Training_Homework_Session_2_-_Charles_Yusuf.txt", "r") as f:
#     text = f.read()

# url_list = urls(text)

# process = CrawlerProcess()
# process.crawl(ScraperSpider, urls=url_list)
# process.start()

from nltk.tokenize import sent_tokenize, word_tokenize

with open("uploads/ITA_Training_Homework_Session_2_-_Charles_Yusuf.txt", "r") as f:
    text = f.read()

tokens = sent_tokenize(text)
file2_docs = []
for line in tokens:
    file2_docs.append(line)

for line in file2_docs:
    query_doc = [word.lower() for word in word_tokenize(line)]
    print(query_doc)

# print(len(file2_docs))
# print(len(tokens))


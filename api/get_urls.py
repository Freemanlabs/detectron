from googlesearch import search
import random


def get_phrases(text, n=10):
    split_text = text.split()
    phrases = [
        " ".join(split_text[i : i + n])
        for i in range(0, len(split_text), n)
        if len(split_text[i : i + n]) > 5
    ]
    return phrases


def get_random_phrases(phrases, n):
    return [random.choice(phrases) for _ in range(n)]


def urls(text):
    print("Extracting phrases...")
    phrases = get_phrases(text)
    random_phrases = get_random_phrases(phrases, 6)

    urls = list()
    print("Running google search on random phrases...")
    for query in random_phrases:
        urls.extend(search(query=query, num=5, stop=5))

    return urls

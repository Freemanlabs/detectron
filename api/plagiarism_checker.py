import gensim
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def from_sklearn(search_result, query_doc_file):
    print("Detecting plagiarism...")
    with open(search_result, "r") as f:
        scraped_doc = json.load(f)

    with open(query_doc_file, "r") as f:
        base_document = f.read()

    documents = [doc["text"] for doc in scraped_doc]

    vectorizer = TfidfVectorizer()

    # To make uniformed vectors, both documents need to be combined first.
    documents.insert(0, base_document)
    embeddings = vectorizer.fit_transform(documents)

    cosine_similarities = cosine_similarity(embeddings[0:1], embeddings[1:]).flatten()

    print("cosine:", cosine_similarities)
    print("length cosine", len(cosine_similarities))
    print("len doc", len(documents))

    avg_sims = np.sum(cosine_similarities) / len(cosine_similarities)
    print("avg_sims:", avg_sims)
    new_cosine = [x / sum(cosine_similarities) for x in cosine_similarities]

    avg_sims2 = np.sum(cosine_similarities)
    print("avg_sims2:", avg_sims2)

    highest_score = 0
    highest_score_index = 0
    for i, score in enumerate(cosine_similarities):
        if highest_score < score:
            highest_score = score
            highest_score_index = i

    most_similar_document = documents[highest_score_index]

    # print(
    #     "Most similar document by TF-IDF with the score:",
    #     most_similar_document,
    #     highest_score,
    # )

    # os.remove(search_result)

    return round(float(highest_score) * 100)


def from_gensim(search_result, query_doc_file):
    avg_sims = []

    print("Detecting plagiarism...")
    with open(search_result, "r") as f:
        scraped_doc = json.load(f)

    text_list = [doc["text"] for doc in scraped_doc]

    tokens = sent_tokenize(" ".join(text_list))

    file_docs = [line for line in tokens]

    length_file_docs = len(file_docs)

    documents = [[word.lower() for word in word_tokenize(text)] for text in file_docs]

    dictionary = gensim.corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(document) for document in documents]
    tf_idf = gensim.models.TfidfModel(corpus)
    similarity = gensim.similarities.Similarity(
        "workdir/", tf_idf[corpus], num_features=len(dictionary)
    )

    with open(query_doc_file, "r") as f:
        tokens = sent_tokenize(f.read())
        file2_docs = [line for line in tokens]

    for line in file2_docs:
        query_doc = [word.lower() for word in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)
        query_doc_tf_idf = tf_idf[query_doc_bow]
        # print("Comparing Result:", similarity[query_doc_tf_idf])
        sum_of_sims = np.sum(similarity[query_doc_tf_idf], dtype=np.float32)
        avg = sum_of_sims / length_file_docs
        # print(f"avg: {sum_of_sims / length_file_docs}")
        avg_sims.append(avg)

    total_avg = np.sum(avg_sims, dtype=np.float)
    # print(total_avg)
    percentage_of_similarity = round(float(total_avg) * 100)
    if percentage_of_similarity >= 100:
        percentage_of_similarity = 100

    # os.remove(search_result)

    return percentage_of_similarity


def check_plagiarism(search_result, query_doc_file):
    # sk = from_sklearn(search_result, query_doc_file)
    # print("sklearn:", sk)

    # gens = from_gensim(search_result, query_doc_file)
    # print("gensim:", gens)

    return from_gensim(search_result, query_doc_file)

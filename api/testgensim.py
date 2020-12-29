from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
import numpy as np

main_doc = "The SPIDER_MIDDLEWARES setting is merged with the SPIDER_MIDDLEWARES_BASE setting defined in Scrapy (and not meant to be overridden) and then sorted by order to get the final sorted list of enabled middlewares: the first middleware is the one closer to the engine and the last is the one closer to the spider. In other words, the process_spider_input() method of each middleware will be invoked in increasing middleware order (100, 200, 300, …), and the process_spider_output() method of each middleware will be invoked in decreasing order.\
\
To decide which order to assign to your middleware see the SPIDER_MIDDLEWARES_BASE setting and pick a value according to where you want to insert the middleware. The order does matter because each middleware performs a different action and your middleware could depend on some previous (or subsequent) middleware being applied.\
React is a library, not a framework. Unlike client-side MVC frameworks, like Backbone, Ember, and AngularJS, it makes no assumptions about your tech stack so you can easily integrate it into a new or legacy code base. It’s often used to manage specific areas of an application’s UI, rather than the entire UI.\
\
React’s only concern is with the user interface (the ‘V’ in MVC) \
I always setup a virtual environment. A virtual environment manages dependencies of the project and remain particular for the single project. It does not affect the system packages. The following commands are for Unix-based systems. They create virtual environment and activates it. \
Python versions <3.4 do not have virtual environments inbuilt. You need to install a third-party package virtualenv and run virtualenv venv \
This feature was added in Flask 0.6 but can be achieved in older versions as well by subclassing the request object. For more information on that consult the Werkzeug documentation on file handling. \
A while ago many developers had the idea to read the incoming file in small chunks and store the upload progress in the database to be able to poll the progress with JavaScript from the client. Long story short: the client asks the server every 5 seconds how much it has transmitted already. Do you realize the irony? The client is asking for something it should already know."

query = "The SPIDER_MIDDLEWARES setting is merged with the SPIDER_MIDDLEWARES_BASE setting defined in Scrapy (and not meant to be overridden) and then sorted by order to get the final sorted list of enabled middleware. \
\
So for example, if at mid-semester or much later on you find out that your proposed scope can’t be achieved by the end of the semester. \
\
React is a library, not a framework. Unlike client-side MVC frameworks, like Backbone, Ember, and AngularJS, it makes no assumptions \
\
I always setup a virtual environment. A virtual environment manages dependencies of the project and remain particular for the single project. It does not affect the system packages. \
\
This feature was added in Flask 0.6 but can be achieved in older versions as well by subclassing the request object. For more information on that consult the Werkzeug documentation on file handling."

split_text = main_doc.split()
phrases = [
    " ".join(split_text[i : i + 10])
    for i in range(0, len(split_text), 10)
    if len(split_text[i : i + 10]) > 5
]
print(phrases)
print(len(phrases))
print(len(split_text))
# tokens = sent_tokenize(main_doc)
# file_docs = []
# for line in tokens:
#     file_docs.append(line)

# gen_docs = [[w.lower() for w in word_tokenize(text)] for text in file_docs]
# dictionary = gensim.corpora.Dictionary(gen_docs)
# # print(dictionary.token2id)

# corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# tf_idf = gensim.models.TfidfModel(corpus)
# # for doc in tf_idf[corpus]:
# #     print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
# sims = gensim.similarities.Similarity(
#     "workdir/", tf_idf[corpus], num_features=len(dictionary)
# )

# tokens2 = sent_tokenize(query)
# file2_docs = []
# for line in tokens2:
#     file2_docs.append(line)

# avg_sims = []
# plagirised_text = []
# for line in file2_docs:
#     query_doc = [w.lower() for w in word_tokenize(line)]
#     query_doc_bow = dictionary.doc2bow(query_doc)
#     query_doc_tf_idf = tf_idf[query_doc_bow]
#     # print(document_number, document_similarity)
#     print("Comparing Result:", sims[query_doc_tf_idf])
#     sum_of_sims = np.sum(sims[query_doc_tf_idf], dtype=np.float32)
#     print(sum_of_sims)
#     avg = sum_of_sims / len(file_docs)
#     print(f"avg: {avg}")
#     avg_sims.append(avg)

#     if np.max(sims[query_doc_tf_idf]) > 0.5:
#         plagirised_text.append(line)

# total_avg = np.sum(avg_sims, dtype=np.float)
# percentage_of_similarity = round(float(total_avg) * 100)
# print(percentage_of_similarity)

# for p in plagirised_text:
#     print(p + "\n")
# print(len(plagirised_text))


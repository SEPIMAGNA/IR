import math
import os
import re


def tf(term, doc):
    # Count the times term occurred in document and return It.
    return doc.split().count(term) / len(doc.split())


def df(term, corpus):
    # For each document in corpus if term was in the document add 1 to frequency ( and then return the sum ).
    return sum(1 for doc in corpus if term in doc.split())


def idf(term, corpus):
    # Count the times term occurred in document and return It.
    return math.log(len(corpus) / 1 + df(term, corpus))


def tf_idf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)


def main():
    print('> Please enter your term and then insert documents path of Corpus:\n')
    term = input('> Term: \n>> ')
    # List of Corpus documents path
    path = input('\n> Path of documents folder:\n\n>> ')
    os.chdir(path)
    docs = os.listdir(path)

    # Representing the Corpus.
    corpus = []
    for doc in docs:
        # Using regex to remove unwanted chars
        corpus.append(re.sub(r'([^\s\w]|_)+', "", open(path + '/' + doc, 'r').read().lower()))
    scores = {}

    for doc in corpus:
        # Calculating the score of each document in corpus with respect to term
        scores[docs[corpus.index(doc)]] = round(tf_idf(term, corpus[corpus.index(doc)], corpus), 5)

    for item in scores.keys():
        print('>>> ' + str(item) + ': tf-idf = ' + str(scores[item]) + '\n')


if __name__ == "__main__":
    main()

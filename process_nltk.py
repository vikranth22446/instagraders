from itertools import product

import nltk
from nltk import PunktSentenceTokenizer, pos_tag
from nltk.corpus import stopwords, state_union, wordnet, wordnet_ic
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stoplist = set(stopwords.words("english"))

import spacy

nlp = spacy.load("en")


def run_nltk(paragraph, answers):
    """

    :param paragraph: a paragraph of text
    :param answers: a list of answers with text
    :return:
    """

    def get_nouns(x):
        return x[1] == "NOUN"

    ps = PorterStemmer()
    key = []
    for i in answers:
        print(word_tokenize(i))
        tokenized_answer = pos_tag((word_tokenize(i)), tagset="universal")
        print(tokenized_answer)
        arr = [i[0].lower() for i in tokenized_answer if i[1] == "NOUN" or i[1] == "ADJ"]

        if arr:
            key.append(arr)
    print(key)
    tokenized_paragraph = word_tokenize(paragraph.lower())
    import requests

    r = requests.get(
        "https://api.textgears.com/check.php?text={}!&key=72ZxTaaeG6S4oUD9".format(
            paragraph))

    json_grammar = r.json()
    score = json_grammar["score"]

    ap_grade = 0
    for answer in key:
        initial_index = 0
        correct = False
        while initial_index != len(tokenized_paragraph) - 1:
            tokenized_answers_traversed = 0

            initial = (False, 0)
            for i in range(initial_index, len(tokenized_paragraph)):
                if tokenized_answers_traversed == len(answer):
                    correct = True
                    break

                tokens = nlp(tokenized_paragraph[i])
                tokens2 = nlp(answer[tokenized_answers_traversed])
                simarality = tokens.similarity(tokens2)
                if simarality > 0.8:
                    print("Similiar: {}, {}".format(tokenized_paragraph[i], answer[tokenized_answers_traversed]))
                    if not initial[0]:
                        initial = (True, i)
                    tokenized_answers_traversed += 1
                else:
                    if initial[0] and (i - initial[1]) > 20:
                        initial_index = i
                        break
                if i == len(tokenized_paragraph) - 1:
                    initial_index = i
                    correct = False
                    break
            if tokenized_answers_traversed == len(answer):
                correct = True
                break

        if correct:
            ap_grade += 1
    return ap_grade, score, len(answers)


if __name__ == '__main__':
    ps = PorterStemmer()

    print(pos_tag((word_tokenize("John's")), tagset='universal'))
    x, y, size = run_nltk(
        "This is an  pragraph with concepts of water retention and cohesion. Water is universal. Water is the most basic molecule known to man. ",
        ["Water is universal", "Cohesion", "Gravity is green"])
    print(x, y, x / size)

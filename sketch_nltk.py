from itertools import product

import nltk
from nltk import PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union, wordnet, wordnet_ic
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

example_sentence = "This is an example off stopping word filteration"
stoplist = set(stopwords.words("english"))
filtered_words = [ps.stem(w) for w in word_tokenize(example_sentence) if w not in stoplist]
print(filtered_words)


def get_pps():
    custom_sent_tokenizer = PunktSentenceTokenizer(sample_token)

    sample_token = state_union.raw("2005-GWBush.txt")
    real = state_union.raw("2005-GWBush.txt")

    tokenized = custom_sent_tokenizer.tokenize(real)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEntity = nltk.ne_chunk(tagged, binary=True)
            namedEntity.draw()
            print(tagged)
    except Exception:
        print("e")


def get_syns(word):
    synomys = []
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synomys.append(l.name)
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    print(synomys)
    print(antonyms)
    return synomys


# u = set.intersection(set("love"), set(get_syns("romance")))
# print(u)
#
# cars = wordnet.synsets("car", "n")
# bikes = wordnet.synsets("bike", "n")
#
# brown_ic = wordnet_ic.ic("ic-brown.dat")
# semcor_ic = wordnet_ic.ic("ic-semcor.dat")
#
# for car in cars:
#     for bike in bikes:
#         jcs_brown = car.jcn_similarity(bike, brown_ic)
#         jcs_semcor = car.jcn_similarity(bike, semcor_ic)
#         print("JCS(%s, %s) = (%.4f, %.4f)" %
#               (str(car), str(bike), jcs_brown, jcs_semcor))
# get_syns()
#
# actual = wordnet.synsets('worse')[0]
# predicted = wordnet.synsets('better')[0]
# similarity = actual.jcn_similarity(actual, predicted)
# print(similarity)
# #
# from itertools import product
#
love = wordnet.synsets('dog')[0].definition()
hatred = wordnet.synsets('cheese')[0].definition()
import spacy

import spacy

nlp = spacy.load("en")
tokens = nlp("love")
tokens2 = nlp("romance")
print(tokens.similarity(tokens2))
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.similarity(token2))
# print(love)
# print(hatred)
# nlp = spacy.load('en')
# doc1 = nlp("dog")
# doc2 = nlp("cheese")
# print(doc1.similarity(doc2))

# allsyns1 = set(ss for word in ["hatred"] for ss in wordnet.synsets(word))
# allsyns2 = set(ss for word in ["sticks"] for ss in wordnet.synsets(word))
# best = max((wordnet.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in
#         product(allsyns1, allsyns2))
# print(best)
# (0.9411764705882353, Synset('command.v.02'), Synset('order.v.01'))
# allsyns1 = set(ss for ss in wordnet.synsets("good"))
# allsyns2 = set(ss for ss in wordnet.synsets("bad"))
# best = max((wordnet.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in
#            product(allsyns1, allsyns2))
# print(best)

# (0.9411764705882353, Synset('command.v.02'), Synset('order.v.01'))
# from nltk.corpus import wordnet as wn
# from nltk.corpus import wordnet_ic
#
# cars = wordnet.synset("romance.n.01")
# bikes = wordnet.synset("love.n.01")
#
# brown_ic = wordnet_ic.ic("ic-brown.dat")
# semcor_ic = wordnet_ic.ic("ic-semcor.dat")
# jcs_brown = cars.jcn_similarity(bikes, brown_ic)
# jcs_semcor = cars.jcn_similarity(bikes, semcor_ic)
# print("JCS(%s, %s) = (%.4f, %.4f)" %
#       (str(cars), str(bikes), jcs_brown, jcs_semcor))

# w1 = wordnet.synsets("greater", pos="a")[0]
# w2 = wordnet.synsets("worse", pos="a")[0]
# print(w1, w2)
# print(w1.wup_similarity(w2))
# import nltk, string
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# nltk.download('punkt')  # if necessary...
#
# stemmer = nltk.stem.porter.PorterStemmer()
# remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
#
#
# def stem_tokens(tokens):
#     return [stemmer.stem(item) for item in tokens]
#
#
# '''remove punctuation, lowercase, stem'''
#
#
# def normalize(text):
#     return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
#
#
# vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
#
#
# def cosine_sim(text1, text2):
#     tfidf = vectorizer.fit_transform([text1, text2])
#     return ((tfidf * tfidf.T).A)[0, 1]
#
#
# print(cosine_sim(love, hatred))

import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from lxml import etree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer


xml_path = "news.xml"
lemmatizer = WordNetLemmatizer()
vectorizer = TfidfVectorizer()

tree = etree.parse(xml_path)
root = tree.getroot()
news_collection = root[0]
headlines = []
nouns_from_all_texts = []
all_words = []
for el in news_collection:
    #print(f"{el[0].text}:")
    headlines.append(el[0].text + ":")
    lst = word_tokenize(el[1].text.lower())
    lemmatized = [lemmatizer.lemmatize(token) for token in lst]
    tokens_without_sw = [word for word in lemmatized if not word in stopwords.words('english') and word not in string.punctuation]
    common = Counter(tokens_without_sw)
    out = sorted(common, key=lambda x: (common[x], x), reverse=True)
    nouns = []
    for w in out:
        temp = [w]
        #if len(nouns) >= 5:
        #    break
        if nltk.pos_tag(temp)[0][1] == "NN":
            nouns.append(w)

    all_words.append(el[1].text.lower())
    nouns_from_all_texts.append(nouns)

tfidf = vectorizer.fit_transform(all_words)
terms = vectorizer.get_feature_names()

for i in range(len(headlines)):
    print(headlines[i])
    res = []
    m = tfidf[i].tocoo()
    tuples = zip(m.row, m.col, m.data)

    sorted_tfidf = sorted(tuples, key=lambda x:x[2], reverse=True)

    for t in sorted_tfidf:
        if len(res) >= 5:
            break
        if terms[t[1]] in nouns_from_all_texts[i]:
            res.append(terms[t[1]])

    print(" ".join(res))
    print()
import requests as rq
import nltk
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import wordpunct_tokenize,pos_tag,ne_chunk

#response=rq.get("https://en.wikipedia.org/wiki/Google")
#cont=BeautifulSoup(response.content,"html.parser")
#print(cont.text)
#Tokenization
print("----Tokenization----------")
file_content = open("sample.txt").read()
wtokens = nltk.word_tokenize(file_content)
stokens = nltk.word_tokenize(file_content)
print(wtokens)
for s in stokens:
   print(s)
for w in wtokens:
   print(w)

#POS Tagging
print("-------POS---------")
print(nltk.pos_tag(wtokens))

#Stemming
print("-------Stemming---------")
pStemmer = PorterStemmer()
print(pStemmer)
for w in wtokens:
   print(w," : ", pStemmer.stem(w))

#Lemmatization
print("-------Lemmatization---------")
lemmetizer = WordNetLemmatizer()
print(lemmetizer)
for w in wtokens:
    print(w, " : ", lemmetizer.lemmatize(w))

#Trigram
print("-------Trigram--------")
new_trigrams = []
c = 0
while c < len(wtokens) - 2:
    new_trigrams.append((wtokens[c], wtokens[c+1], wtokens[c+2]))
    c += 2
for trigram in new_trigrams:
    print(trigram)

#Named Entity Recognition
print("-------NER---------")
print(ne_chunk(pos_tag(wordpunct_tokenize(file_content))))


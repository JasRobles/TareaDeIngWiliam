import nltk
from gtts import gTTS
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
from googletrans import Translator

text = "On February 15, 2023, 39 people were killed in a bus crash in Panama. It was headed to a migrant reception center in the town of Gualaca when it crashed in Gualaca District, Chiriquí Province, in the west of the country about 67.8 km (42.1 mi) from the Costa Rican border."

#nltk.download()
#Tokenizacion
sentence_list = nltk.sent_tokenize(text)

#En esta parte encuentra la frecuencia de las palabras
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1

#Calcula las frases que mas se repiten
sentences_socores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 50:
                if sent not in sentences_socores.keys():
                    sentences_socores[sent] = word_frequencies[word]
                else:
                    sentences_socores[sent] += word_frequencies[word]

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#Resumen con las mejores frases
import heapq
summary_sentences = heapq.nlargest(7, sentences_socores, key=sentences_socores.get)
summary = ' '.join(summary_sentences)
googleTrad = Translator()

traducc=googleTrad.translate(summary, dest='spanish')
print(traducc.text)
Sound = gTTS(text=traducc.text,lang='es',slow=False)
Sound.save('Jasmin.mp3')
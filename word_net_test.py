import sys
import random
import nltk
from nltk.corpus import wordnet as wn

input_sentence = sys.argv[1]

tokenized = nltk.word_tokenize(input_sentence)
tagged = nltk.pos_tag(tokenized)


def find_syn(word):
    synsets = wn.synsets(word)
    synsets = [syn for syn in synsets if syn.pos() == 'r']
    syn = random.choice(synsets)
    lemma = random.choice(syn.lemmas())
    return lemma.name()

output = []
for word in tagged:
    if word[1] == 'RB':
        new_word = word[0]
        while new_word == word[0]:
            new_word = find_syn(word[0])
        output.append(new_word.replace('_', ' '))
    else:
        output.append(word[0])

print ' '.join(output)

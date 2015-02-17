import sys
import random
import nltk
from nltk.corpus import wordnet as wn

input_sentence = sys.argv[1]

tokenized = nltk.word_tokenize(input_sentence)
tagged = nltk.pos_tag(tokenized)


def find_syn(word_tuple):
    word, pos = word_tuple
    pos = word_types_to_sub[pos]
    synsets = wn.synsets(word)
    synsets = [syn for syn in synsets if syn.pos() == pos]
    if not synsets:
        return None
    syn = random.choice(synsets)
    lemma = random.choice(syn.lemmas())
    return lemma.name()

output = []
word_types_to_sub = {
    'RB' : 'r',
    'VBP': 'v',
}

for word in tagged:
    if word[1] in word_types_to_sub.keys():
        new_word = word[0]
        while new_word == word[0]:
            new_word = find_syn(word)
            if new_word == None: #we couldn't find replacement
                new_word = word[0]
                break
        output.append(new_word.replace('_', ' '))
    else:
        output.append(word[0])

print ' '.join(output)

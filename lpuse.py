from nltk.corpus import wordnet as wn
import re


def clean_words(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z]+", sentence)


def synonyms_of(word):
    words = {word}

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            words.add(lemma.name().lower().replace("_", " "))

    return words


def expanded_sentence_words(sentence):
    result = set()

    for word in clean_words(sentence):
        result.update(synonyms_of(word))

    return result


def sentence_meaning_score(sentence1, sentence2):
    words1 = expanded_sentence_words(sentence1)
    words2 = expanded_sentence_words(sentence2)

    common = words1.intersection(words2)
    total = words1.union(words2)

    if not total:
        return 0, common

    score = len(common) / len(total)
    return score, common


s1 = "I want food"
s2 = "I want films"
for i in range(5):
    inputsentence = input("\nEnter a sentence\n").lower().strip()
    score1, c1 = sentence_meaning_score(s1, inputsentence)
    score2, c1 = sentence_meaning_score(s2, inputsentence)
    print(score1, score2)
    if score1 < score2:
        print("tkt le lo")
    else:
        print("Maggi le lo")

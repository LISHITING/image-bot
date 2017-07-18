import pycrfsuite
from nltk.tag.perceptron import PerceptronTagger
from nltk import word_tokenize
import os

tagger = PerceptronTagger()


def posTagger(sentence):
    tokenizedSentence = word_tokenize(sentence)
    posTaggedSentence = tagger.tag(tokenizedSentence)
    return posTaggedSentence


def posTagAndLabel(sentence):
    taggedSentence = posTagger(sentence)
    taggedSentenceJson = []
    for token, postag in taggedSentence:
        taggedSentenceJson.append([token, postag, "O"])
    return taggedSentenceJson

    return success


def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        'postag=' + postag,
        'postag[:2]=' + postag[:2],
    ]
    if i > 0:
        word1 = sent[i - 1][0]
        postag1 = sent[i - 1][1]
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            '-1:postag=' + postag1,
            '-1:postag[:2]=' + postag1[:2],
        ])
    else:
        features.append('BOS')

    if i < len(sent) - 1:
        word1 = sent[i + 1][0]
        postag1 = sent[i + 1][1]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:postag=' + postag1,
            '+1:postag[:2]=' + postag1[:2],
        ])
    else:
        features.append('EOS')

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def get_parameter(sentence, name):
    name = str(name) + '.crfsuite'
    sentence = posTagAndLabel(sentence)
    tagger = pycrfsuite.Tagger()

    result = {}

    currentpath = os.path.dirname(os.path.realpath(__file__))
    crfmodel = os.path.join(currentpath, name)
    tagger.open(crfmodel)

    taglist = tagger.tag(sent2features(sentence))
    for i in range(len(taglist)):
        if taglist[i] != 'O':
            result[taglist[i]] = sentence[i][0]
            return result
    return {}

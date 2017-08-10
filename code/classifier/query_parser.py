from core.crf import get_parameter
from core.svm import get_intention
from nltk.corpus import wordnet as wn


def parse_query(query):
    intention = get_intention([query])
    parameter = get_parameter(query, intention).get('target')
    print('intention1:', intention, 'parameter:', parameter)
    if parameter is not None:
        parameter = wn.morphy(parameter)
    return intention, parameter

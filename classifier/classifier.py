from svm.svm import get_intention
from crf.crf import get_parameter


def get_result(query):
    intention = get_intention([query])
    parameter = get_parameter(query, intention)
    result = dict(intention=intention, parameter=parameter)
    return result


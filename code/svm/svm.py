import pickle
import os
def get_intention(query):
    """
    use SVM classifier to predict
    """
    currentpath = os.path.dirname(os.path.realpath(__file__))
    vectorizer = pickle.load(open(os.path.join(currentpath, '../model/vectorizer.model'), "rb"))
    clf = pickle.load(open(os.path.join(currentpath, '../model/svm.model'), "rb"))
    x_vec = vectorizer.transform(query)
    prediction = clf.predict(x_vec)[0]
    return prediction
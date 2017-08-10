import pickle
import config


def get_intention(query):
    vectorizer = pickle.load(open(config.PATH_TO_VECTORIZER, "rb"))
    svm_classifier = pickle.load(open(config.PATH_TO_SVM_MODEL, "rb"))
    x_vec = vectorizer.transform(query)
    prediction = svm_classifier.predict(x_vec)[0]
    return prediction

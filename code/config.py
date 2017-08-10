import os

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PATH_TO_IMAGE = (os.path.join(CURRENT_PATH, './temp/imagefile'))
PATH_TO_CKPT = (os.path.join(CURRENT_PATH, './model/frozen_inference_graph.pb'))
PATH_TO_LABELS = (os.path.join(CURRENT_PATH, './model/mscoco_label_map.pbtxt'))
PATH_TO_RESULT = (os.path.join(CURRENT_PATH, './temp/filted_result'))
PATH_TO_CRF_MODEL = (os.path.join(CURRENT_PATH, './model'))
PATH_TO_SVM_MODEL = (os.path.join(CURRENT_PATH, './model/svm.model'))
PATH_TO_VECTORIZER = (os.path.join(CURRENT_PATH, './model/vectorizer.model'))
NUM_CLASSES = 100

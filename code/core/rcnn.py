import pickle
import numpy as np
import tensorflow as tf
from core.utils import label_map_util
import config


def save_image(img):
    pickle.dump(img, open(config.PATH_TO_IMAGE, "wb"), True)
    boxes, scores, classes, num_detections = detect()
    filtered_result = result_filter(classes, scores)
    pickle.dump(filtered_result, open(config.PATH_TO_RESULT, "wb"), True)
    return True


def detect():
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(config.PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_np = pickle.load(open(config.PATH_TO_IMAGE, "rb"))
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            (boxes, scores, classes, num_detections) = sess.run([boxes, scores,
                                                                 classes, num_detections],
                                                                feed_dict={image_tensor: image_np_expanded})
    return boxes, scores, classes, num_detections


def result_filter(classes, scores, threshold=0.3):
    tmp = list(zip(classes[0], scores[0]))
    filtered_result = [i for i in tmp if i[1] > threshold]
    return filtered_result


def find_obj(parameter):
    try:
        filtered_result = pickle.load(open(config.PATH_TO_RESULT, "rb"))
    except:
        filtered_result = []
    tmp = [int(c) for c, s in filtered_result]
    parameter = parameter2id(parameter)
    if parameter:
        return parameter in tmp
    else:
        return False


def count_obj(parameter):
    try:
        filtered_result = pickle.load(open(config.PATH_TO_RESULT, "rb"))
    except:
        filtered_result = []
    tmp = [int(c) for c, s in filtered_result]
    parameter = parameter2id(parameter)
    return tmp.count(parameter)


def list_obj():
    try:
        filtered_result = pickle.load(open(config.PATH_TO_RESULT, "rb"))
    except:
        filtered_result = []
    tmp = [int(c) for c, s in filtered_result]
    tmp_set = list(set(tmp))
    output = []
    category_index = load_index()
    for key, value in category_index.items():
        for i in tmp_set:
            if i == int(value.get('id')):
                output.append(value.get('name'))
    return output


def parameter2id(parameter):
    category_index = load_index()
    for key, value in category_index.items():
        if parameter == value.get('name'):
            return int(value.get('id'))
    return False


def load_index():
    label_map = label_map_util.load_labelmap(config.PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=config.NUM_CLASSES,
                                                                use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    return category_index

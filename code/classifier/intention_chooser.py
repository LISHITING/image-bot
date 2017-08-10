from core import rcnn


def switch_intention(intention=None, parameter=None):
    if intention == 'verify':
        if parameter is not None:
            if verify(parameter):
                return 'Yes, I can see ' + parameter + ' in the picture!'
            else:
                return 'No, I can not find any ' + parameter + ' in the picture. '
        else:
            return 'Oh, I can not understand that thing you want to find'
    elif intention == 'getnum':
        if parameter is not None:
            if verify(parameter):
                count = str(get_num(parameter))
                return 'I can find ' + count + '\n' + add_s(parameter, count) + ' in the picture'
            else:
                return 'No, I can not find any ' + parameter + ' in the picture:( '
        else:
            obj_list = get_obj()
            obj_num_list = [get_num(obj) for obj in obj_list]
            answer = ','.join(list(map(lambda a, b: str(a) + " " + add_s(x=b, num=a), obj_num_list, obj_list)))
            return 'I can find ' + answer + ' in the picture.'
    elif intention == 'getobj':
        obj_list = get_obj()
        if len(obj_list) > 0:
            answer = ','.join(obj_list)
            return 'I can find ' + answer + ' in the picture'
        else:
            return 'I can not find anything, make sure you have uploaded a picture'
    elif intention == 'drawbox':
        return draw_box()
    elif intention == 'welcome':
        return welcome()
    else:
        return 'NOTHING'


def add_s(x, num):
    if int(num) > 1:
        return x + 's'
    else:
        return x


def verify(parameter):
    return rcnn.find_obj(parameter)


def get_obj():
    return rcnn.list_obj()


def get_num(parameter):
    return rcnn.count_obj(parameter)


def welcome():
    return 'Hello, you can feed me an image'


def draw_box():
    return 'drow box is called'

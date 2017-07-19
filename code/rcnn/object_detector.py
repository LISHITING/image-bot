from rcnn import core


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
                return 'I can find ' + count + '\n' + parameter + ' in the picture'
            else:
                return 'No, I can not find ' + parameter + ' in the picture:( '
        else:
            return 'Sorry, I think I did not understand that thing'
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


def verify(parameter):
    return core.find_obj(parameter)


def get_obj():
    return core.list_obj()


def get_num(parameter):
    return core.count_obj(parameter)


def welcome():
    return 'Hello, you can feed me an image'


def draw_box():
    return 'drow box is called'

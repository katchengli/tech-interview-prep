class OkEros(object):
    def __init__(self):
        pass


    def getRectangleIntersection(rect1, rect2):

        if ((rect1['left_x'] + rect1['width']) <= rect2['left_x'] or
            (rect2['left_x'] + rect2['width']) <= rect1['left_x'] or
            (rect1['bottom_y'] + rect1['height']) <= rect2['bottom_y'] or
            (rect2['bottom_y'] + rect2['height']) <= rect1['bottom_y']):
            try:
                raise Exception('No Rectangular Intersection')
            except Exception as exc:
                print(str(type(exc)) + ': ' + str(exc.args))
                return {'left_x':None, 'bottom_y':None, 'width':None, 'height':None}

        left_x = max(rect1['left_x'], rect2['left_x'])
        bottom_y = max(rect1['bottom_y'], rect2['bottom_y'])

        width = min(rect1['left_x']+rect1['width'], rect2['left_x']+rect2['width']) - left_x
        height = min(rect1['bottom_y']+rect1['height'], rect2['bottom_y']+rect2['height']) - bottom_y

        return {'left_x':left_x, 'bottom_y':bottom_y, 'width':width, 'height':height}

rectangle1 = {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
rectangle2 = {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
print(OkEros.getRectangleIntersection(rectangle1, rectangle2))
#should print {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
rectangle1 = {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
rectangle2 = {'left_x':11, 'bottom_y':5, 'width':10, 'height':4}
print(OkEros.getRectangleIntersection(rectangle1, rectangle2))
#should raise Exception No Rectangular Intersection
rectangle1 = {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
rectangle2 = {'left_x':1, 'bottom_y':9, 'width':10, 'height':4}
print(OkEros.getRectangleIntersection(rectangle1, rectangle2))
#should raise Exception No Rectangular Intersection
rectangle1 = {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
rectangle2 = {'left_x':2, 'bottom_y':6, 'width':8, 'height':2}
print(OkEros.getRectangleIntersection(rectangle1, rectangle2))
#should print {'left_x':2, 'bottom_y':6, 'width':8, 'height':2}

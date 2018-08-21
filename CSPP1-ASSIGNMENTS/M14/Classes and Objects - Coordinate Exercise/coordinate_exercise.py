"""Exercise: coordinate"""
class Coordinate(object):
    '''This is a class and its name is Coordinate'''
    def __init__(self, x_input, y_input):
        self.x_input = x_input
        self.y_input = y_input
    def getx_input(self):
        '''Getter method for a Coordinate object's x coordinate.'''
        return self.x_input
    def gety_input(self):
        '''Getter method for a Coordinate object's y coordinate'''
        return self.y_input
    def __str__(self):
        '''Used while we print an object'''
        return '<' + str(self.getx_input()) + ',' + str(self.gety_input()) + '>'
    def __eq__(self, other):
        '''This is used when the two co-ordinates are equal'''
        assert type(other) == type(self)
        if self.getx_input() == other.getx_input():
            if self.gety_input() == other.gety_input():
                return True
        return False
    def __repr__(self):
        '''Represenation of a co-ordinate'''
        return 'Coordinate(' + str(self.getx_input()) + ',' + str(self.gety_input()) + ')'
#X_NEW = Coordinate(10, 10)
#X1_NEW = Coordinate(10, 10)
#print(X_NEW.__eq__(X1_NEW))
#print(X_NEW.__repr__())
def main():
    '''Writing inside this function'''
    data = input()
    data = data.split(' ')
    data = list(map(int, data))
    print(Coordinate(data[0], data[1]) == Coordinate(data[2], data[3]))
    print(Coordinate(data[4], data[5]).__repr__())
if __name__ == "__main__":
    main()

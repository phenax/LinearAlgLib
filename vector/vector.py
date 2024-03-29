

class Vector(object):
    """
        Vector data structure
    
        [description]
    """

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __getitem__(self, index):
        return self.coordinates[index]

    # Adds vector v with itself and returns a vector that is the sum of both 
    def plus(self, v):
        new = [] 
        n = len(self.coordinates)
        for i in range(n):
            new.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new) 

    # Subtracts vector v from vector self and returns the vector that is the difference of both
    def minus(self, v):
        new = [] 
        n = len(self.coordinates)
        for i in range(n):
            new.append(self.coordinates[i] - v.coordinates[i])
        return Vector(new)

    def sc_mult(self, c):
        new = []
        n = len(self.coordinates)
        for i in range(n):
            new.append(self.coordinates[i] * c) 
        return Vector(new)

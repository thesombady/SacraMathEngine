
from .Vector import vec3d, vec4d
from .Matrix import matrix3d

#from SacraMathEngine import *


class Triangle:
    def __init__(self, vec1, vec2, vec3, reminder = 1):
        """
        if not isinstance((vec1, vec2, vec3), vec3d):
            raise TypeError("Wrong format in Triangle")
        """
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        self.reminder = reminder
        self.set = [self.vec1, self.vec2, self.vec3]
        self.set2 = [self.vec1.set2, self.vec2.set2, self.vec3.set2]


    def __str__(self):
        """Print statement for Triangle-object"""
        return f'[{self.vec1}, {self.vec2}, {self.vec3}]'

    def __repr__(self):
        """Print statement for Triangle-object"""
        return f'[{self.vec1}, {self.vec2}, {self.vec3}]'

    def __add__(self, vector):
        """Definition of adding vectors in a set"""
        if isinstance(vector, (vec3d, vec4d)):
            return Triangle(self.vec1 + vector, self.vec2 + vector, self.vec3 + vector)
        else:
            pass

    def __sub__(self, vector):
        """Definition of subtracting vectors in a set"""
        if isinstance(vector, (vec3d, vec4d)):
            return Triangle(self.vec1 - vector, self.vec2 - vector, self.vec3 - vector)

    def __len__(self):
        """Return the length of triangle, which is 3 by definition. """
        return len(self.set)

    def __getitem__(self, index):
        """Get the vector defined at index 'index', given the attribute 'index'."""
        return self.set[index]

    def __mul__(self, Scalar):
        """Returns a Triangle-object where each vector i multiplied by the scalar 'Scalar'."""
        if isinstance(Scalar, (float, int)):
            return Triangle(self.vec1 * Scalar, self.vec2 * Scalar, self.vec3 * Scalar)
        else:
            pass

    def __len__(self):
        return len(self.set)

    def __eq__(self, other):
        if self.vec1 == other.vec1 and self.vec2 == other.vec2 and self.vec3 == other.vec3:
            return True
        else:
            return False

    def _ZeroVector(self, triangle):
        """Do not use this method"""
        for i in range(len(triangle)):
            if triangle[i] == vec3d(0,0,0):
                return True
        return False

    def _ZeroVector1(self):
        """Checks if an a vector in the triangle and returns a boolean-value accordingly."""
        for i in range(3):
            if self.set[i] == vec3d(0,0,0):
                return True
        return False


    def normvector(self):
        """Calculates the facing of the Triangle."""
        """
        try:
            Tested = [self.set[i] for i in range(len(self.set)) if self.set[i] != vec3d(0,0,0)]
            if len(Tested) == 3:
                vec1 = self.vec1 - self.vec3
                vec2 = self.vec2 - self.vec3
                return vec1.cross(vec2)
            else:
                return Tested[0].cross(Tested[1])
        except Exception as e:
            raise e
        """
        try:
            if self._ZeroVector1():
                if self.set[0] == vec3d(0,0,0):
                    if self.set[1] == vec3d(0,0,0) and self.set[2] == vec3d(0,0,0):
                        return vec3(1,0,0)
                    elif self.set[1] == vec3d(0,0,0):
                        return self.set[2]
                    elif self.set[2] == vec3d(0,0,0):
                        return self.set[1]
                elif self.set[1] == vec3d(0,0,0):
                    if self.set[0] == vec3d(0,0,0) and self.set[2] == vec3d(0,0,0):
                        return vec3d(1,0,0)
                    elif self.set[0] == vec3d(0,0,0):
                        return self.set[2]
                    elif self.set[2] == vec3d(0,0,0):
                        return self.set[0]
                elif self.set[2] == vec3d(0,0,0):
                    if self.set[0] == vec3d(0,0,0) and self.set[1] == vec3d(0,0,0):
                        return vec3d(1,0,0)
                    elif self.set[0] == vec3d(0,0,0):
                        return self.set[1]
                    elif self.set[1] == vec3d(0,0,0):
                        return self.set[0]
            else:
                vec1 = self.vec1 - self.vec2
                vec2 = self.vec2 - self.vec3
                return vec1.cross(vec2)
        except:
            raise ValueError("[Triangle]:Cant compute the norm value")
#triangle1 = Triangle(vec3d(0,0,0), vec3d(1,0,0), vec3d(0,1,1))
#print(triangle1.normvector())

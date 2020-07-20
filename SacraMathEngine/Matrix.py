from math import tan, pi, radians
from .Vector import vec3d, vec4d
#from SacraMathEngine import *

class matrix3d:
    """ Intalizes a matrix which is in R^3 space; Of which the basic eigen-values can be computed. """
    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        self.matrix = (self.vec1, self.vec2, self.vec3)

    def __str__(self):
        """Default print statement"""
        return f'<({self.vec1[0]}, {self.vec1[1]}, {self.vec1[2]})\n ({self.vec2[0]}, {self.vec2[1]}, {self.vec2[2]})\n ({self.vec3[0]}, {self.vec3[1]}, {self.vec3[2]})>'

    def __add__(self, other):
        """Definition of addition of two matrix3d-objects; Returns a matrix3d-object."""
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __radd__(self, other):
        """Definition of reverse-addition of two matrix3d-objects; Returns a matrix3d-object."""
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __sub__(self, other):
        """Definition of subtraction of two matrix3d-objects; Returns a matrix3d-object."""
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __rsub__(self, other):
        """Definition of reverse-subtraction of two matrix3d-objects; Returns a matrix3d-object."""
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __mul__(self, other):
        """Definition of scalar multiplciation with matrix3d-object, if not the attribute 'other', is a scalar but rather
        a matrix3d it returns m matrix3d-object; If the attribute 'other' is of type vec3d, it returns a vec3d-object as per definition
        of vector matrix multiplication with a 3sqaure matrix and 3-d vector."""
        if isinstance(other, (int, float)):
            return matrix3d(vec1 * other, vec2 * other, vec3 * other)
        elif isinstance(other, vec3d):
            col1 = self.vec1[0] * other[0] + self.vec1[1] * other[1] + self.vec1[2] * other[2]
            col2 = self.vec2[0] * other[0] + self.vec2[1] * other[1] + self.vec2[2] * other[2]
            col3 = self.vec3[0] * other[0] + self.vec3[1] * other[1] + self.vec3[2] * other[2]
            return vec3d(col1, col2, col3)
        elif isinstance(other, matrix3d):
            x1 = self.vec1[0] * other.vec1[0] + self.vec1[1] * other.vec2[0] + self.vec1[2] * other.vec3[0]
            x2 = self.vec1[0] * other.vec1[1] + self.vec1[1] * other.vec2[1] + self.vec1[2] * other.vec3[1]
            x3 = self.vec1[0] * other.vec1[2] + self.vec1[1] * other.vec2[2] + self.vec1[2] * other.vec3[2]
            nvec1 = vec3d(x1, x2, x3)
            y1 = self.vec2[0] * other.vec1[0] + self.vec2[1] * other.vec2[0] + self.vec2[2] * other.vec3[0]
            y2 = self.vec2[0] * other.vec1[1] + self.vec2[1] * other.vec2[1] + self.vec2[2] * other.vec3[1]
            y3 = self.vec2[0] * other.vec1[2] + self.vec2[1] * other.vec2[2] + self.vec2[2] * other.vec3[2]
            nvec2 = vec3d(y1, y2, y3)
            z1 = self.vec3[0] * other.vec1[0] + self.vec3[1] * other.vec2[0] + self.vec3[2] * other.vec3[0]
            z2 = self.vec3[0] * other.vec1[1] + self.vec3[1] * other.vec2[1] + self.vec3[2] * other.vec3[1]
            z3 = self.vec3[0] * other.vec1[2] + self.vec3[1] * other.vec2[2] + self.vec3[2] * other.vec3[2]
            nvec3 = vec3d(z1, z2, z3)
            return matrix3d(nvec1, nvec2, nvec3)
        else:
            pass

    def trace(self):
        """Computes the trace of a given matrix."""
        return self.vec1[0] + self.vec2[1] + self.vec3[2]

class Matrix4d:
    def __init__(self, vec1, vec2, vec3, vec4):
        if isinstance(vec1, vec4d) and isinstance(vec2, vec4d) and isinstance(vec3, vec4d) and isinstance(vec4, vec4d):
            self.vec1 = vec1
            self.vec2 = vec2
            self.vec3 = vec3
            self.vec4 = vec4
        elif vec1 != None or vec2 != None or vec3 != None or vec4d != None:
            #self.InitializeProjection()
            pass
        else:
            self.vec1 = vec1
            self.vec2 = vec2
            self.vec3 = vec3
            self.vec4 = vec4

    def __str__(self):
        """Standard print-statement"""
        # Making row-vectors
        return f'[{self.vec1}\n {self.vec2}\n {self.vec3}\n {self.vec4}]'

    def __add__(self, Other):
        """Stanard addition of two matricies."""
        if isinstance(Other, Matrix4d):
            return Matrix4d(self.vec1 + Other.vec1, self.vec2 + Other.vec2, self.vec3 + Other.vec3, self.vec4 + Other.vec4)
        else:
            pass

    def __mul__(self, Other):
        """Standard multiplication with scalar and a vec4d-object."""
        if isinstance(Other, (int, float)):
            return Matrix4d(self.vec1 * Other, self.vec2 * Other, self.vec3 * Other, self.vec4 * Other)
        elif isinstance(Other, vec4d):
            vec1 = self.vec1[0] * Other.x + self.vec1[1] * Other.y + self.vec1[2] * Other.z + self.vec1[3] * Other.w
            vec2 = self.vec2[0] * Other.x + self.vec2[1] * Other.y + self.vec2[2] * Other.z + self.vec2[3] * Other.w
            vec3 = self.vec3[0] * Other.x + self.vec3[1] * Other.y + self.vec3[2] * Other.z + self.vec3[3] * Other.w
            vec4 = self.vec4[0] * Other.x + self.vec4[1] * Other.y + self.vec4[2] * Other.z + self.vec4[3] * Other.w
            return vec4d(vec1, vec2, vec3, vec4)
        elif isinstance(Other, vec3d):
            Other = vec4d(vector = Other)
            vec1 = self.vec1[0] * Other.x + self.vec1[1] * Other.y + self.vec1[2] * Other.z + self.vec1[3] * Other.w
            vec2 = self.vec2[0] * Other.x + self.vec2[1] * Other.y + self.vec2[2] * Other.z + self.vec2[3] * Other.w
            vec3 = self.vec3[0] * Other.x + self.vec3[1] * Other.y + self.vec3[2] * Other.z + self.vec3[3] * Other.w
            vec4 = self.vec4[0] * Other.x + self.vec4[1] * Other.y + self.vec4[2] * Other.z + self.vec4[3] * Other.w
            return vec4d(vec1, vec2, vec3, vec4)

    def Multiplcation(self, Other):
        """Standard multiplication with scalar and a vec4d-object."""
        if isinstance(Other, (int, float)):
            return Matrix4d(self.vec1 * Other, self.vec2 * Other, self.vec3 * Other, self.vec4 * Other)
        elif isinstance(Other, vec4d):
            vec1 = self.vec1[0] * Other.x + self.vec1[1] * Other.y + self.vec1[2] * Other.z + self.vec1[3] * Other.w
            vec2 = self.vec2[0] * Other.x + self.vec2[1] * Other.y + self.vec2[2] * Other.z + self.vec2[3] * Other.w
            vec3 = self.vec3[0] * Other.x + self.vec3[1] * Other.y + self.vec3[2] * Other.z + self.vec3[3] * Other.w
            vec4 = self.vec4[0] * Other.x + self.vec4[1] * Other.y + self.vec4[2] * Other.z + self.vec4[3] * Other.w
            if vec4 != 0:
                return vec4d(vec1 / vec4, vec2 / vec4, vec3 / vec4, vec4 / vec4) #Can manually change whether to use w or not
            else:
                raise ZeroDivisionError("Cannot divide by Zero\nCannot return to cartesian space")
        elif isinstance(Other, vec3d):
            Other = vec4d(vector = Other)
            vec1 = self.vec1[0] * Other.x + self.vec1[1] * Other.y + self.vec1[2] * Other.z + self.vec1[3] * Other.w
            vec2 = self.vec2[0] * Other.x + self.vec2[1] * Other.y + self.vec2[2] * Other.z + self.vec2[3] * Other.w
            vec3 = self.vec3[0] * Other.x + self.vec3[1] * Other.y + self.vec3[2] * Other.z + self.vec3[3] * Other.w
            vec4 = self.vec4[0] * Other.x + self.vec4[1] * Other.y + self.vec4[2] * Other.z + self.vec4[3] * Other.w
            if vec4 != 0:
                return vec4d(vec1 / vec4, vec2 / vec4, vec3 / vec4, vec4 / vec4) #Can manually change whether to use w or not
            else:
                raise ZeroDivisionError("Cannot divide by Zero\nCannot return to cartesian space")

    def trace(self):
        value = self.vec1[0] + self.vec2[1] + self.vec3[2] + self.vec4[3]
        return value


def ProjectionMatrix(size = (100,100), theta = 30, zfar = 1000, znear = 0.01):
    if size[1] != None:
        ratio = size[0] / size[1]
    else:
        size = 1
    fratio = 1 / tan(radians(theta)) #Convert to radians
    qratio = zfar / (zfar - znear)
    vec1 = vec4d(ratio * fratio, 0, 0, 0)
    vec2 = vec4d(0, fratio, 0, 0)
    vec3 = vec4d(0, 0, qratio , 1)
    vec4 = vec4d(0, 0, qratio - znear * qratio, 0)
    #print(vec4)
    return Matrix4d(vec1, vec2, vec3, vec4)

Prodmatrix = ProjectionMatrix()
#print(Prodmatrix)

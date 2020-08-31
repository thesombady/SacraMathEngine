class vec3d:
    def __init__(self, x, y, z):
        if x == None or y == None or z == None:
            if x == None:
                self.x = 0
            elif y == None:
                self.y = 0
            elif z == None:
                self.z = 0
        else:
            self.x = x
            self.y = y
            self.z = z
        self.set = self.x, self.y, self.z

    def __repr__(self):
        """Default print statement"""
        return f'<({self.x}, {self.y}, {self.z})>'

    def __str__(self):
        """Default print statement"""
        return f'<({self.x}, {self.y}, {self.z})>'

    def __add__(self, other):
        """Defintion of addition of two vectors, returns a vec3d-object."""
        if isinstance(other, vec3d):
            return vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __radd__(self, other):
        """Definition of reverse addition of two vectors, returns a vec3d-object."""
        if isinstance(other, vec3d):
            return vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __sub__(self, other):
        """Definition of subtraction of two vectors, returns a vec3d-object.s"""
        if isinstance(other, vec3d):
            return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __rsub__(self, other):
        """Definition of reverse-subtraction of two vectors, returns a vec3d-object.s"""
        if isinstance(other, vec3d):
            return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __mul__(self, value):
        """Definition of scalar multiplication, only works with float or integers; Returns a vec3d-object.s"""
        if isinstance(value, vec3d):
            pass
        elif isinstance(value, (float, int)):
            return vec3d(self.x * value, self.y * value, self.z * value)
        else:
            pass

    def __rmul__(self, value):
        """Definition of reverse-scalar multiplication, only works with float or integers; Returns a vec3d-object.s"""
        if isinstance(value, vec3d):
            pass
        else:
            return vec3d(self.x * value, self.y * value, self.z * value)

    def __getitem__(self, Index):
        """Get the value of the vec3d-object at index 'Index'."""
        return self.set[Index]

    def __abs__(self):
        return vec3d(abs(self.x), abs(self.y), abs(self.y))

    def __len__(self):
        return len(self.set)

    def __truediv__(self, Scalar):
        if isinstance(Scalar, (float, int)):
            if Scalar != 0:
                return vec3d(self.x / Scalar, self.y / Scalar, self.z / Scalar)
            else:
                raise ValueError("Cannot performe division with zero.")
        elif isinstance(Scalar, vec3d):
            raise TypeError("Cannot performe division with a vector object")
        else:
            pass

    def __contains__(self, value):
        pass

    def dot(self, other):
        """Compute the dot-product of two vectors, returns a float or integer."""
        if isinstance(other, vec3d):
            value = self.x * other.x + self.y * other.y + self.z * other.z
            if value != 0:
                return value
            else:
                return None
        else:
            pass

    def cross(self, other):
        """Compute the cross-product of two vec3d-objects; Returns a vec3d-object."""
        if isinstance(other, vec3d):
            col1 = self.y * other.z - self.z * other.y
            col2 = self.z * other.x - self.x * other.z
            col3 = self.x * other.y - self.y * other.z
            return vec3d(col1, col2, col3)
        else:
            pass

    def norm(self):
        """Calculates the norm of a given vector, returns a scalar of either type integer or float."""
        value = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)
        return value

    def normalize(self):
        """Normalizes a vector with self.norm() function and returns a vec3d-object"""
        return 1 / (self.norm()) * vec3d(self.vec1, self.vec2, self.vec3) # a valid solution is * self

    def line(self, Other, Number):
        """Returns multiple vectors that increase equvilantly"""
        #Not done yet
        if isinstance(Number, int) and isinstance(Other, vec3d):

            Number = Number + 1
            epsilonx = abs(self.x - Other.x) / Number
            epsilony = abs(self.y - Other.y) / Number
            epsilonz = abs(self.z - Other.z) / Number
            Line = []
            for i in range(1, Number):
                 Line.append(vec3d(epsilonx * i, epsilony * i, epsilonz * i))
            return Line

            #while self < = Other

        else:
            raise TypeError("Line method can only take integers as inputs")

    def project2d(self, ratio, theta):

        pass

class vec4d:

    def __init__(self, x = None, y = None, z = None, w = 1, vector = None):
        if vector != None and isinstance(vector, vec3d):
            self.x = vector.x
            self.y = vector.y
            self.z = vector.z
            self.w = 1
        else:
            self.x = x
            self.y = y
            self.z = z
            self.w = w
            self.vector = (self.x, self.y, self.z, self.w)

    def __truediv__(self, value):
        if value != 0:
            x, y, z, w = self.x / value, self.y / value, self.z / value, self.w / value
            return vec4d(x, y, z, w)
        else:
            pass

    def __abs__(self):
        return vec4d(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    def __add__(self, other):
        if isinstance(other, vec4d):
            return vec4d(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __radd__(self, other):
        if isinstance(other, vec4d):
            return vec4d(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        if isinstance(other, vec4d):
            return vec4d(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __rsub__(self, other):
        if isinstance(other, vec4d):
            return vec4d(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __str__(self):
        return f'<({self.x}, {self.y}, {self.z}, {self.w})>'

    def __repr__(self):
        return f'<({self.x}, {self.y}, {self.z}, {self.w})>'

    def __mul__(self, value):
        """Definition of scalar multiplication, only works with float or integers; Returns a vec3d-object.s"""
        if isinstance(value, vec4d):
            pass
        elif isinstance(value, (float, int)):
            return vec4d(self.x * value, self.y * value, self.z * value, self.w * value)
        else:
            pass


    def __getitem__(self, index):
        return self.vector[index]

    def cross(self, other):
        """Compute the cross-product of two vec3d-objects; Returns a vec3d-object."""
        if isinstance(other, vec3d):
            col1 = self.y * other.z - self.z * other.y
            col2 = self.z * other.x - self.x * other.z
            col3 = self.x * other.y - self.y * other.z
            return vec4d(col1, col2, col3, 1)
        else:
            pass

    def dot(self, other):
        if isinstance(other, vec4d):
            value = self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w
            return value
        else:
            pass

    def norm(self):
        """Calculates the norm of a given vector, returns a scalar of either type integer or float."""
        value = (self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2) ** (1/2)
        return value

    def normalize(self):
        normvalue = self.norm()
        if normvalue != 0:
            return 1 / normvalue  * vec4d(self.x, self.y, self.z, self.w)
        else:
            raise ZeroDivisionError("The norm of the vector i zero, and thus it cannot be normalized.\nDivision with zero would occur.")

    def line(self, other, number):
        if isinstance(other, vec3d):
            other = vec4d(vector = other)
        mapx = abs(self.x - other.x) / number
        mapy = abs(self.y - other.y) / number
        mapz = abs(self.z - other.z) / number
        mapw = abs(self.w - other.w) / number
        vectors =[vec4d(self.x + mapx * i, self.y + mapy * i, self.z + mapz * i, self.w + mapw * i) for i in range(number + 1)]
        return vectors

#from .Vector import vec3d
#from .Matrix import matrix3d
#from .Triangle import Triangle
from SacraMathEngine import vec3d, Triangle
import json
import os


class MeshObject:
    def __init__(self, Object, Name, Done = False):
        if isinstance(Object, (list, tuple)) and not Done: #Standard if one wants something quickly, and not importing as a json
            self.Name = Name
            self.IntalizeFromList(Object)
            pass
        elif isinstance(Object, dict) and not Done: #When we read from a dictionary, when importing from json.
            self.Name = Name
            self.IntalizeFromDict(Object)
        else:
            #This part of the code will execute if neither of the above is fulfilled, thus when adding or multiplying.
            self.Mesh = Object
            self.Name = Name


    def IntalizeFromList(self, Object):
        """ When giving a list as starting argument; Intalize such that one returns a current mesh as a list of triangles with vec3d objects."""
        # A "bug", it  cannot load entire cube but only the first Triangle
        self.Mesh = []
        Vectors = []
        for i in range(len(Object)):
            Vectors.append(vec3d(Object[0], Object[1], Object[2]))
        print(Vectors)
        for i in range(0, len(Vectors) - 2, 3):
            self.Mesh.append(Triangle(Vectors[i], Vectors[i + 1], Vectors[i + 2]))

    def __sub__(self, Other):
        """Remove a triangle from a mesh, if the triangle exits."""
        if isinstance(Other, Triangle):
            if Other in self.Mesh:
                NewMesh = self.Mesh.remove(Other)
                return MeshObject(NewMesh, self.Name, Done = True)
            else:
                return KeyError("Can only remove a Triangle-Object.")

    def IntalizeFromDict(self, Object):
        pass

    def __str__(self):
        return f'{self.Mesh}'

    def __repr__(self):
        return f'{(self.Mesh)}'

    def SaveToJson(self, Path = os.getcwd()):
        Mesh = []
        print(self.Mesh)

    def __add__(self, Other):
        """Adder function that adds differently depending on which type of input. """
        if isinstance(Other, Triangle):
            NewMesh = self.Mesh + [Other]
            return MeshObject(NewMesh, self.Name, Done = True)
        elif isinstance(Other, vec3d):
            def adder(tri):
                """Helper function to __add__; If one tries to add a tringle this one is used."""
                if isinstance(tri, Triangle):
                    return tri + Other
                else:
                    raise TypeError("Wrong input in helper function to __add__.\n The vector addition is not working correctly. ")
            NewMesh = list(map(adder, self.Mesh))
            return MeshObject(NewMesh, self.Mesh, Done = True)
        elif isinstance(Other, MeshObject):
            NewMesh = self.Mesh + Other.Mesh
            return MeshObject(NewMesh, self.Name, Done = True)

    def __mul__(self, Scalar):
        if isinstance(Scalar, (float, int)):
            def mul(tri):
                if isinstance(tri, Triangle):
                    return tri * Scalar
                else:
                    pass
            NewMesh = list(map(mul, self.Mesh))
            return MeshObject(NewMesh, self.Name, Done = True)

        else:
            raise TypeError("Cannot scale a mesh with anything but floats or integers")

    def __dir__(self):
        return ['__str__', '__repr__', '__add__', '__mul__', 'IntalizeFromDict', 'IntalizeFromList', 'SaveToJson', '__init__'] #Update on working

    def __len__(self):
        return len(self.Mesh)




Cube2 = [[0,0,0], [0, 1, 0], [1, 1, 0],
    [0, 0, 0], [1, 1, 0], [1, 0, 0],
    [1, 0, 0], [1, 1, 0], [1, 1, 1],
    [1, 0, 0], [1, 1, 1], [1, 0, 1],
    [1, 0, 1], [1, 1, 1], [0, 1, 1],
    [1, 0, 1], [0, 1, 1], [0, 0, 1],
    [0, 0, 1], [0, 1, 1], [0, 1, 0],
    [0, 0, 1], [0, 1, 0], [0, 0, 0],
    [0, 1, 0], [0, 1, 1], [1, 1, 1],
    [0, 1, 0], [1, 1, 1], [1, 1, 0],
    [1, 0, 1], [0, 0, 1], [0, 0, 0],
    [1, 0, 1], [0, 0, 0], [1, 0, 0]]

MeshCube = MeshObject(Cube2, 'Cube')
vec1 = vec3d(1,1,1)
tri = Triangle(vec1, vec1, vec1)
print(MeshCube.SaveToJson())



"""
Cube = {
    "Cube" : [[[vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0)],
    [vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0)]],
    [[vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1)],
    [vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1)]],
    [[vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1)],
    [vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1)]],
    [[vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0)],
    [vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0)]],
    [[vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1)],
    [vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0)]],
    [[vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0)],
    [vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0)]]]
}
"""
"""
Cube = [[[vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0)],
    [vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0)]],
    [[vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1)],
    [vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1)]],
    [[vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1)],
    [vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1)]],
    [[vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0)],
    [vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0)]],
    [[vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1)],
    [vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0)]],
    [[vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0)],
    [vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0)]]]
"""

"""
Cube = {
    "Cube" : [[Triangle(vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0))],
    [Triangle(vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0))],
    [Triangle(vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1))],
    [Triangle(vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1))],
    [Triangle(vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1))],
    [Triangle(vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1))],
    [Triangle(vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0))],
    [Triangle(vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0))],
    [Triangle(vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1))],
    [Triangle(vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0))],
    [Triangle(vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0))],
    [Triangle(vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0))]]
}

Cube2 = MeshObject(Cube, 'Cube')
print(Cube2)
"""


"""
MeshCube = {
    "South" : [(vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0)),
    (vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0))],
    "East" : [(vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1)),
    (vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1))],
    "North": [(vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1)),
    (vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1))],
    "West" : [(vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0)),
    (vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0))],
    "Top" : [(vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1)),
    (vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0))],
    "Bottom" : [(vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0)),
    (vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0))]
}
"""

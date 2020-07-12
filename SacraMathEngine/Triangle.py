#from .Vector import vec3d
#from .Matrix import matrix3d
from SacraMathEngine import vec3d
import json

class Triangle:
    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        self.set = (self.vec1, self.vec2, self.vec3)

    def __str__(self):
        return f'[{self.vec1}, {self.vec2}, {self.vec3}]'

    def __len__(self):
        return len(self.set)

    def __getitem__(self, index):
        return self.set[index]

    def __mul__(self, Scalar):
        if isinstance(Scalar, (float, int)):
            return Triangle(self.vec1 * Scalar, self.vec2 * Saclar, self.vec3 * Scalar)
        else:
            pass


class MeshObject:
    def __init__(self, Object, Name):
        if not isinstance(Object, dict):
            raise KeyError("Cannot load current file-type")
        else:
            self.Object = Object[Name]

    def __mul__(self, Scalar):

        pass


    def __str__(self):
        return f'{self.Object}'

    def __len__(self):
        return len(self.Object)
        pass

    def __getitem__(self, index):
        return self.Object[index]

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
for i in range(len(Cube2)):
    for j in range(len(Cube2[i])):
        print(Cube2[i][j])



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

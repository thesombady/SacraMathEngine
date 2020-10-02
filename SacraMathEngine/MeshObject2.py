import os
import json
"""
from .Vector import vec3d, vec4d
from .Triangle import Triangle
from .Matrix import matrix3d, Matrix4d
"""
from SacraMathEngine import vec3d, vec4d, Triangle, matrix3d, Matrix4d

class MeshObject3d():

    def __init__(self, Iterated = False):
        if Iterated != False:
            self.Mesh = Iterated
        else:
            self.Mesh = []
        pass

    def __repr__(self):
        return f'{self.Mesh}'

    def _setter(self, object):
        try:
            path = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/saves', NameOfObject + '.json') #change when done
            with open(path) as file:
                Data = json.load(file)
            for x in Data.keys():
                #If there are multiple keys in the .json file, the last key will be used.
                ListMesh = Data[x]
            #print(ListMesh[0])
        except Exception as E:
            #raise PathError("Current file do not exits.")
            raise E

    def __add__(self, Other):
        if isinstance(Other, vec3d):
            NewMesh = self.Mesh.copy()
            ShiftedMesh = []
            for tri in NewMesh:
                ShiftedMesh.append(tri + Other)
            return MeshObject3d(ShiftedMesh)
        elif isinstance(Other, Triangle):
            NewMesh = self.Mesh.copy()
            NewMesh.append(Triangle)
            return MeshObject3d(NewMesh)
        elif isinstance(Other, MeshObject3d):
            pass
        else:
            raise TypeError("[SystemError]: Cannot add object to Mesh")

Mesh = MeshObject3d()
Triangle1 = Triangle(vec3d(1,1,1), vec3d(2,2,2), vec3d(3,3,3))
a = Mesh + Triangle1
print(a)
a = a + vec3d(1,1,1)
print(a)

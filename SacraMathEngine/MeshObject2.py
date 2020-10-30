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

    def __a2dd__(self, Other):
        if isinstance(Other, vec3d):
            NewMesh = self.Mesh.copy()
            ShiftedMesh = []
            for i in range(len(NewMesh)):
                print(type(NewMesh[i]))
            return MeshObject3d(ShiftedMesh)
        elif isinstance(Other, Triangle):
            NewMesh = self.Mesh.copy()
            NewMesh.append(Triangle)
            return MeshObject3d(NewMesh)
        elif isinstance(Other, MeshObject3d):
            pass
        else:
            raise TypeError("[SystemError]: Cannot add object to Mesh")

    def __add__(self, Other):
        if isinstance(Other, Triangle):
            if len(self.Mesh) != 0: # Tests if the is already a mesh exisitng
                NewMesh = self.Mesh.copy()
                NewMesh.append(Other)
                return MeshObject3d(NewMesh)
            else:
                return MeshObject3d([Other])
        elif isinstance(Other, (vec3d, vec4d)):
            if len(self.Mesh) > 0:
                NewMesh = self.Mesh.copy()
                NewMesh1 = []
                for i in range(len(NewMesh)): #We iterate over the Triangle set, the class Triangle can add Vectors
                    NewMesh1.append(NewMesh[i] + Other)
                return MeshObject3d(NewMesh1)
            else:
                raise TypeError("[System]: Cannot add object to Mesh.")
        else:
            pass


    def _saver(self, Name):
        try:
            filepath = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Saves', Name + '.json')
        except Exception as E:
            raise E('[System]: Cant write MeshObject.')
        Meshdata = [self.Mesh[i].set2 for i in range(len(self.Mesh))]
        data = {Name : Meshdata}
        try:
            with open(filepath, 'w') as file:
                json.dump(data, file, indent = 3)
        except Exception as E:
            raise E


Mesh = MeshObject3d()
Triangle1 = Triangle(vec3d(1,1,1), vec3d(2,2,2), vec3d(3,3,3))
a = Mesh + Triangle1
A = (a + Triangle1) + vec3d(1,1,1)
print(A)
A._saver('Kid')

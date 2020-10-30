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
        self._CenterOfMass()

    def __repr__(self):
        return f'{self.Mesh}'

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
            Filepath = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Saves', Name + '.json')
        except Exception as E:
            raise E('[System]: Cant write MeshObject.')
        Meshdata = [self.Mesh[i].set2 for i in range(len(self.Mesh))]
        data = {Name : Meshdata}
        try:
            with open(Filepath, 'w') as file:
                json.dump(data, file, indent = 3)
        except Exception as E:
            raise E

    def _setter(self, Name):
        try:
            Filepath = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Saves', Name + '.json')
        except:
            raise KeyError('[System]: Cant load current file')
        with open(Filepath, 'r') as file:
            JsonData = json.load(file)
        for key in JsonData.keys(): #Should be one key!
            Data = JsonData[key]
        Mesh = []
        for tri1 in Data:
            vec1 = vec3d(tri1[0][0], tri1[0][1], tri1[0][2])
            vec2 = vec3d(tri1[1][0], tri1[1][1], tri1[1][2])
            vec3 = vec3d(tri1[2][0], tri1[2][1], tri1[2][2])
            tri2 = Triangle(vec1, vec2, vec3)
            Mesh.append(tri2)
        return MeshObject3d(Mesh)

    def _CenterOfMass(self):
        if len(self.Mesh) == 0:
            pass
        else:
            Center = vec3d(0,0,0)
            for i in range(len(self.Mesh)):
                sum = (self.Mesh[i][0] + self.Mesh[i][1] + self.Mesh[i][2]) * (1/3)
                Center += sum
            Center = Center/len(self.Mesh)
            deviation = []
            for i in range(len(self.Mesh)):
                for j in range(3):
                    delta = Center - self.Mesh[i][j]
                    try:
                        deviation.append(abs(delta.norm()))
                    except:
                        raise ValueError('[System]: Cant compute center of mass, error in deviation definition')
            Epsilon = max(deviation)
            self.CenterOfGravity = (Center, Epsilon)
            print(self.CenterOfGravity)



"""
Mesh = MeshObject3d()
Triangle1 = Triangle(vec3d(1,1,1), vec3d(2,2,2), vec3d(3,3,3))
a = Mesh + Triangle1
A = (a + Triangle1) + vec3d(1,1,1)
print(A)
#A._saver('Kid')
"""
Mesh = MeshObject3d()._setter('Kid')

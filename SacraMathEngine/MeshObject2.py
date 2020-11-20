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

    def __mul__(self, scalar): #Scales with a scalar
        if not isinstance(scalar, (float, int)):
            raise TypeError("[System]: Can only scale with scalar values")
        else:
            Mesh = self.Mesh.copy()
            try:
                NewMesh = [Mesh[i] * scalar for i in range(len(Mesh))]
                return MeshObject3d(NewMesh)
            except:
                raise KeyError('[System]: Cant compute __mul__ method.')

    def __len__(self):
        return len(self.Mesh)

    def __getitem__(self, index):
        return self.Mesh[index]

    def _RemoveTriangle(self, triangle):
        if isinstance(triangle, Triangle):
            for i in range(len(self.Mesh)):
                if triangle == self.Mesh[i]: #self.Mesh[i] is a triangle
                    MeshCopy = self.Mesh.copy()
                    del MeshCopy[i]
                    return MeshCopy
                else:
                    raise KeyError("[System]: Variable, triangle, does not exist in the mesh")
        else:
             raise TypeError("[System]: Input, triangle is or wrong time, needs to be of type triangle")


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





"""
Mesh = MeshObject3d()
Triangle1 = Triangle(vec3d(1,1,1), vec3d(2,2,2), vec3d(3,3,3))
a = Mesh + Triangle1
A = (a + Triangle1) + vec3d(1,1,1)
print(A)
#A._saver('Kid')
"""
"""Making a pyramid/tetrahydron """
"""
Mesh = MeshObject3d()
a = Mesh + Triangle(vec3d(0,0,0), vec3d(1,0,0), vec3d(0,0,1)) #Bottom
a = a + Triangle(vec3d(0,0,0), vec3d(0,1,0), vec3d(0,0,1)) #Side 1
a = a + Triangle(vec3d(1,0,0), vec3d(0,1,0), vec3d(0,0,1)) #Side 2
a = a + Triangle(vec3d(1,0,0), vec3d(0,1,0), vec3d(0,0,0)) #Side 3
a._saver('Tetrahydron')
"""

"""Making a Cube"""
"""
Mesh = MeshObject3d()
A = Mesh + Triangle(vec3d(0,0,0), vec3d(0,0,1), vec3d(1,0,1)) #Buttom1
A = A + Triangle(vec3d(1,0,0), vec3d(1,1,0), vec3d(0,1,0)) #Bottom2
A = A + Triangle(vec3d(0,0,0), vec3d(0,1,0), vec3d(1,0,0)) #Side1-1 #Front-1-2
A = A + Triangle(vec3d(1,0,0), vec3d(1,1,0), vec3d(0,1,0)) #Side1-2
A = A + Triangle(vec3d(0,0,0), vec3d(0,1,0), vec3d(0,0,1)) #Side2-1 #West-1-2
A = A + Triangle(vec3d(0,0,1), vec3d(0,1,1), vec3d(0,1,0)) #Side2-2
A = A + Triangle(vec3d(0,1,0), vec3d(1,1,0), vec3d(1,1,1)) #Side3-1 #Top-1-2
A = A + Triangle(vec3d(1,1,1), vec3d(0,1,1), vec3d(1,1,0)) #side3-2
A = A + Triangle(vec3d(1,1,0), vec3d(1,1,1), vec3d(1,0,0)) #Side4-1 #East-1-2
A = A + Triangle(vec3d(1,0,0), vec3d(1,0,1), vec3d(1,1,1)) #Side4-2
A = A + Triangle(vec3d(1,1,1), vec3d(1,0,1), vec3d(0,0,1)) #Side5-1 #North-1-2
A = A + Triangle(vec3d(0,0,1), vec3d(0,1,1), vec3d(1,1,1)) #Side5-2
A._saver('Cube')
"""

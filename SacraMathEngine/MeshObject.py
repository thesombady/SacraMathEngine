import os
import json
from .Vector import vec3d, vec4d
from .Triangle import Triangle
from .Matrix import matrix3d, Matrix4d
#from SacraMathEngine import vec3d, vec4d, Triangle, matrix3d



class PathError(Exception):
    """Error-handeling."""
    pass

class MeshObjectError(Exception):
    """Error-handeling."""
    pass


class MeshObject:

    AllActiveMeshes = []
    MeshCenterOfMass = []

    def __init__(self, Iterated = None):
        """A small __init__ function, pass no argument, it's only when scaling or adding something the Iterated argument
        is used."""
        if Iterated != None:
            self.Mesh = Iterated #Everything should be in correct format by this point.
            #print(self.Mesh)
            self.AllActiveMeshes.append(self.Mesh)
            self.CenterOfMass()
            #print(self.Mesh)
        else:
            self.Mesh = None #Just initialize the artibute self.Mesh

    def setter(self, NameOfObject):
        """The argument NameOfObject is path to the MeshObject, of which should be in json format. The path will be found
        as in the Saves folder in SacraGameEngine."""
        try:
            path = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/saves', NameOfObject + '.json') #change when done
            with open(path) as file:
                Data = json.load(file)
            for x in Data.keys():
                #If there are multiple keys in the .json file, the last key will be used.
                ListMesh = Data[x]
            #print(ListMesh[0])
        except:
            raise PathError("Current file do not exits.")
        Vectors = []
        self.Mesh = []
        for vec in ListMesh:
            vec = vec3d(vec[0], vec[1], vec[2])
            Vectors.append(vec)
        for i in range(0, len(Vectors)-2, 3):
            self.Mesh.append(Triangle(Vectors[i], Vectors[i + 1], Vectors[i + 2]))
        self.AllActiveMeshes.append(self.Mesh)
        self.CenterOfMass()
        return '[System:] Intalization have been completed.'

    def getter(self):
        return f'{self.Mesh}'

    def __repr__(self):
        return f'{self.Mesh}'

    def __str__(self):
        return f'{self.Mesh}'

    def __add__(self, Object):
        if isinstance(Object, Triangle):
            NewMesh = self.Mesh.copy()
            NewMesh.append(Object)
            return MeshObject(NewMesh)
        elif isinstance(Object, MeshObject):
            NewMesh = self.Mesh + Object.Mesh
            return MeshObject(NewMesh)
        elif isinstance(Object, vec3d):
            NewMesh = self.Mesh.copy()
            ShiftedMesh = []
            for tri in NewMesh:
                ShiftedMesh.append(tri + Object)
            return MeshObject(ShiftedMesh)
        else:
            pass

    def __len__(self):
        return len(self.Mesh)

    def __mul__(self, Object):
        if isinstance(Object, (int, float)):
            NewMesh = []
            for tri in self.Mesh: # Each atribute "tri" is a triangle object.
                NewMesh.append(tri * Object)
            return MeshObject(NewMesh)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.Mesh[index]

    def __dir__(self):
        return ['__mul__', '__add__', 'CenterOfMass', 'Collission', '__len__', '__getitem__',
        '__str__', '__repr__', 'getter', 'setter', 'SaveToJson']

    def CenterOfMass(self):
        """Returns a vuege center of mass, with some deviation; The deviation is the longest distance from center of mass.
        This method is not optimized for non-symetrical Meshes."""
        center = vec3d(0,0,0)
        for i in range(len(self.Mesh)):
            sum = (self.Mesh[i][0] + self.Mesh[i][1] + self.Mesh[i][2]) * (1/3)
            center += sum
        center = center / len(self.Mesh)
        deviation = []
        for i in range(len(self.Mesh)):
            for j in range(3):
                delta = center - self.Mesh[i][j]
                if delta != None:
                    deviation.append(abs(delta.norm()))
        epsilon = max(deviation)
        self.CenterOfGravity = (center, epsilon)
        self.MeshCenterOfMass.append(self.CenterOfGravity)


    def Collission(self):#Removed and added to the physics engine
        """Returns a boolean expression for each object colliding; Works upon the center of mass definition."""
        MeshesToSearchThrough = self.AllActiveMeshes.copy()
        MeshesCenterOfMass = self.MeshCenterOfMass.copy()
        try:
            IndexForMesh = MeshesToSearchThrough.index(self.Mesh)
            IndexForMass = MeshesCenterOfMass.index(self.CenterOfGravity)
            del MeshesToSearchThrough[IndexForMesh: IndexForMass +1]
            del MeshesCenterOfMass[IndexForMass: IndexForMass + 1]
        except:
            raise MeshObjectError("Cannot performe Collission calculations, indicies do not exist \n Needs atleast two meshes to search through.")
        for mesh in MeshesCenterOfMass: #This is not yet completed!
            if self.CenterOfGravity[1] == 0:
                print('Something happens')


    def SaveToJson(self, Name):
        """Save the current MeshObject as a .json file."""
        # Add so that we cannot override!
        try:
            path = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/saves', Name + '.json')
        except:
            raise PathError("Cannot load the path")
        MeshSave = []
        for i in range(len(self.Mesh)):
            for j in range(len(self.Mesh[i])):
                MeshSave.append([self.Mesh[i][j][0], self.Mesh[i][j][1], self.Mesh[i][j][2]])#This is the vector
        data = {Name : MeshSave}
        try:
            with open(path, 'w') as file:
                json.dump(data, file, indent = 3)
        except:
            raise PathError("Cannot save file.")

#Cube = MeshObject()

Cube = """{"Cube" : [[0,0,0], [0, 1, 0], [1, 1, 0],
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
    [1, 0, 1], [0, 0, 0], [1, 0, 0]]}"""


#data = json.loads(Cube)
#rawdata = json.dumps(data, indent = 4)
#print(json.dumps(data, indent = 4))


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

Cube2 = MeshObject3d(Cube, 'Cube')
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

import os
import json
from SacraMathEngine import vec3d, Triangle

class PathError(Exception):
    """Error-handeling."""
    pass


class MeshObject:

    AllActiveMeshes = []

    def __init__(self, Iterated = None):
        """A small __init__ function, pass no argument, it's only when scaling or adding something the Iterated argument
        is used."""
        if Iterated != None:
            self.Mesh = Iterated #Everything should be in correct format by this point.
            print(self.Mesh)
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
        """
        for key in Data.keys():
            print(key, Data[key])
        """ # Small thing to get acess to the name
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


    def SaveToJson(self):
        Triangles = []
        for tri in self.Mesh:
            Triangles.append([tri[0], tri[1], tri[2]])
        print(Triangles)
        Vectors = []
        for i in range(len(Triangles)):
            Vectors.append([Triangles[i][0], Triangles[i][1], Triangles[i][2]])
            print(i)#Not working this solution
        print(Vectors)







Cube = MeshObject()
(Cube.setter('test'))
#print(len(Cube))#Output : 12
vec1 = vec3d(1,1,1)
vec2 = vec3d(1,1,1)
vec3 = vec3d(1,1,1)
tri = Triangle(vec1, vec2, vec3)
#print(Cube * 2)
#Cube.SaveToJson()


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

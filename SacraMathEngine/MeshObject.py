import os
import json
from SacraMathEngine import vec3d, Triangle

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
            print(self.Mesh)
            self.AllActiveMeshes.append(self.Mesh)
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
        self.AllActiveMeshes.append(self.Mesh)
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

    def CenterOfMass(self):
        """Returns a vuege center of mass, with some deviation; The deviation is the longest distance from center of mass.
        This method is not optimized for non-symetrical Meshes."""
        CenterOfTriangles = []
        for item in self.Mesh:
            center = item[0] + item[1] + item[2]
            CenterOfTriangles.append(center)
        sum = vec3d(0,0,0)
        print(CenterOfTriangles)
        for vector in CenterOfTriangles:
            sum += vector
        center = sum * (1/len(CenterOfTriangles))
        delta =


    def Collission(self):
        """Returns a boolean expression for each object colliding; Works upon the center of mass definition."""
        MeshesToSearchThrough = self.AllActiveMeshes.copy()
        try:
            index = MeshesToSearchThrough.index(self.Mesh)
            MeshesToSearchThrough.remove(self.Mesh)
            CenterOfMasses = MeshCenterOfMass.copy()
            del CenterOfMasses[index: index + 1]
        except:
            raise MeshObjectError('Mesh do not exist in the list of Meshes.')
        #We have a copy of the correct meshes to verify relate distances

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
Cube.CenterOfMass()


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

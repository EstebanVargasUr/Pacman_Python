import CreaNivel.MapRand as Nivel
import random
from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
        self.direcciones = {}
        self.nodes = defaultdict(list)
        self.distances = {}
    
    def add_edge(self, from_node, to_node, weight, direccion,direccion2):
        # Note: assumes edges are bi-directional
        self.distances[(from_node, to_node)] = weight

        self.nodes[from_node].append(from_node)

        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        self.direcciones[(from_node, to_node)] = direccion
        self.direcciones[(to_node, from_node)] = direccion2

    def floyd_warshall(self):
        nodes = list(self.nodes)

        for i in nodes:
            dict_i = {}
            for j in nodes:
                if i == j:
                    dict_i[j] = 0
                    continue
                try:
                    dict_i[j] = self.weights[i][j]#['weight']
                except:
                    dict_i[j] = float("inf")

            self.distances[i] = dict_i

        for i in nodes:
            for j in nodes:
                for k in nodes:
                    ij = self.distances[i][j]
                    ik = self.distances[i][k]
                    kj = self.distances[k][j]

                    if ij > ik + kj:
                        self.distances[i][j] = ik + kj

        return self.distances
    
def Dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    current_shortest_weight = 0
    direcciones = []
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        if next_node is not None:
            direcciones.append(graph.direcciones[(current_node, next_node)])
        current_node = next_node
        
    # Reverse path
    path = path[::-1]
    direcciones = direcciones[::-1]

    # print("Costo: " , current_shortest_weight)
    # print("Direccion: " , direcciones)
    return direcciones   

def camino(P, u, v):                        #Camino u⤳v dado por Floyd-Warshall
    lista = [v]                             #El camino termina en v
    while v != u:                           #Hasta no llegar a u
        v = P[u, v]                         #…retrocedemos un paso
        lista.append(v)                     
    lista.reverse()                         #Enlistamos el recorrido en reversa
    return lista

def floyd_warshall(G,inicial):
    D, P = dict(), dict()                   #Matrices de distancias y caminos
    for u in G.nodes:                             #Inicializar caminos
        for v in G.nodes:
            if v in G.edges[u]:     
                          #¿v es vecino de u?
                D[u, v], P[u, v] = G.weights[(u,v)], u #Distancia y camino inicial
            else: D[u, v], P[u, v] = float("inf"), None #No hay camino inicial

    for k in G.nodes:                             #Vértice k en consideración
        for u in G.nodes:                         #Iterar sobre toda pareja de vért.
            for v in G.nodes:
                atajo = D[u, k] + D[k, v]   #Distancia de u a v pasando por k
                if atajo < D[u, v]:         #¿Pasar por k forma un atajo?
                    D[u, v] = atajo         #Actualizar distancias
                    P[u, v] = P[k, v]       #Actualizar caminos
    
    Recorrido = list()
    Destino = random.randint(1, len(G.nodes))

    for u in G.nodes:
        for v in G.nodes:
            if u != v and D[u, v] < float('inf'):
                lista = camino(P, v, u)
                if str(lista[len(lista)-1]) == str(inicial) and str(lista[0]) == str(Destino):
                    for i in range(len(lista)):
                        #print(lista[i],end=" ")
                        if i+1 <len(lista):
                            Recorrido.append(G.direcciones[(lista[i],lista[i+1])])
                    return Recorrido
                #     if i+1 < len(lista):
                #         print(G.direcciones[(lista[i],lista[i+1])],end='─►')
                #         #return G.direcciones[(lista[i],lista[i+1])]
                # print("|",end="")
                # print()
                # print('─►'.join(camino(P, u, v)), ':', D[u, v])
                #print()

def CreaGrafo(MatrizO):
    Grafo = Graph()
    MatrizV = Nivel.DeterminaVertice(MatrizO) # LA MATRIZ QUE CONTIENE LA UBICACION DE LOS VERTICES Y ADEMAS LA CANTIDAD DE VERTICES
    Peso = 1
    
    for i in range(21):
        for j in range(21):
            #SI ES UN VERTICE
            if MatrizV[i][j] != ' ' and MatrizV[i][j] != '#':
                Aux = 0 
                Peso = 1

                if MatrizV[i][j+1] == '#' and MatrizV[i][j-1] ==' ' and MatrizV[i+1][j] == '#' and MatrizV[i-1][j] == ' ':
                    Grafo.nodes[MatrizV[i][j]].append(MatrizV[i][j])

                # EVALUACION ADYACENTE DERECHA 
                if MatrizV[i][j+1] != '#':
                    Aux = j+1 
                    while Aux != 21 and MatrizV[i][Aux] != '#':
                        if MatrizV[i][Aux] != ' ' and MatrizV[i][Aux] != '#':
                            Grafo.add_edge(MatrizV[i][j], MatrizV[i][Aux], Peso,"izquierda","derecha") # SE INVIERTE PARA APLICAR DE MEJOR MANERA EL RECORRIDO
                            break
                        Peso += 1
                        Aux+=1

                Aux = 0 
                Peso = 1
                # EVALUACION ADYACENTE ABAJO 
                if MatrizV[i+1][j] != '#':
                    Aux = i+1 
                    while Aux != 21 and MatrizV[Aux][j] != '#':
                        if MatrizV[Aux][j] != ' ' and MatrizV[Aux][j] != '#':
                            Grafo.add_edge(MatrizV[i][j], MatrizV[Aux][j], Peso,"arriba","abajo")    # SE INVIERTE PARA APLICAR DE MEJOR MANERA EL RECORRIDO
                            break
                        Peso += 1
                        Aux+=1
                        
    # for u in range(80):
    #     print(u,"Vecinos: ",Grafo.edges[str(u)])

    return MatrizV, Grafo




import CreaNivel.MapRand as Nivel
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
    
    def add_edge(self, from_node, to_node, weight, direccion,direccion2):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        self.direcciones[(from_node, to_node)] = direccion
        self.direcciones[(to_node, from_node)] = direccion2

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
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
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def dijsktra(graph, initial, end):
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

    print("Costo: " , current_shortest_weight)
    return path , direcciones   

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




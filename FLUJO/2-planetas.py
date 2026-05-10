"""
(★) La red de transporte intergaláctico es una de las maravillas del nuevo imperio terráqueo.
Cada tramo de rutas galácticas tiene una capacidad infinita de transporte entre ciertos
planetas. No obstante, por burocracia - que es algo que no los enorgullece - existen puestos
de control en cada planeta que reduce cuantos naves espaciales pueden pasar por día por
ella. Por una catástrofe en el planeta X, la tierra debe enviar la mayor cantidad posible de
naves de ayuda. Por un arreglo, durante un día los planetas solo procesaran en los puestos
de control aquellas naves enviadas para esta misión. Tenemos que determinar cuál es la
cantidad máxima de naves que podemos enviar desde la tierra hasta el planeta X.
Sugerencia: considerar a este un problema de flujo con capacidad en nodos y no en ejes
"""
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.capacidad = {}
        pass
    def agregar_arista(self, u, v, capacidad):
        self.grafo[u].add(v)
        self.grafo[v].add(u)
        self.capacidad[(u, v)] += capacidad
        self.capacidad[(v, u)] = 0
    
    def adyacentes(self, u): return self.grafo[u]
        
        
def transformar_planetas(rutas, capacidades):
    grafo = Grafo()
    # Medio que ya tierra y X deberian estar en las rutas por LOGICA
    # Divido en direcciones internas y luego externas
    
    for planeta, cap in capacidades:
        p_in = f"{planeta}_in"
        p_out = f"{planeta}_out"
        grafo.agregar_arista(p_in, p_out, cap)
        
    for p1, p2 in rutas:
        grafo.agregar_arista(f"{p1}_out", f"{p2}_in", float("inf"))
        grafo.agregar_arista(f"{p2}_out", f"{p1}_in", float("inf"))
        
    return grafo


def bfs(grafo, s, t):
    return # Simulo bfs, no hace falta codearlo

def aumento(b, camino, grafo):
    for u, v in camino:
        grafo.capacidad[(u,v)] -= b
        grafo.capacidad[(v,u)] += b

def bottleneck(camino, grafo):
    return min(grafo.capacidad[(u,v)] for u, v in camino)

def edmons_karp(grafo, s, t): # O(V * E^2)
    flujo = 0
    while True:
        camino = bfs(grafo, s, t)
        if camino == None: 
            break
        b = bottleneck(camino, grafo)
        aumento(b, camino, grafo)
        flujo+=b
    return flujo
# Por cada planeta, saco dos nodos nuevos
# Uno que sea el de entrada y otro el de salida 
# ¿Que es el modelo del problema no? uno de entrada infinita peeero salida finita


# Rutas lo pienso como un (u,v)
# Capacidades son el "TAX" q cobra cada planeta
def galacticos(Tierra, X, rutas, capacidades):
    grafo_transformado = transformar_planetas(rutas, capacidades)
    s = f"{Tierra}_in"
    t = f"{X}_out"
    
    # |V| = 2 * Planeta
    # |E| = P + 2 * R
    flujo_max = edmons_karp(grafo_transformado, s, t)
    # => O(V* E^2) = O(P*(P+R))
    return flujo_max
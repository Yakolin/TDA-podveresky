"""
(★★) Para un evento solidario un conjunto de n personas se ofrecieron a colaborar. En el
evento hay m tareas a desarrollar. Cada tarea tiene un cupo máximo de personas que la
puede realizar. A su vez cada persona tiene ciertas habilidades que la hacen adecuadas para
un subconjunto de tareas. 
Proponga una solución mediante red de flujos que maximice la cantidad de personas asignadas a las tareas. 

¿Hay forma de lograr asegurarnos un piso mínimo de personas en cada tarea? 
¿Cómo impacta en la solución presentada en el punto anterior?
"""
class Grafo:  # Planteo esta estructura para facilitar el codigo
    def __init__(self):
        self.grafo = {}
        self.capacidad = {}

    def agregar_aristas(self, u, v, cap):
        self.grafo[u].add(v)
        self.grafo[v].add(u)  
        self.capacidad[(u, v)] += cap
        self.capacidad[(v, u)] = 0

    def obtener_adyacentes(self, u):
        return self.grafo[u]

    def obtener_capacidad(self, u, v):
        return self.capacidad[(u, v)]
    
def transformar_problema(s,t, personas, tareas):
    grafo = Grafo()
    
    for persona in personas.keys():
        grafo.agregar_aristas(s, persona, 1)
        
    for nombre, maximo in tareas:
        grafo.agregar_aristas(nombre, t, maximo)
    
    for persona, habilidades in personas.items():
        for tarea in habilidades:
            grafo.agregar_aristas(persona, tarea, 1)
    
    return grafo 

def bfs(grafo, s, t): return
def bottleneck(grafo, camino):
    return min(grafo.capacidad[(u,v)] for u, v in camino)

def aumento(grafo, camino, b):
    for u,v in camino:
        grafo.capacidad[(u,v)] -= b
        grafo.capacidad[(v,u)] += b
        
def edmons_karp(grafo, s,t):
    flujo = 0
    while True: 
        camino = bfs(grafo, s, t)
        if not camino: break
        b = bottleneck(grafo, camino)
        aumento(grafo, camino, b)
        flujo+=b
        
# Personas de la forma {persona: [tareas]}
def evento_solidario(personas, tareas):
    grafo = transformar_problema("S", "T", personas, tareas)
    flujo = edmons_karp(grafo, "S", "T")
    
    return flujo


"""
Para lo otro, debemos de plantear una red de flujo con restricciones
es decir, agregar un S* y un T*
Calculamos las capacidades de tarea -> t con p = max-min

Calculamos las demandas por la formula de entradas y salidas
Lv = sum (min_entrada) - sum(min_salida)

dv = dv-Lv

si dv < 0: Se agrega arista al S* con -dv
sino al T* con dv
"""

def transformar_problema_demandas(s,t, personas, tareas):
    grafo = Grafo()
    
    for persona in personas.keys():
        grafo.agregar_aristas(s, persona, 1)
        
    for persona, habilidades in personas.items():
        for tarea in habilidades:
            grafo.agregar_aristas(persona, tarea, 1)
    
    t_star = "T_star"
    s_tar = "S_star"
    # Segun las formulas
    # D tarea = min => Dtarea > 0 => Se une a T_star
    # Dt = -min => Dtarea < 0 => Se une a S_star
    for nombre, minimo, maximo in tareas:
        grafo.agregar_aristas(nombre, t, maximo-min)
        grafo.agregar_aristas(nombre, t_star, minimo)
        grafo.agregar_aristas(s_tar, t, minimo)
        
    # En teoria se agrega una arista de retorno para la circulacion 
    grafo.agregar_aristas(t, s, float("inf")) # A CHEKEAR SI ESTO ES ASI O NO... PEEERO...
    return grafo 


"""
(★) La policía de la ciudad tiene “n” comisarías dispersas por la ciudad. Para un evento
deportivo internacional deben asignar la custodia de “m” centros de actividades. Una
comisaría y un centro de actividades pueden ser emparejados si y sólo si la distancia entre
ellos no es mayor a un valor d. Contamos con la distancia entre todos los centros y las
comisarías. Una comisaría sólo puede custodiar un centro. El centro puede ser custodiado
por una comisaría. 

Determinar si es posible la asignación de tal forma que todos los centros estén custodiados. 

¿Cómo modificaría la resolución del problema si en lugar de que cada
centro de actividades i tenga que ser asignado a una sola comisaría, tenga que ser asignado
a m_i comisarías? 

¿Cómo modificaría la resolución del problema si además hubiera una
restricción entre comisarías que implicaría que una comisaría Ni y una Nj no pudieran ser
asignadas juntas a un centro Mi? 

¿Para qué casos dejaría de ser eficiente la resolución?
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
        
def transformar_problema(comisarias, centros, distancia, d):
    grafo = Grafo()
    s = "s"
    t = "t"
    for c in comisarias:
        grafo.agregar_arista(s, c, 1)
    for m in centros:
        grafo.agregar_arista(m, t, 1)
    
    for c in comisarias:
        for m in centros:
            if distancia[(c,m)] < d: 
                grafo.agregar_arista(c,m,1)
    
    return grafo
def edmons_karp(grafo_transformado, s, t):
    flujo = 0
    # supongo q hice edmons
    return flujo
    
# Distancia lo pienso como un diccionario de tuplas (u,v) = distancia
def policias(comisarias, centros, distancia, d):
    # |E| = N + N*M + M = N*M
    # |V| = 2 + N + M
    
    grafo_transformado = transformar_problema(comisarias, centros, distancia, d) # O(N*M)
    
    flujo_max = edmons_karp(grafo_transformado, "s", "t") # O(V*E^2)
    
    # En el peor caso => O((N+M) * (N*M)^2)
    
    # Sin embargo, como son unitarias y es un grafo bipartito practicamente
    # A lo peor es O(F * |E|) = O(M * (N*M))
    
    return flujo_max == len(centros)


"""
Para la primer pregunta: 
    debemos de modificar que en la arista de centro -> T la capacidad = m_i
    for m, demanda in centros:
        grafo.agregar_arista(m, t, demanda)
    y el flujo_max = sum(m_i) para saber si se resolvio o no
    
Para la segunda: 
    Creo que no se puede resolver porque flujo no tiene una forma de recordar combinaciones

Para la tercera: 
    no comprendo mucho la pregunta)?
"""
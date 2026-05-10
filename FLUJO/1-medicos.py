"""
(★) La sala de guardia de un hospital tiene que tener al menos un médico en todos los
feriados y en los fines de semana largos de feriados. Cada profesional indica sus
posibilidades: por ejemplo alguien puede estar de guardia en cualquier momento del fin de
semana largo del 9 de julio (p. ej. disponibilidad de A para el 9 de julio = (Jueves 9/7, Viernes
10/7, Sábado 11/7, Domingo 12/7)), también puede suceder que alguien pueda sólo en parte
(por ejemplo, disponibilidad de B para 9 de julio = (Jueves 9/7, Sábado 11/7, Domingo 12/7)).
Aunque los profesionales tengan múltiples posibilidades, a cada uno se lo puede convocar
para un solo día (se puede disponer de B sólo en uno de los tres días que indicó). Para
ayudar a la sala de guardia a planificar cómo se cubren los feriados durante todo el año
debemos resolver el problema de las guardias: Existen k períodos de feriados (por ejemplo, 9
de julio es un período de jueves 9/7 a domingo 12/7, en 2019 Día del Trabajador fue un
período de 1 día: miércoles 1 de mayo, etc.). Dj es el conjunto de fechas que se incluyen en el
período de feriado j-ésimo. Todos los días feriados son los que resultan de la unión de todos
los Dj. Hay n médicos y cada médico i tiene asociado un conjunto Si de días feriados en los
que puede trabajar (por ejemplo B tiene asociado los días Jueves 9/7, Sábado 11/7, Domingo
12/7, entre otros).
Proponer un algoritmo polinomial (usando flujo en redes) que toma esta información y
devuelve qué profesional se asigna a cada día feriado (o informa que no es posible resolver
el problema) sujeto a las restricciones:

○ Ningún profesional trabajará más de F días feriados (F es un dato), y sólo en días en
los que haya informado su disponibilidad.

○ A ningún profesional se le asignará más de un feriado dentro de cada período Dj.

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
    
def generar_transformacion(medicos, medicos_disponibilidad, dias, findes, F):
    grafo = Grafo()
    for m in medicos:
        grafo.agregar_aristas("S", m, F)
        for nombre_finde in findes:
            nodo_medico_finde = f"{m}_finde_{nombre_finde}"
            grafo.agregar_aristas(m, nodo_medico_finde, 1)
            for dia in dias:
                if dia in medicos_disponibilidad[m]:
                    grafo.agregar_aristas(nodo_medico_finde, dia, 1)
                
    for d in dias: 
        grafo.agregar_aristas(d, "T", 1)
        
    return grafo


def bfs(grafo, origen, destino):
    visitados = [origen]
    cola = [origen]
    padres = {origen: None}
    
    while cola: 
        actual = cola.popleft()
        if actual == destino:
            break
        for vecino in grafo.obtener_adyacentes(actual):
            if vecino in visitados or grafo.obener_capacidad(actual, vecino) <= 0: continue
            
            visitados.add(vecino)
            padres[vecino] = actual
            cola.append(vecino)
        
    camino = []
    actual = destino
    while actual: 
        nodo_prev = padres[actual]
        camino.append((nodo_prev, actual))
        actual = nodo_prev
    return camino

def bottleneck(grafo ,camino):
    return min( grafo.obtener_capacidad(u,v) for u, v in camino)

def aumento(b, camino, grafo):
    for u,v in camino:
        grafo.capacidad[(u,v)] -= b
        grafo.capacidad[(v,u)] += b
        
def edmons_karp(grafo, s, t):
    grafo_residual = grafo.copy()
    flujo = 0
    while True:
        camino = bfs(grafo, s, t)
        if not camino: break
        
        b = bottleneck(grafo, camino)
        aumento(b, camino, grafo)
        flujo+=b
        
    return flujo, grafo_residual
# medicos son "nodos", y cada
def organizar_medicos(medicos, dias,  findes, F):
    grafo_transformado = generar_transformacion(medicos, dias, findes, F)
    flujo, grafo_residual = edmons_karp(grafo_transformado, "S", "T")
    if flujo <= len(dias):
        return "No funco"
    
    return "funco"
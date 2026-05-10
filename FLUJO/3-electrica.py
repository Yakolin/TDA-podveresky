"""
(★) La compañía eléctrica de un país nos contrata para que le ayudemos a ver si su red de
transporte desde su nueva generadora hidroeléctrica hasta su ciudad capital es robusta. Nos
otorgan un plano con la red eléctrica completa: todas las subestaciones de distribución y red
de cableados de alta tensión. Lo que quieren que le digamos es: cuantas secciones de su red
se pueden interrumpir antes que la ciudad capital deje de recibir la producción de la
generadora? (Sugerencia: investigue sobre el Teorema de Menger) Puede informar cual es el
subconjunto de ejes cuya falla provoca este problema?

"""
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.capacidad = {}
    def agregar_arista(self, u, v, cap):
        self.grafo[u].add(v)
        self.grafo[v].add(u)
        self.capacidad[(u,v)] += self.capacidad
        self.capacidad[(v,u)] = 0
    def adyacentes(self, u): return self.grafo[u]
    
def transformar_grafo(cableados):
    grafo = Grafo
    for u, v in cableados:
        grafo.agregar_arista(u, v, 1)    
    return grafo

def edmons_karp(grafo, fuente, capital):
    # Ya lo codee como 5 veces jajajaja
    return

def obtener_corte_minimo(grafo_residual, fuente):
    S = [fuente]
    cola = [fuente]
    while cola:
        actual = cola.popleft()
        for v in grafo_residual.adyacentes(actual):
            if v in S or grafo_residual.capacidad[(actual,v)] <= 0: continue
            S.append(v)
            cola.append(v)
    
    return S, grafo_residual.nodos() - S 

def mapa_electrico(cableados, fuente, capital):
    # Aca supongo que tanto fuente y capital estan en los cableados
    grafo_transformado = transformar_grafo( cableados)
    flujo_max, grafo_residual = edmons_karp(grafo_transformado, fuente, capital)
    
    # Como modele el problema con aristas de peso 1, el flujo_max me da la capacidad del corte minimo
    # Es decir, el flujo maximo es la cant de secciones que suministran a la capital
    
    # Para buscar aquellos que su falla genera problemas, 
    # tenemos que hacer una busqueda de las aristas que conectan S con el conjunto T
    S, T = obtener_corte_minimo(grafo_residual, fuente)
    
    # Aca hay que buscar cada eje tal que u este en S y v este en T 
     
    return
"""
(★) Una compañía minera nos pide que la ayudemos a analizar su nueva explotación. Ha
realizado el estudio de suelos de diferentes vetas y porciones del subsuelo. Con estos datos
se ha construido una regionalización del mismo. Cada región cuenta con un costo de
procesamiento y una ganancia por extracción de metales preciosos. (En algunos casos el
costo supera al beneficio). Al ser un procesamiento en profundidad ciertas regiones
requieren previamente procesar otras para acceder a ellas. La compañía nos solicita que le
ayudemos a maximizar su ganancia, determinando cuales son las regiones que tiene que
trabajar. Tener en cuenta que el costo y ganancia de cada región es un valor entero. Para
cada región sabemos cuales son aquellas regiones que le preceden. 
Resolver el problema planteado utilizando una aproximación mediante flujo de redes
"""
class Grafo:
    def __init__(self):
        pass

def transformar_problema(regiones, requisitos):
    s = "s"
    t = "t"
    
    # Recalculamos todos los valores utiles
    regiones = [(r[0], r[1] - r[2]) for r in regiones]
    
    C = sum(r[1] for r in regiones if r[1] > 0)
    
    grafo = Grafo()
    
    for nombre, ganancia in regiones:
        if ganancia < 0:
            grafo.agregar_arista(nombre, t, -ganancia)
        elif ganancia > 0:
            grafo.agregar_arista(s, nombre, ganancia)
        
    # Supongamos que requisitos me da las predecencias, es decir, i->j , i->j+1... 
    for j, i in requisitos:
        # j precede a i 
        grafo.agregar_arista(i, j, C+1)
    return grafo, C

def edmons_karp(grafo, s, t):
    return
def recorrer_desde_s(grafo_residual, s):
    return

# Regiones de la forma (nombre, gi, ci)
def minar(regiones, requisitos):
    grafo, C = transformar_problema(regiones, requisitos)
    flujo_max, grafo_residual = edmons_karp(grafo, "s", "t")
    # El flujo maximo en estos ejercicios nos devuelve 
    # Lo que no pudimos ganar de la cantidad C
    # Es decir, la PENALIZACION
    ganancia_maxima = C - flujo_max
    proyectos_utiles = recorrer_desde_s(grafo_residual, "s")
    
    return ganancia_maxima, proyectos_utiles
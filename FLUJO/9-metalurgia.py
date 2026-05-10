"""
(★★) Un taller metalúrgico cuenta con un conjunto de M controles numéricos
computarizados (CNC). Cada uno de ellos puede realizar trabajos de duración en bloques de
1 hora. Por otro lado, cuenta con N tareas a realizar. Cada tarea i tiene una duración de
horas de desarrollo, una hora de posible comienzo (cuando puede comenzar a realizarse) y
una hora de entrega (momento donde debe estar finalizada). Las tareas pueden realizarse
parcialmente y utilizarse para su elaboración una o varias máquinas. Por ejemplo si la tarea
A requiere 4 horas. Podría realizarse 1 hora en la máquina 1 y luego de un intervalo concluir
su desarrollo en la máquina B (3 horas restantes). El jefe de planta nos solicita nuestra ayuda
para que le ayudemos a determinar si podrá cumplir con la finalización de las tareas en
tiempo y forma. Y en caso afirmativo le indiquemos cómo organizarla. Se solicita utilizando
redes de flujos dar una solución al problema.
"""
class Grafo:
    def __init__(self):
        pass
    
def transformar_problema(M, tareas):
    grafo = Grafo()
    s = "s"
    t = "t"
    max_tiempo = max(tarea[2] for tarea in tareas)
    for i in range(max_tiempo):
        # Pensamos a los intervalos de tiempo como (i-1, i) => cubre hasta i
        grafo.agregar_arista(s, i+1, M) 
        for tarea in tareas:
            # Añadimos arista si ese intervalo entra en la tarea
            if i >= tarea[1] and i+1 <= tarea[2]:
                grafo.agregar_arista(i+1, tarea, 1)

    for tarea in tareas:
        grafo.agregar_arista(tarea, t, tarea[0])            
    return grafo

def edmons_karp(grafo, s, t):
    return
# Tareas de la forma (di, inicio,)
def taller_metalurgico(M, tareas):
    grafo_transformado = transformar_problema(M, tareas)
    # Aca ya tenemos el problema transformado, sabemos que se resolvio el problema
    # si y solo flujo_max == sum(d_i) de cada tarea_i
    
    demanda_total = sum(tarea[0] for tarea in tareas)
    flujo = edmons_karp(grafo_transformado, "s", "t")
    
    return flujo == demanda_total
    
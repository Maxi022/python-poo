"""
Un decorador en Python es una función que permite añadir funcionalidad adicional a otra función o método sin modificar su código. 
Los decoradores son muy útiles para reutilizar código, aplicar validaciones, o realizar acciones antes o después de la ejecución de una función.
"""

"""
    Ejemplo Básico de un Decorador
    Vamos a crear un decorador que mida el tiempo que tarda una función en ejecutarse:
"""
import time

def mide_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

"""
    'mide_tiempo' es el decorador que toma una función func como argumento.
    Dentro de 'mide_tiempo', definimos 'wrapper', una función interna que envuelve la función original.
    'wrapper' toma los mismos argumentos que la función original (*args y **kwargs).
    'wrapper' mide el tiempo antes y después de llamar a la función original func, y luego imprime el tiempo de ejecución.
    Finalmente, 'wrapper' devuelve el resultado de la función original.
"""

@mide_tiempo
def suma(a, b):
    time.sleep(1)  # Simulando un retraso
    return a + b

@mide_tiempo
def factorial(n):
    time.sleep(1)  # Simulando un retraso
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
"""
    La línea '@mide_tiempo' aplica el decorador mide_tiempo a la función suma.
    Esto es equivalente a escribir suma = mide_tiempo(suma), pero es más limpio y legible.
"""

resultado_suma = suma(5, 3)
print(f"Resultado de suma: {resultado_suma}")

"""
    Cuando llamas a suma(5, 3), en realidad estás llamando a la función wrapper dentro del decorador.
    El decorador mide el tiempo de ejecución de suma y luego imprime el tiempo tomado.
"""

"""
Esto demuestra cómo el decorador mide_tiempo añade funcionalidad adicional (medir el tiempo de ejecución) a las funciones suma y factorial sin modificar su código.
"""
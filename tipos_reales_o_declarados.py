"""
Tipos Reales o Declarados
Tipo Declarado:
El tipo declarado es el tipo que se especifica en el código, generalmente usando anotaciones de tipo.
"""

def sumar(a: int, b: int) -> int:
    return a + b

"""
Aquí, a y b están declarados como int.
"""

"""
Tipo Real:
El tipo real es el tipo que el objeto realmente tiene en tiempo de ejecución.
"""

def sumar(a: int, b: int) -> int:
    return a + b

print(sumar(1, 2))       # Tipo real: int (esperado)
print(sumar(1.5, 2.5))   # Tipo real: float (no esperado, pero Python lo permite)

"""
Punto Clave:
En Python, las anotaciones de tipo son solo sugerencias y no son estrictamente obligatorias en tiempo de ejecución. El tipo real del objeto puede diferir del tipo declarado.
"""

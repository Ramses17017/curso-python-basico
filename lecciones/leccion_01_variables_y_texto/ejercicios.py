"""Lección 1: variables, texto y números.

Completa las seis funciones en orden. Cada una tiene su guía paso a paso
en el README de esta carpeta.

Para evaluarte:

    pytest lecciones/leccion_01_variables_y_texto

Para evaluar un solo ejercicio, por ejemplo el 3:

    pytest lecciones/leccion_01_variables_y_texto -k ejercicio_3
"""


def nombre_completo(nombre, apellido):
    """Une nombre y apellido con un espacio, cada uno con mayúscula inicial.

    Ejemplo:
        >>> nombre_completo("ana", "lópez")
        'Ana López'
    """
    # Borra la línea de abajo y escribe tu código en su lugar.
    return f"{nombre} {apellido}".title()


def limpiar_texto(texto):
    """Quita los espacios de los extremos y pasa todo a minúsculas.

    Ejemplo:
        >>> limpiar_texto("  Monterrey ")
        'monterrey'
    """
    # Borra la línea de abajo y escribe tu código en su lugar.
    return texto.strip().lower()


def precio_a_numero(texto):
    """Convierte un precio escrito como texto en un número con decimales.

    El texto puede traer espacios, el símbolo de pesos y comas de miles.

    Ejemplo:
        >>> precio_a_numero(" $1,250.50 ")
        1250.5
    """
    # Borra la línea de abajo y escribe tu código en su lugar.
    precio = float(texto.replace("$", "").replace(",", ""))
    return precio


def calcular_total(cantidad, precio_unitario):
    """Multiplica cantidad por precio unitario y redondea a dos decimales.

    Ejemplo:
        >>> calcular_total(3, 19.99)
        59.97
    """
    # Borra la línea de abajo y escribe tu código en su lugar.
    total_m = round(cantidad * precio_unitario, 2)
    return total_m


def aplicar_descuento(total, porcentaje):
    """Resta al total el porcentaje indicado y redondea a dos decimales.

    El porcentaje llega como número entre 0 y 100.

    Ejemplo:
        >>> aplicar_descuento(200, 15)
        170.0
    """
    # Borra la línea de abajo y escribe tu código en su lugar.
    descuento = total * porcentaje
    descuento_real = descuento / 100
    precio_f = round(total - descuento_real, 2)
    return  precio_f


def formatear_importe(importe):
    """Devuelve el importe como texto, con comas de miles, dos decimales y moneda.

    Ejemplo:
        >>> formatear_importe(1250.5)
        '$1,250.50 MXN'
    """
    # Borra la línea de abajo y escribe tu código en su lugar.
    return f"${importe:,.2f} MXN"

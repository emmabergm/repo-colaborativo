

def registrar_habitos():
    """
    Permite ingresar actividades realizadas durante el día.

    Returns
    -------
    list
        Lista con las actividades ingresadas por el usuario.
    """

  
       habitos= []
       seguir="si"
       
       while seguir== "si":
           actividad= input ("ingrese una actividad: ")
           habitos.append(actividad)
           
           seguir= input ("¿deseas agregar otra actividad? (si/no)")
       
       return habitos 
       

def analizar_habitos(lista):
    """
    Analiza cuántas veces aparece cada actividad.

    Parameters
    ----------
    lista : list
        Lista de actividades ingresadas.

    Returns
    -------
    dict
        Diccionario con el conteo de actividades.
    """

    conteo = {}

    for actividad in lista:
        if actividad in conteo:
            conteo[actividad] += 1
        else:
            conteo[actividad] = 1

    return conteo

import funciones_habitos

lista = funciones_habitos.registrar_habitos()

resultado = funciones_habitos.analizar_habitos(lista)

print("Resumen de actividades: ")

for actividad, cantidad in resultado.items():
    print(actividad, ":", cantidad)
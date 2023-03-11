# Pedir información de la asignatura al usuario
nombre_asignatura = input("\nIngrese el nombre de la asignatura: ")
nota = float(input("Ingrese su nota: "))
creditos = int(input("Ingrese el número de créditos: "))

# Crear un diccionario para almacenar la información
asignatura = {
  "nombre": nombre_asignatura,
  "nota": nota,
  "creditos": creditos
}

print(f"El estudiante tiene un promedio de {nota} de la asignatura {nombre_asignatura} con {creditos} creditos\n")


""" # Pedir al usuario si quiere ingresar otra asignatura
otra_asignatura = input("¿Desea ingresar información sobre otra asignatura? (s/n): ")

# Inicializar las variables para calcular el promedio ponderado
promedio = 0
total_creditos = 0

# Mientras el usuario quiera ingresar otra asignatura
while otra_asignatura == "s":
  # Pedir información de la siguiente asignatura
  nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
  nota = float(input("Ingrese su nota: "))
  creditos = int(input("Ingrese el número de créditos: "))

  # Agregar la información al diccionario
  asignatura_actual = {
    "nombre": nombre_asignatura,
    "nota": nota,
    "creditos": creditos
  }
  asignatura["asignatura_actual"] = asignatura_actual

  # Sumar los créditos y las notas ponderadas
  total_creditos += creditos
  promedio += nota * creditos

  # Preguntar si quiere ingresar otra asignatura
  otra_asignatura = input("¿Desea ingresar información sobre otra asignatura? (s/n): ")

# Calcular el promedio ponderado
promedio /= total_creditos

# Mostrar la información del diccionario y el promedio
print("Información de las asignaturas:")
for asignatura_actual in asignatura.values():
  print("- Nombre:", asignatura_actual["nombre"])
  print("  Nota:", asignatura_actual["nota"])
  print("  Créditos:", asignatura_actual["creditos"])

print("El estudiante tiene un promedio de:", promedio) """
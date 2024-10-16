#Escribe un programa que determine si una nota numérica es "Aprobado" o
#"Reprobado" usando if
nota= int(input("ingrese su calificacion:") )
#Solicita al usuario una calificación y determina si la nota es aprobatoria
#(>= 60) o reprobatoria (<60).
if (nota >=60):
 print(f"nota aprovada ")
else:
 print(f"su nota esta reprobada ")
#Miguel Castillo Ordaz
#Calcular el porcentaje de hombres y mujeres inscritos en clase.

Análisis:
E: numero de hombres y mujeres inscritos
S: número total de alumnos, porcentaje de mujeres, porcentaje de hombres.
E/S:  sumar número de hombres y número de mujeres inscritos, dividir número de hombres y mujeres entre diez por cien por ciento.

Algoritmo:
nh= int(input("Teclea número de hombres inscritos: "))
nm= int(input("Túmero de mujeres inscritas: "))
suma: nombres inscritos + mujeres inscritas
porcentajeuno: nh/10*100%
porcentajedos: nm/10*100%
print(“Mujeres inscritas (nm) Hombres inscritos (nh) Total de inscritos: %d Porcentaje de mujeres: %02d1d Porcentaje de hombres: %03d1d”) % (suma,porcentajeuno,porcentajedos)

PERSONAS = LEER_PERSONAS()
mayores_edad = 0
menores_edad = 0
hombres_mayores_edad = 0
mujeres_menores_edad = 0
mujeres = 0

for PERSONA in PERSONAS:
    print(PERSONA[0])
    if PERSONA[1] > 17:
        mayores_edad += 1
        if PERSONA[0].upper() == 'MASCULINO' or PERSONA[0].upper() == 'H' or PERSONA[0].upper() == 'HOMBRE':
            hombres_mayores_edad += 1
    else:
        menores_edad += 1
        if PERSONA[0].upper() == 'FEMENINO' or PERSONA[0].upper() == 'M' or PERSONA[0].upper() == 'MUJER':
            mujeres_menores_edad += 1
    if PERSONA[0].upper() == 'FEMENINO' or PERSONA[0].upper() == 'M' or PERSONA[0].upper() == 'MUJER':
        mujeres += 1
print(mujeres)
porcentaje_mujeres = (mujeres / 50) * 100
porcentaje_mayores_edad = (mayores_edad / 50) * 100

print(f"""Mayores edad: {mayores_edad}
menores edad: {menores_edad}
Hombres mayores de edad: {hombres_mayores_edad}
Mujeres menores de edad: {mujeres_menores_edad}
Porcetaje de mayores de edad: {porcentaje_mayores_edad}%
Porcentaje de mujeres: {porcentaje_mujeres}%""")

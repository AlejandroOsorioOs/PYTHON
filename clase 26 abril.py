SUELDOS= []
for X in range (5):
    VALOR= int (input("INGRESE EL SUELDO: "))
    SUELDOS.append (VALOR)
print ("LISTA SIN ORDENAR ")
print (SUELDOS)

for K in range (4):
    for X in range (4):
        if SUELDOS [X] > SUELDOS [X+1]:
            AUX= SUELDOS[X]
            SUELDOS[X]=SUELDOS[X+1]
            SUELDOS [X+1]=AUX
print("LISTA ORDENADA")
print(SUELDOS)
#ENUNCIADO
# HALLAR EL AREA Y EL PERIMETRO DE UN CUADRADO LEYENDO POR TECLADO EL VALOR DE SU LADO
#DESARROLLADO POR JUAN ALEJANDRO OSORIO OSPINA
#FECHA 08.03.2023
# VERSION 1


#ENTRADA
print ("")
v_lado = input("POR FAVOR DIGITE EL VALOR DEL LADO: ") #LECTURA
v_lado = int (v_lado) #CONVERSION DE TEXTO A ENTERO

print ("")
#PROCESOS
v_area = v_lado * v_lado #CALCULAR EL AREA DEL CUADRADO
v_perimetro = v_lado * 4

#SALIDAS
print ("EL AREA DEL CUADRADO ES: ", v_area)
print ("")
print ("EL PERIMETRO DEL CUADRADO ES: ", v_perimetro)
print ("")
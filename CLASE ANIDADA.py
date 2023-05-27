# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# DOCUMENTACION
	# ENUNCIADO: Leer o capturar dos numeros por teclado, identificar el mayor e imprimirlo
	# DESARROLLADO POR: Juan Alejandro Osorio Ospina
	# VERSION: 1.0
	# FECHA 28.02.2023
	# DECLARACION DE VARIABLES
	v_numuno = int()
	v_numdos = int()
	# INICIALIZACION
	v_numuno = 0
	v_numdos = 0
	# LECTURA DE DATOS
	print "DIGITE EL PRIMER NUMERO: "
	v_numuno = int(raw_input())
	print "DIGITE EL SEGUNDO NUMERO: "
	v_numdos = int(raw_input())
	# PROCESOS
	if v_numuno>v_numdos:
		print "EL NUMERO MAYOR ES : ",v_numuno
	else:
		if v_numuno<v_numdos:
			print "EL NUMERO MAYOR ES : ",v_numdos
		else:
			print "LOS NUMEROS DIGITADOS SON IGUALES"


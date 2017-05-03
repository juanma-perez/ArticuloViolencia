#Functions that use logic of python 

def getArray(caracter,linea):
	return linea.split(caracter)

def addValue(diccionario,nombre,valor):
	diccionario[nombre]=valor
	return diccionario

def getValue(arreglo,posicion):
	try:
		return arreglo[posicion-1]
	except:
		raise Exception("The array " + str(arreglo) + " has no position " + str(posicion))

def getSubArray(arreglo,posicionIni, posicionFin):
	try:
		return arreglo[posicionIni-1:posicionFin]
	except:
		raise Exception("The array " + str(arreglo) + " has no positions " + str(posicion) + " "+ str(posicionFin))

def removeSubString(string, sub):
	return string.strip(sub)

def deleteSubString(string, sub):
	return string.remove(sub)
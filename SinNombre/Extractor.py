# -*- coding: utf-8 -*-
import Charmer 
from FileManager import FileManager


def obtenerEstructura(arreglo):
	diccionario = {}
	#AsesinatosSelectivos 1981-2012
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Lugar",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Tipo de implicados",Charmer.getSubArray(arreglo,7,8))
	diccionario =  Charmer.addValue(diccionario,"Cantidad de victimas",Charmer.getValue(arreglo,9))
	diccionario =  Charmer.addValue(diccionario,"Fuente",Charmer.getValue(arreglo,10))"""
	#AtaquesPoblaciones 1988-2012
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Lugar",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Hecho",Charmer.getValue(arreglo,7))
	diccionario =  Charmer.addValue(diccionario,"Tipo de arma",Charmer.getValue(arreglo,8))
	diccionario =  Charmer.addValue(diccionario,"Tipo implicado",Charmer.getValue(arreglo,9))
	temp = {}
	temp =  Charmer.addValue(temp,"Victimas fatales",Charmer.getValue(arreglo,10))
	temp =  Charmer.addValue(temp,"Combatientes",Charmer.getValue(arreglo,11))
	temp =  Charmer.addValue(temp,"Población civil",Charmer.getValue(arreglo,12))
	temp =  Charmer.addValue(temp,"Lesionados",Charmer.getValue(arreglo,13))
	diccionario =  Charmer.addValue(diccionario,"Cantidad de personas",temp)
	diccionario =  Charmer.addValue(diccionario,"fuente",Charmer.getValue(arreglo,14))"""
	#AtentadosTerroristas1988-2012
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Lugar",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Tipo implicado",Charmer.getValue(arreglo,7))
	temp = {}
	temp =  Charmer.addValue(temp,"Victimas fatales",Charmer.getValue(arreglo,8))
	temp =  Charmer.addValue(temp,"Lesionados",Charmer.getValue(arreglo,9))
	diccionario =  Charmer.addValue(diccionario,"Cantidad de personas",temp)
	diccionario =  Charmer.addValue(diccionario,"fuente",Charmer.getValue(arreglo,10))"""
	#CivilesMuertosAccionesBelicas1988-2012
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Lugar",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Tipo de hecho",Charmer.getValue(arreglo,7))
	diccionario =  Charmer.addValue(diccionario,"Tipo de implicado",Charmer.getValue(arreglo,8))
	temp = {}
	temp =  Charmer.addValue(temp,"Victimas",Charmer.getValue(arreglo,9))
	temp =  Charmer.addValue(temp,"Combatientes",Charmer.getValue(arreglo,10))
	temp =  Charmer.addValue(temp,"Población civil",Charmer.getValue(arreglo,11))
	diccionario =  Charmer.addValue(diccionario,"Cantidad de personas",temp)
	diccionario =  Charmer.addValue(diccionario,"fuente",Charmer.getValue(arreglo,12))"""
	#DanoBienesCiviles1988-2012
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Lugar",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Tipo de hecho",Charmer.getValue(arreglo,7))
	diccionario =  Charmer.addValue(diccionario,"Tipo de bien",Charmer.getValue(arreglo,8))
	diccionario =  Charmer.addValue(diccionario,"Tipo de implicados",Charmer.getSubArray(arreglo,9,10))
	temp = {}
	temp =  Charmer.addValue(temp,"Victimas fatales",Charmer.getValue(arreglo,11))
	temp =  Charmer.addValue(temp,"Lesionados",Charmer.getValue(arreglo,12))
	diccionario =  Charmer.addValue(diccionario,"Cantidad de personas",temp)
	diccionario =  Charmer.addValue(diccionario,"fuente",Charmer.getValue(arreglo,13))"""
	#MAP1982-2013
	"""diccionario =  Charmer.addValue(diccionario,"Tipo de evento",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Corregimiento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Evento",Charmer.getValue(arreglo,7))
	diccionario =  Charmer.addValue(diccionario,"COD_DANE_MUNI",Charmer.getValue(arreglo,8))
	diccionario =  Charmer.addValue(diccionario,"COD_DANE_DEPTO",Charmer.getValue(arreglo,9))
	diccionario =  Charmer.addValue(diccionario,"Tipo de lugar",Charmer.getValue(arreglo,10))
	diccionario =  Charmer.addValue(diccionario,"Tipo de area",Charmer.getValue(arreglo,11))"""
	#Masacres1980-2012
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))
	diccionario =  Charmer.addValue(diccionario,"Lugar",Charmer.getValue(arreglo,6))
	diccionario =  Charmer.addValue(diccionario,"Tipo implicado",Charmer.getValue(arreglo,7))
	diccionario =  Charmer.addValue(diccionario,"Cantidad de victimas",Charmer.getValue(arreglo,8))
	diccionario =  Charmer.addValue(diccionario,"Fuente",Charmer.getValue(arreglo,9))"""
	#SecuestrosColombia1970-2010
	"""diccionario =  Charmer.addValue(diccionario,"Dia",Charmer.getValue(arreglo,1))
	diccionario =  Charmer.addValue(diccionario,"Mes",Charmer.getValue(arreglo,2))
	diccionario =  Charmer.addValue(diccionario,"Año",Charmer.getValue(arreglo,3))
	diccionario =  Charmer.addValue(diccionario,"Departamento",Charmer.getValue(arreglo,4))
	diccionario =  Charmer.addValue(diccionario,"Municipio",Charmer.getValue(arreglo,5))	
	diccionario =  Charmer.addValue(diccionario,"Lugar de Ocurrencia",Charmer.getValue(arreglo,6))	
	diccionario =  Charmer.addValue(diccionario,"Modalidad",Charmer.getValue(arreglo,7))	
	diccionario =  Charmer.addValue(diccionario,"Motivo Argumentado",Charmer.getValue(arreglo,8))	
	diccionario =  Charmer.addValue(diccionario,"Autor Presunto",Charmer.getValue(arreglo,9))	
	diccionario =  Charmer.addValue(diccionario,"Autor Confirmado",Charmer.getValue(arreglo,10))	
	diccionario =  Charmer.addValue(diccionario,"Exigencia",Charmer.getValue(arreglo,11))	
	diccionario =  Charmer.addValue(diccionario,"Tipo de Desenlace",Charmer.getValue(arreglo,12))	
	diccionario =  Charmer.addValue(diccionario,"Primera Fuente",Charmer.getValue(arreglo,13))"""
	return diccionario

def generarJSON(file):
	fileManager = FileManager()
	with fileManager.readFile(file) as f:
		for line in f:
			try:
				fileManager.writeFileJSON(Charmer.removeSubString(file,".txt"),obtenerEstructura(Charmer.getArray('	',line.replace("\n",""))))	
			except Exception as error:
				fileManager.recordError(error)
			

generarJSON("Masacres1980-2012.txt")
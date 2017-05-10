# -*- coding: utf-8 -*-

import json 
import redis
import Charmer
import prubaneo4j
from FileManager import FileManager
fileManager = FileManager()
ontologia = fileManager.leerJson("ontologia.json")

def sendRedis(callback):
	redisClient = redis.StrictRedis(host='localhost', port=6379, db=0) 	
	return callback(redisClient)	

def getSet(query):
	def function(redisClient):
		return redisClient.smembers(query)
	return sendRedis(function)

def get(query):
	def function(redisClient):
		return redisClient.get(query)
	return sendRedis(function)

def crearStructure():
	dic = {}
	def function(redisClient):
		for nodo in redisClient.keys("nodes:*"):
			temp = {} 
			for atributo in getSet(nodo):
				temp[atributo]= ""
			dic[nodo[6:]]=temp
		return dic
	return sendRedis(function)
structure = crearStructure()

def compareSinonimo(palabra):
	sinonimo = get("synonymous:" + palabra)
	if sinonimo != None:
		return sinonimo
	else:
		return palabra

def synonymous_atr():
	def function(redisClient):
		dic = {}
		for item in redisClient.keys("synonymous_atr:*"):
			dic[item.replace("synonymous_atr:","")]=get(item)
		return dic
	return sendRedis(function)

synonymous = synonymous_atr()

def fillStructure(json, t_hecho, id):
	for key in json.keys():
		if synonymous.has_key(key.encode("utf-8")):
			arr = Charmer.getArray(":",synonymous[key.encode("utf-8")].encode("utf-8"))
			if len(arr) == 1:
				structure[arr[0]]= json[key]
			if len(arr) == 2:
				structure[arr[0]][arr[1]]= json[key]
		structure["Event"]["t_event"] = t_hecho
		structure["Event"]["id"] = id

def readFile(file, t_hecho):
	with fileManager.readFileGenerated(file) as file:
		cont = 1
		for line in file:
			if cont == 15:
				break;	
			if cont%100 == 0:
				print cont 		
			fillStructure(json.loads(line),t_hecho, cont)
			prubaneo4j.cargarEstructura(structure)
			cont+=1

readFile("MasacresFinal.json", "masacre")


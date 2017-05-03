# -*- coding: utf-8 -*-

import json 
import redis
import Charmer
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
		for nodo in redisClient.keys("nodos:*"):
			temp = {} 
			for atributo in getSet(nodo):
				temp[atributo]= ""
			dic[nodo[6:]]=temp
		return dic
	return sendRedis(function)
structure = crearStructure()

def fillStructure(json):
	for key in json.keys():
		if get("sinonimos_atr:" + key) != None:
			arr = Charmer.getArray(":",get("sinonimos_atr:" + key))
			if len(arr) == 1:
				structure[arr[0]]= json[key]
			if len(arr) == 2:
				structure[arr[0]][arr[1]]= json[key]
		
def readFile(file):
	with fileManager.readFileGenerated(file) as file:
		for line in file:
			fillStructure(json.loads(line))
			print structure

readFile("Masacres1980-2012.json")

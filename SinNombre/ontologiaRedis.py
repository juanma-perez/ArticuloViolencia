# -*- coding: utf-8 -*-
import json 
import redis
import Charmer
from FileManager import FileManager

fileManager = FileManager()
ontologia = fileManager.leerJson("ontologia1.json")

def sendRedis(callback):
	redisClient = redis.StrictRedis(host='localhost', port=6379, db=0) 	
	#print("Conectandose a redis")
	#print("Se envío mensaje a redis")
	return callback(redisClient)	

def testRedis(redisClient):
	print(redisClient.get('test'))

def addSet(root, json):
	for subRoot in json:
		clave = root + ':' + subRoot
		for i in range(0,len(json[subRoot])):				
			print("sadd "+clave.encode("utf-8")+" " +json[subRoot][i].encode("utf-8"))
			def function(redisClient):
				return "Registros insertados: " + str(redisClient.sadd(clave,json[subRoot][i].encode("utf-8")))
			print(sendRedis(function))
def set(root, json):
	for subRoot in json:
		clave = root + ':' + subRoot
		for i in range(0,len(json[subRoot])):				
			print("set "+clave.encode("utf-8")+" " +json[subRoot][i].encode("utf-8"))
			def function(redisClient):
				return "Registros insertados: " + str(redisClient.set(clave,json[subRoot][i].encode("utf-8")))
			print(sendRedis(function))

def getSet(query):
	def function(redisClient):
		return redisClient.smembers(query)
	return sendRedis(function)

def addString(root,json):
        for subRoot in json:
                clave=subRoot
                print("set "+clave.encode("utf-8")+" " +json[subRoot].encode("utf-8"))
                def function(redisClient):
                        return "Registros insertados: " + str(redisClient.set(clave,json[subRoot].encode("utf-8")))
                print(sendRedis(function))

def cargarOntologia():
	addSet("nodos", ontologia["nodos"]);		
	addSet("relaciones", ontologia["relaciones"]);
	addString("sinonimos", ontologia["sinonimos"]);
	set("sinonimos_atr", ontologia["sinonimos_atr"]);

cargarOntologia()

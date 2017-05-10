# -*- coding: utf-8 -*-
import json 
import redis
import Charmer
from FileManager import FileManager

fileManager = FileManager()
ontologia = fileManager.leerJson("ontologia.json")

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
def cleanOnotology():
	def function(redisClient):
		redisClient.flushall()
	sendRedis(function)
def cargarOntologia():
	print cleanOnotology()
	addSet("nodes", ontologia["nodes"]);		
	addSet("relations", ontologia["relations"]);
	addString("synonymous", ontologia["synonymous"]);
	set("synonymous_atr", ontologia["synonymous_atr"]);

cargarOntologia()
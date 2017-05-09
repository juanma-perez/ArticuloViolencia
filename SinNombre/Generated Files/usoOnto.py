import json
import redis

def sendRedis(callback):
	redisClient = redis.StrictRedis(host='localhost', port=6379, db=0) 	
	return callback(redisClient)
    
def Reemplazar(archivo):
    array=[]
    arrayResult=[]
    for line in open(archivo, 'r'):
        linejson = json.loads(line)
        resultD= buscarRedis(linejson['Departamento'].lower().encode("UTF-8"))
        resultM= buscarRedis(linejson['Municipio'].lower().encode("UTF-8"))
        resultT= buscarRedis(linejson['Tipo implicado'].lower().encode("UTF-8"))
        if resultT:
            linejson['Tipo implicado']=resultD
        if resultD:
            linejson['Departamento']=resultD
        if resultM:
            linejson['Municipio']=resultM
        ActualizarCampos(linejson)
        
def ActualizarCampos(doc):
    with open('ArchivoSalida.json', 'a') as f:
        json.dump(doc,f)
        f.write("\n")

def buscarRedis(clave):
    def function(redisClient):
        return redisClient.get(clave)
    return sendRedis(function)


file='ArchivoEntrada.json'

ReemplazarOrg(file)


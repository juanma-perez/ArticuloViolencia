import json
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "8112"))

def cargarDatos():
    session = driver.session()
    array=[]
    for line in open('DeptosMuniColombia.json', 'r'):
        array.append(json.loads(line))
    for doc in array:
        try:
            session.run("CREATE (d:Lugar {n_lugar:{depto},t_lugar:'Departamento'})",
                        {"depto":doc['Nombre']})
            print "Creo Departamento "+doc['Nombre']
            if(doc['Municipios']):
                for item in doc['Municipios']:
                    session.run("CREATE (m:Lugar {n_lugar:{muni},t_lugar:'Municipio'})",{"muni":item})
                    print "Creo municipio "+item                    
        except:
            print "este Departamento no tiene municipios"
    session.close()
    
def crearRelaciones():
    session = driver.session()
    array=[]
    for line in open('DeptosMuniColombia.json', 'r'):
        array.append(json.loads(line))
    for doc in array:
        try:
            if(doc.has_key('Municipios')):
                for item in doc['Municipios']:
                    print "Departamento "+ doc['Nombre']+" Municipio "+item
                    session.run("MATCH (d:Lugar {n_lugar:{depto}}) "+
                                "MATCH (m:Lugar {n_lugar:{muni}}) "+
                                "MERGE (d)-[r:SeConforma]->(m)",
                                {"muni":item,"depto":doc['Nombre']})
        except:
            print ":)"
        
    session.close()

def borrarDatos():
    try:
        session.run("MATCH (n) DETACH DELETE n")
        print "Borrando datos..."
    except:
            print "Unexpected error to Delete"

#borrarDatos()
#cargarDatos()
#crearRelaciones()

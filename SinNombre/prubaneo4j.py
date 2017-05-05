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
                    print item.encode('UTF-8')
                    session.run("CREATE (m:Lugar {n_lugar:{muni},t_lugar:'Municipio'})",{"muni":item})
                    session.run("MATCH (u:Lugar {n_lugar:{dept}}) "+
                                "MATCH (v:Lugar {n_lugar:{mun}}) "+
                                "MERGE (u)-[r:SeConforma]->(v)",
                                {"mun":item,"dept":doc['Nombre']})                 
        except:
            print "este Departamento no tiene municipios"
   

def borrarDatos():
    session = driver.session()
    try:
        session.run("MATCH (n) DETACH DELETE n")
        print "Borrando datos..."
        
    except:
            print "Unexpected error to Delete"

borrarDatos()
#cargarDatos()


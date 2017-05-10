import json
from neo4j.v1 import GraphDatabase, basic_auth
from tqdm import tqdm

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "8112"))

def cargarDatosDepto():
    session = driver.session()
    try:
        with open('DeptosMuniColombia.json', 'r') as f:
            print ("Inicia carga de Departamentos y municipios")
            lineas  = tqdm(f.readlines())
            for line in lineas:
                doc = json.loads(line)  
                session.run("CREATE (d:Site {n_site:{depto},t_site:'Departamento'})",
                            {"depto":doc['Nombre'].encode('UTF-8')})
                #print "Creo Departamento "+doc['Nombre']
                if(doc.has_key('Municipios')):
                    for item in doc['Municipios']:
                        #print item.encode('UTF-8')
                        session.run("CREATE (m:Site {n_site:{muni},t_site:'Municipio'})",{"muni":item.encode('UTF-8')})
                        session.run("MATCH (u:Site {n_site:{dept}}) "+
                                    "MATCH (v:Site {n_site:{mun}}) "+
                                    "MERGE (u)-[r:consist]->(v)",
                                    {"mun":item.encode('UTF-8'),"dept":doc['Nombre'].encode('UTF-8')})
                        """result = session.run("MATCH (u:Site {n_site:{dept}}) "+
                                             "MATCH (v:Site {n_site:{mun}}) RETURN u.n_site AS dept, v.n_site AS muni",
                                             {"mun":item.encode('UTF-8'),"dept":doc['Nombre'].encode('UTF-8')})"""
                        
                    """    for record in result:
                            straa = "%s %s" % (record["dept"], record["muni"]) + " Resultado de la insercion"
                            print(straa.encode('UTF-8'))"""

        print "Departamentos y municipios cargados"
    except:
        print "Error en la carga de departamentos y municipios"
   
org = []
def cargarEstructura(jestructure):
    session = driver.session()    
    #"dia_suceso","mes_suceso","a\u00F1o_sucesceso","sinopsis","t_hecho" in org:
    session.run("CREATE (suceso:Event {day_event:{day_event},month_event:{month_event},year_event:{year_event}, synopsis:{synopsis}, t_event:{t_event}, n_event:{n_event}, id:{id}})", jestructure["Event"])
    temp = jestructure["Organization"]["n_org"]
    temp = temp.replace("Guerrilla-","")
    temp = temp.replace("Guerrilla ","")
    otro = temp.split(" y ")
    for valor in otro:
        valor2 = valor.split("-")
        for item in valor2:
            if item in org:
                pass
            else:
                session.run("CREATE (organizacion:Organization {n_org:{n_org}})", {"n_org":item})
                org.append(item)    
            session.run("MATCH (s:Event {id:{id}})"+
                        "MATCH (o:Organization {n_org:{n_org}})"+
                        "MERGE (o)-[cau:cause]-> (s)",{"id":jestructure["Event"]["id"],"n_org":item.encode('UTF-8')})
    json = {"id":jestructure["Event"]["id"],"n_site":jestructure["Site"]["n_site"].encode('UTF-8')}    
    retorno2 = session.run("MATCH (exis:Site {n_site:{n_site}}) return exis.n_site AS retorno",{"n_site":jestructure["Site"]["n_site"]})  
    cont = 0
    for item in retorno2:
        cont += 1
    if cont == 0:
        print "entra"
        session.run("CREATE (m2:Site {n_site:{muni},t_site:'Municipio'})",{"muni":jestructure["Site"]["n_site"].encode('UTF-8')})
        session.run("MATCH (u2:Site {n_site:{dept}}) "+
                    "MATCH (v2:Site {n_site:{mun}}) "+
                    "MERGE (u2)-[r:consist]->(v2)",
                    {"mun":jestructure["Site"]["n_site"].encode('UTF-8'),"dept":jestructure["Site"]["up_level"].encode('UTF-8')})
    retorno = session.run("MATCH (s1:Event {id:{id}})"+
            "MATCH (l1:Site {n_site:{n_site}})"+
            "MERGE (s1)-[happ:happenedIn]-> (l1) return l1.n_site AS retorno",json)
    for item in retorno:
        cont += 1
    if cont == 0:
        print jestructure["Site"]
    
def borrarDatos():
    session = driver.session()
    try:
        print "Inicia la eliminacion de datos..."        
        session.run("MATCH (n) DETACH DELETE n")
        print "Datos eliminados"        
    except:
            print "Unexpected error to Delete"

borrarDatos()
cargarDatosDepto()
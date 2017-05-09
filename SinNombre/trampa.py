import json
from tqdm import tqdm
# -*- coding: utf-8 -*-
def hacerTrampa(file):
	with open('Generated Files/' + file, 'r') as f:
	    lineas  = tqdm(f.readlines())
	    dicDeptos = {}
	    dicMunicipios = {}
	    grupos = {}
	    for line in lineas:
	    	linejson = json.loads(line)
	    	if dicDeptos.has_key(linejson["Departamento"]):
	    		dicDeptos[linejson["Departamento"]] +=1
	    	else: 
	    		dicDeptos[linejson["Departamento"]] = 1
	    	if dicMunicipios.has_key(linejson["Municipio"]):
	    		dicMunicipios[linejson["Municipio"]] +=1
	    	else: 
	    		dicMunicipios[linejson["Municipio"]] = 1
	    	if grupos.has_key(linejson["Tipo implicado"]):
	    		grupos[linejson["Tipo implicado"]] +=1
	    	else: 
	    		grupos[linejson["Tipo implicado"]] = 1
	    print ("")
	    print ("Departamentos")
	    for key in dicDeptos: 
	    	print (key.encode('utf-8') + " = " +  str(dicDeptos[key]))
	    print ("")
	    print ("Municipios")
	    for key in dicMunicipios: 
	    	print (key.encode('utf-8') + " = " +  str(dicMunicipios[key]))
	    print ("")
	    print ("Grupos armados")
	    for key in grupos: 
	    	print (key.encode('utf-8') + " = " +  str(grupos[key]))

hacerTrampa("AtaquesPoblaciones1988-2012.json")
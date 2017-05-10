import json

# -*- coding: utf-8 -*-

def hacerTrampa():
	grupos = {}
	with open('Generated Files/' + "AtaquesPoblaciones1988-2012.json", 'r') as f:

	    lineas  = f.readlines()
	    for line in lineas:	    	
	    	linejson = json.loads(line)

	    	temp = linejson["Tipo implicado"]
	    	temp = temp.replace("Guerrilla-","")
	    	temp = temp.replace("Guerrilla ","")
	    	otro = temp.split(" y ")
	    	for valor in otro:
	    		if grupos.has_key(valor.strip()):
	    			grupos[valor.strip()] +=1
	    		else:
	    			grupos[valor.strip()] = 1

	with open('Generated Files/' + "AtentadosTerroristas1988-2012.json", 'r') as f:
	    lineas  = f.readlines()
	    for line in lineas:	    	
	    	linejson = json.loads(line)
	    	temp = linejson["Tipo implicado"]
	    	temp = temp.replace("Guerrilla-","")
	    	temp = temp.replace("Guerrilla ","")
	    	otro = temp.split(" y ")
	    	for valor in otro:
	    		if grupos.has_key(valor.strip()):
	    			grupos[valor.strip()] +=1
	    		else:
	    			grupos[valor.strip()] = 1

	with open('Generated Files/' + "CivilesMuertosAccionesBelicas1988-2012.json", 'r') as f:
	    lineas  = f.readlines()
	    for line in lineas:	    	
	    	linejson = json.loads(line)
	    	temp = linejson["Tipo implicado"]
	    	temp = temp.replace("Guerrilla-","")
	    	temp = temp.replace("Guerrilla ","")
	    	otro = temp.split(" y ")
	    	for valor in otro:
	    		valor2 = valor.split("-")
	    		for item in valor2:
		    		if grupos.has_key(item.strip()):
		    			grupos[item.strip()] +=1
		    		else:
		    			grupos[item.strip()] = 1

	with open('Generated Files/' + "Masacres1980-2012.json", 'r') as f:
	    lineas  = f.readlines()
	    for line in lineas:	    	
	    	linejson = json.loads(line)
	    	temp = linejson["Tipo implicado"]
	    	temp = temp.replace("Guerrilla-","")
	    	temp = temp.replace("Guerrilla ","")
	    	otro = temp.split(" y ")
	    	for valor in otro:
	    		valor2 = valor.split("-")
	    		for item in valor2:
		    		if grupos.has_key(item.strip()):
		    			grupos[item.strip()] +=1
		    		else:
		    			grupos[item.strip()] = 1
	return grupos
	   



other = hacerTrampa()
print ("")
print ("Grupos armados")
for key in other: 
	print (key.encode('utf-8') + " = " +  str(other[key]))
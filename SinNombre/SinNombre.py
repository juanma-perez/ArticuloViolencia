# -*- coding: utf-8 -*-
import Simulador
import Charmer 
from FileManager import FileManager
import json 

class SinNombreOntologia():
	def suceso(self):
		return {u"Dia":"",u"Mes":"",u"A\u00f1o":""} 

	def lugar(self):
		return {u"Nivel":u"Departamento",u"Nombre":u""}

	def __init__(self, jsonLine):
		self.jsonLine = jsonLine
		self.fileManager = FileManager()
		self.structure = {}
		try:
			with self.fileManager.readFile("structure.json") as z:
				self.structure = json.loads(z.read().replace('\n', ''))
		except Exception as e:
			self.fileManager.recordError("Couldn't load the structures file ")
		self.clear()
	
	def clear(self):
		self.suc = self.suceso()
		self.depto = self.lugar()
		self.municipio = self.lugar()

	def process(self,case,value):
		if case == "Dia": 
			self.suc = Charmer.addValue(self.suc,"Dia",value)
		elif case == "Mes":
			self.suc = Charmer.addValue(self.suc,"Mes",value)
		elif case == u"A\u00f1o":
			self.suc = Charmer.addValue(self.suc,u"A\u00f1o",value)
		elif case == "Departamento":
			self.depto = Charmer.addValue(self.depto,"Nombre",value)


	def fillStructure(self):
		try:
			register=json.loads(self.jsonLine)
			for reg in register:
				if self.structure.has_key(reg):
					self.process(reg,register[reg])
		except Exception as error:
			self.fileManager.recordError(error)


fileManager = FileManager()
file = "prueba.json"
with fileManager.readFile(file) as f:
	for line in f:
		a = SinNombreOntologia(line)
		a.fillStructure()
		print "Suceso"
		for thing in a.suc:
			print "	" + thing.encode("utf-8") + ": " + a.suc[thing].encode("utf-8")
		print "Lugar"
		for site in a.depto:
			print "	" + site.encode("utf-8") + ": " + a.depto[site].encode("utf-8")
		print ""
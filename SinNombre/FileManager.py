# -*- coding: utf-8 -*-
import json 
import time

class FileManager():
	def __init__(self):
		try:      
			with open("config.json",'r') as c:#Open the file 
				self.path = json.load(c)
		except IOError:
			self.recordError("The configuration file no exists")
	
	def recordError(self,error):
		try:      
			with open(self.path[u"generatedFilePath"] + self.path[u"logFile"],'a') as g:#Open the file 
				g.write("--------------------------------------------------------\n")
				g.write(time.strftime("%x") + " " + time.strftime("%X") + "\n")
				g.write(error)
				g.write("\n")
		except IOError as error:
			open(self.path[u"generatedFilePath"] + self.path[u"logFile"],'w')
			self.recordError(error)
	
	def writeFileJSON(self,file, line):
		try:      
			with open(self.path["generatedFilePath"] + file + ".json",'a') as g:#Open the file 
				json.dump(line, g) 
				g.write("\n")
		except IOError:
			open(file,'w')
			self.writeFileJSON(self.path["generatedFilePath"] + file + ".json", line)
		except Exception as error:
			print error
			#self.recordError("Error: " + str(error))

	def writeFile(self,file, line):
		try:      
			with open(self.path["generatedFilePath"] + file ,'a') as g:#Open the file 
				g.write(line + "\n")
		except IOError:
			open(file,'w')
			self.writeFileJSON(self.path["generatedFilePath"] + file, line)
		except Exception as error:
			print error
			 #self.recordError("Error: " + error)

	def readFile(self, file):
		try:      
			return open(self.path["generatedFilePath"] + file,'r')
		except IOError:
			self.recordError("No se puede leer el archivo: " + file)

	def readFileGenerated(self, file):
		try:      
			return open(self.path["generatedFilePath"] + file,'r')
		except IOError:
			self.recordError("No se puede leer el archivo: " + file)

	def leerJson(self, file):
		try:
			with open(file) as data_file:
				return json.load(data_file)
		except IOError:
			self.recordError("No se puede leer el archivo JSON: " + file)

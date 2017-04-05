# -*- coding: utf-8 -*-
import json 


class FileManager():
	def __init__(self):
		try:      
			with open("config.json",'r') as c:#Open the file 
				self.path = json.load(c)
		except IOError:
			self.recordError("The configuration file no exists")
	
	def recordError(self,error):
		try:      
			with open(self.path["generatedFilePath"] + file + ".log",'w') as g:#Open the file 
				g.write(error)
		except IOError as error:
			with open(self.path["generatedFilePath"] + file + ".log",'a') 
			print error
	
	
	def writeFileJSON(self,file, line):
		try:      
			with open(self.path["generatedFilePath"] + file + ".json",'a') as g:#Open the file 
				json.dump(line, g) 
				g.write("\n")
		except IOError:
			open(file,'w')
			self.writeFileJSON(self.path["generatedFilePath"] + file + ".json", line)
		except Exception as error:
			self.recordError("Error: " + error)

	def readFile(self, file):
		try:      
			return open(self.path["filePath"] + file,'r')
		except IOError:
			self.recordError("No se puede leer el archivo: " + file)
		
from fileReader import FileReader

class Worker:
	
	def __init__( self ):
		
		self.empList = []
		
	def getFileContent( self ):
		
		self.empList = FileReader().reading()
		
	def getVacCount( self ):
		
		counter = 0
		for emp in self.empList:
			
			if( emp.city == "Vác" ):
				
				counter += 1
		
		print( counter )
		
worker = Worker()
worker.getFileContent()
worker.getVacCount()

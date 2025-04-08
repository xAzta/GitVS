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
		
		print( "Váciak létszáma: ", counter )

	def morSalaryAvg( self ):
		
		salarySum = 0
		counter = 0

		for emp in self.empList:

			if( emp.city == "Mór" ):

				counter += 1
				salary += int( emp.salary )

		salaryAvg = salarySum / counter

		print( "Móri dolgozók fizetés átlaga: ", salaryAvg )

	def getCsomorSalarySum( self ):

		salarySum = 0

		for emp in self.empList:

			if( emp.city == "Csömör" ):

				salarySum += int( emp.salary )

		file = open( "csomor.txt", "w", encoding="utf8")

		file.write( "Csömöri dolgozók fizetése: \n")
		file.write( str( salarySum ))

		file.close()

		print( "Csömri dolgozók fizetése: ", salarySum )
	
		
worker = Worker()
worker.getFileContent()
worker.getVacCount()
worker.morSalaryAvg()
worker.getCsomorSalarySum()

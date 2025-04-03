from employee import Employee

class FileReader:

	def __init__( self ):
	
		pass
		
	def reading( self ):
		
		empList = []
		file = open( "employee.txt", "r", encoding="utf8");
		
		file.readline()
		row = file.readline()
		
		while( row ):
			
			rowSp = row.split( ":" )
			emp = employee.Employee( rowSp[0], rowSp[1], rowSp[2], rowSp[3], rowSp[4], rowSp[5], rowSp[6] )
			empList.append( emp )
			
			row = file.readline()
			
		return empList
			
		

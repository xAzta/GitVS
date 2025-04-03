class Worker:
	
	def __init__( self ):
		
		self.name = ""
		self.role = ""
		
	def getName( self ):
		
		return self.name
		
	def SetName( self, name ):
		
		self.name = name
		
	def getRole( self ):
		
		return self.role
		
	def setRole( self, role ):
		
		self.role = role


class Hr:
	
	pek = Worker()
	pek.SetName( "Pista" )
	pek.SetRole( "Pék" )
	
	print( pek.getName() )
	print( pek.getRole() )
	
Hr()

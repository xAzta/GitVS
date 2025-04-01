def read():
	
	print( "Beolvasas..." )
	file = open( "dolgozok100.txt", "r", encoding="utf8" ) 
	
	file.readline()
	row = file.readline()
	
	while( row ):
		
		print( row )
		row = file.readline()
		
read()

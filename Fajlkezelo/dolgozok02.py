def read():
	
	print( "Beolvasas..." )
	file = open( "dolgozok100.txt", "r", encoding="utf8" ) 
	
	file.readline()
	row = file.readline()
	
	while( row ):
		
		rowSp = row.split( ":" )
		print(rowSp[ 0 ])
		
		row = file.readline()
		
read()

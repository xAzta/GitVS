def read():
	
	workerlist = []
	file = open( "dolgozok100.txt", "r", encoding="utf8" )
	
	file.readline()
	row = file.readline()
	
	while( row ):
		
		rowSp = row.split( ":" )
		workerlist.append( rowSp )
		row = file.readline()
		
	print( workerlist )
		
read()

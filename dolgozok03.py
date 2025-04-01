def read():
	
	print ( "1. feladat fájl beolvasása" )
	workerlist = []
	file = open( "dolgozok100.txt", "r", encoding="utf8" )
	
	file.readline()
	row = file.readline()
	
	while( row ):
		
		rowSp = row.split( ":" )
		workerlist.append( rowSp )
		row = file.readline()
		
	print( "Sikeres beolasás." )
	
	return workerlist
	
def salaries():
	
	workerlist = read()
	print( "2 feladat fizetések összegzése." )
	
	sumSalary = 0
	for  worker in workerlist:
		
		salary = int(worker[ 3 ])
		sumSalary += salary
		
	print( "A dolgozók fizetése: ", sumSalary )
		
def countMiskolc():
	
	workerlist = read()
	
	counter = 0
	for worker in workerlist:
		
		if( worker[ 1 ] == "Miskolc" ):
			
			counter += 1
			
	print( "Miskolciak létszáma: ", counter )
	
def sumSzegedSalary():
	
	workerlist = read()
	
	sumSzeged = 0
	for worker in workerlist:
		
		if( worker[ 1 ] == "Szeged" ):
			
			sumSzeged += int( worker[ 3 ])
	print( "Szegediek fizetése: ", sumSzeged )
				
					
#salaries()
#countMiskolc()
#sumSzegedSalary()


def countLajos():
	
	workerlist = read()
	
	counter = 0
	for worker in workerlist:
		
		if( worker[ 0 ] == "Lajos" ):
			
			counter += 1
			
	print( "Lajos nevű dolgozók száma: ", counter )

# két megoldás van, split-es és egy egyszerű.
countLajos()

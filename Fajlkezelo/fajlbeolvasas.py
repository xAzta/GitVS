def read():
	
	print( "Beolvasas..." )
	file = open( "dolgozok100.txt", "r", encoding="utf8" ) # "w" írásra "a" append: hozzáfűzés. Ha szeretnénk módosítani a szöveget az appendet kell használni. encoding="utf8"-vel nem lesz probléma az ékezetes szöveggel.
	
	file.readline()
	row = file.readline()
	
	counter = 0
	while( row ):
		
		counter += 1
		row = file.readline()
		
	print( "Dolgozók létszáma: ", counter )
		
read()

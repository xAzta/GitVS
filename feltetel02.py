"""
match érték:

	case feltétel1:
		utasítások
	case feltétel2:
		utasítások
	case feltétel3:
		utasítások
"""

number = 4

match number:
	
	case 1:
		print( "Egy" )
	
	case 2:
		print( "Kettő" )
		
	case 3:
		print ( "Három" )

	case _:
		print( "Egyik sem" )

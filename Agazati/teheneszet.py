# N�v: Varga Sebastian
# D�tum: 2025.04.08.

tej_naponta_egy_tehentol = 13.8 # liter
tehenek_szama = 63
napok_szama_hetente = 7

# Teljes teh�n�llom�ny kisz�m�t�sa
heti_tejhozam_literben = ( tehenek_szama * tej_naponta_egy_tehentol * 7 ) / 100

# Bek�r�s: heti tejmennyis�g hektoliterben
rendelt_hektoliter = float( input ( "Mennyi tejet szeretne v�s�rolni hetente (hektoliterben)? "))
rendelt_liter = rendelt_hektoliter * 100 # hektoliter -> liter

if heti_tejhozam_literben >= rendelt_liter:

    print( "Rendel�s teljes�thet�" )

else:

    print( "Tehenet kell v�s�rolni" )

print( "K�sz�t�: Varga Sebastian" )


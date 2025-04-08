# Név: Varga Sebastian
# Dátum: 2025.04.08.

tej_naponta_egy_tehentol = 13.8 # liter
tehenek_szama = 63
napok_szama_hetente = 7

# Teljes tehénállomány kiszámítása
heti_tejhozam_literben = ( tehenek_szama * tej_naponta_egy_tehentol * 7 ) / 100

# Bekérés: heti tejmennyiség hektoliterben
rendelt_hektoliter = float( input ( "Mennyi tejet szeretne vásárolni hetente (hektoliterben)? "))
rendelt_liter = rendelt_hektoliter * 100 # hektoliter -> liter

if heti_tejhozam_literben >= rendelt_liter:

    print( "Rendelés teljesíthetõ" )

else:

    print( "Tehenet kell vásárolni" )

print( "Készítõ: Varga Sebastian" )


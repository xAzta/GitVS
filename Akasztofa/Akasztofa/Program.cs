string[] szavak= { "törpe", "pálinka", "bor", "sör", "nyuszi", "cica" };
Random rnd = new Random();

Console.SetCursorPosition(10, 0);
Console.WriteLine("Akasztófa");

Char[] kitalalando = szavak[rnd.Next(0,szavak.Length)].ToCharArray();
Char[] kitalalt = new char[kitalalando.Length];
for (int i = 0; i < kitalalt.Length; i++) kitalalt[i] = '*';

int maxTipp = kitalalando.Length + 2;
int tippSzam = 0;

List<char> chars = new List<char>();
do
{
    Console.SetCursorPosition(1, 2);
    Console.WriteLine(string.Join("", kitalalt));
    Console.SetCursorPosition(1, 4);
    if (chars.Count != 0 ) Console.Write($"Eddigi tippek: {String.Join(", ",chars)}");
    Console.SetCursorPosition(1, 5);
    Console.Write("Tippelj egy betűt: ");
    var tipp = Console.ReadKey().KeyChar;
    chars.Add(tipp);
    tippSzam++;
    char[] ujKitalalt = new char[kitalalt.Length];
    for (int i = 0; i < kitalalando.Length; i++)
    {
        if (kitalalando[i] == tipp)
        {
            kitalalt[i] = tipp;
        }
    }
}
while ((tippSzam <= maxTipp) && (string.Join("", kitalalando) != string.Join("", kitalalt)));

Console.SetCursorPosition(1, 2);
Console.WriteLine(string.Join("", kitalalando));

Console.SetCursorPosition(1, 7);

if (String.Join("", kitalalando) == string.Join("", kitalalt))
    Console.WriteLine("Kitaláltad! Ügyes vagy!");
else
    Console.WriteLine("Sajnos ez most nem sikerült!");

Console.WriteLine("Még egy játék (i/n)?");
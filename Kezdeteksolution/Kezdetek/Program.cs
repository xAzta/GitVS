// See https://aka.ms/new-console-template for more information
using System.ComponentModel.Design;

Console.WriteLine("Hello, World!");
Console.WriteLine("Jáger Attila");
Console.WriteLine("Józsa Béla");

Console.Write("Ird be a neved: ");
/* string nev = Console.ReadLine();

Console.WriteLine("Szervusz, Kedves "+nev);
Console.WriteLine($"Szervusz, Kedves {nev}!"); */

Console.WriteLine("Próba");

Console.Write("Irj be egy számot: ");
string szam = Console.ReadLine();

int szam1 = Convert.ToInt32(szam);

Console.Write("Irj be egy másik számot: ");
int szam2 = Convert.ToInt32(Console.ReadLine() );

Console.WriteLine("Összeg: "+ (szam1 + szam2) );

int i = int.MaxValue;
Console.WriteLine($"i: {i}");
i = i + 1;
Console.WriteLine($"i: {i}");

byte b = 255;
Console.WriteLine($"b: {b}");

Console.WriteLine($"b: {++b}");

float f = 1 / 3.0f;
Console.WriteLine($"Float: {f}");
double d = 1 / 3.0d;
Console.WriteLine($"Double: " + d);

decimal c = 1 / 3.0m;
Console.WriteLine($"Decimal: " + c);

Console.Write("Irj be egy harmadik számot: ");
int szam3 = Convert.ToInt32(Console.ReadLine());

if (szam3 > 10 && szam3 < 100) { 
    Console.WriteLine("10 és 100 között");
}
else {
    Console.WriteLine("NEM 10 ÉS 100 között");
}
double nemEgesz = Math.Sqrt(szam3);

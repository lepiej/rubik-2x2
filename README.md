 Kostka 2x2 
 
 Należy napisać program który obsługuje kostkę rubika 2x2 
 
 Twój program powinien: 
 - Zapamiętać stan ścianek kostki (albo kolorami albo konkretnymi klockami i ich orientacją) 
 - Wyświetlić kostkę (jako siatkę, ścianka po ściance, pseudo 3d) 
 - Obsłużyć wszystkie możliwe ruchy (jest ich 12, 6 w prawo i 6 w lewo) 
 - Jeśli wymaga tego sposób wyświetlania, obracać całą kostkę 
 - Posiadać funkcję mieszającą wykonującą losowe ruchy.

 Co program posiada:
1. Stan kostki - Zapamiętuje wszystkie 6 ścianek (górna, dolna, lewa, prawa, przednia, tylna)

2. Wyświetlanie:
- Widok siatkę (rozłożona kostka)
- Litery kolorow zamiast liczb 
- Widok pseudo-3D (intuicyjny)

3. Wszystkie 12 ruchów:

U, U' - obrot górny
D, D' - obrot dolny
R, R' - obrot prawy
L, L' - obrot lewy
F, F' - obrot przedni
B, B' - obrot tylny

4. Funkcja mieszająca - M mieszy kostkę losowymi ruchami

5. Inne funkcje:

S - pokazanie siatkę
C - reset do stanu początkowego
Q - wyjście

Jak uruchomić:
python3 kostka_2x2_proste.py
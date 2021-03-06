# Määrittelydokumentti


Ohjelmassa etsitään lyhyin reitti labyrintin läpi käyttäen kahta eri algoritmia.
Työssä vertaillaan BFS ja Dead end filling -algoritmien tehokkuutta löytää polku labyrintista ulos. Tietorakenteista käytössä ovat ainakin pinorakenne ja verkko.

Ohjelmassa on tekstikäyttöliittymä, jossa labyrintti muodostuu #- ja . -merkeistä (# tarkoittaen seinää ja . merkiten polkua). 
Ohjelma kysyy käyttäjältä, minkä kokoinen labyrintti generoidaan. Labyrintin alkupiste ja loppupiste kysytään myös käyttäjältä.
Labyrintti luodaan käyttäen satunnaistettua syvyyshakua.

Aikavaativuus leveyssuuntaisessa haussa on O(|E|+|V|log|V|). Dead en fillingin aikavaativuus riippuu paljon tilanteesta, mutta on samaa luokkaa BFS:n kanssa. 
Tilavaativuus on molemmissa O(|V|).

Projekti toteutetaan ainoalla hallitsemallani ohjelmointikielellä Pythonilla. Olen toisen vuoden TKT-pääaineopiskelija.

Lähteet:

https://en.wikipedia.org/wiki/Maze-solving_algorithm

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

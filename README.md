# Regresijski model-Leo Janković 

Znači ovo je jednostavan model koji uspomoć strojnog učenja pretpostavalja cijenu dionice. To radi na osnovu prošlih pomaka u cijeni. 
Za to uspjeti morao sam importati dosta modula, no nakraju se isplatilo. Primjer koji sam ja uzeo je teslina dionica te korisnik samo pokrene kod i outputa se graf koji pokazuje prošlu cijenu(narančasta boja) i buduću cijenu(plava boja).

Malo detaljnije:

Model uči na osnovu prijašnjih pomaka u cijeni, znači naprimjer ako nakon 3 minute rasta u cijeni slijedi 1 minuta pada, on to bilježi te primjenjuje u budućnosti. Ono što je važno jest da sam ga naprvio tako da pretpostavlja cijene nama mjesec dana u nazad tako da možemo vidjeti koliko je točan. Da pojasnim, on gleda cijene od prije 3. mjeseca kako bi pretpostavio cijene u 3. mjesecu tako da ih onda ja mogu uspredit s pravim cijenama u 3. mjesecu i reći kolko je dobar model. Regresija funkcionira tako se uzme neki prosječan pomak u cijeni te onda gledamo odstupe od tog prosječnog pomaka. Zapravo najveći problem ovog koda je bilo koliko informacija(cijena) treba dati modelu jer se cijena bilježi savku minutu, a mi želimo pretpostaviti cijnenu na duži period u budućnosti. Tako da sam mu ja dao cijene na dnevnoj bazi, a ne svake minute jer bi tada vrijeme za naparvit pretpostavku cijene bilo ogromno. Sve u svemu  mogu reći da sam zadovoljan s pretpostavkom, model je procjenio da će cijena nastaviti padati s obzirom na pandemiju( on je to shvatio s obzirom na cijenu, a ne zato jer zna za pandemiju) te se onda opet povisiti. Što donekle ima smilsla,  no vidjet ćemo, vrijeme će reći. Također ono što outputa iza grafa su najviše i najniže cijene, broj trejdanih sherova dionice i završna cijena proteklih 5 dana. Za matematičko obješnjenje regresije ovdje je link:
https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/11-correlation-and-regression 

Novi dio:
Trenutno pokušavam dodati GUI koji će zatražiti ime kompanije, te onda izbaciti njen graf i predikciju. Problem je što mogu imati samo određeni broj kompanija jer ne postoji stranica od koje bi mogao zatražiti simbol kompanije  za ime kompanije koje ja dam.


Uzelo je puno vremena i istraživanja no nakraju se isplatilo i puno sam naučio te se  nadam  da će biti još ovakvih prilika. 

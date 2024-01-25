# Projekt SaToS
Doslovně: Projekt **"Storage against Terms of Service"** neboli 
**Uložiště v rozporu s podmínkami užití.**

## Jak tento magický program funguje?
Tento program umožňuje nahrávat a stahovat soubory na cloud.
Vše je neomezené a šifrované.

## To zní až moc perfektně.
**Jak přesně tohle funguje?**

 - Tento program vychází z jednotlivé myšlenky, že v dnešní době se dají ukládat data téměř kamkoliv. Jediný problém je že většina služeb jako Discord limituje velikost těchto dat (25MB). Proto SaToS přichází do hry:
 
 - Z jednoho velkého souboru (nebo složky v podobě zipu) udělá několik menších dle služby, kam se soubor nahraje (chunky).

 - Každý chunk je zašifrován stejným klíčem, který byl vygenerován pro daný původní soubor.

- Každý zašifrovaný chunk je poté nahrán na službu (např. Discord), a jeho odkaz se následně uloží do emulovaného souborového systému, který obsahuje všechny odkazy na všechny chunky, hash každého chunku, velikost, název a další data.

- Při stahování souboru je tento proces úplně identický, akorát opačný.


**To asi není úplně legit co?**
- No vzhledem k ToS (haha v názvu) moc není. Proto je tento projekt definován jako pouhá demonstrace a pro edukativní účely (mrk mrk).

# ASC-project

Entropia limbii romane.

## Autori

* [Gatej Andrei](https://github.com/Andrei0872)
* [Izotova Daria](https://github.com/Daria602)

---

## Utilizare

1. Copiati repo-ul in masina locala

```bash
git clone https://github.com/dariaASC/ASC-project.git
```

2. Rulati programul folosind

*Important*: inainte de a rula programul, poate ca ati vrea sa modificati valoarea variabilei `grpLenBoundary` din `main.py`. Valoarea maxima folosita de noi a fost `21`(grupul maxim de litere avand lungimea `20`) si programul a fost executat pana la final, cu mentiunea ca a durat ceva mai mult de 10 secunde.

```bash
python main.py
```

---

## Cum functioneaza

* Citirea textului din fisier
* Eliminarea tuturor semnelor de punctuatie, ramanand astfel doar litere mici si spatii
* Pentru combinatii de litere:
  * Trecerea prin fiecare combinatie de litere (incepand cu cate 1 pana la valoarea setata de `grpLenBoundary`) si cautarea frecventei sale
  * Calcularea entropiei folosind formula lui Shannon
* Dupa impartirea textului intr-o lista de cuvinte:
  * Numararea frecventei aparitiei fiecarui cuvant
  * Calcularea entropiei cuvintelor folosind formula lui Shannon
  * Calcularea mediei aritmetice a lungimilor tuturor cuvintelor 
  * Impartirea entropiei la media aritmetica a lungimilor tuturor cuvintelor
* La iesire: entropia pentru fiecare combinatie si entropia pentru toate cuvintele

### Cum s-a calculat entropia pentru grupuri de litere

```
F1 = entropia de cate 1 (4.1)
F2 = entropia de cate 2 (7,5) - entropia de cate 1 (4,1)
F3 = entropia de cate 3 (10,3) - entropia de cate 2 (7,5)
.
.
.
Fn = entropia de cate n - entropia de cate n - 1
```

### Pseudocod

```
content = readFile('input.txt')
content = content.replacePunctuationMarks().adjustSpacesAndNewLines()

for i = 1 until i = groupLengthBoundary
  countFrequencyOfGroup
  computeEntropyForTheCurrentGroup
  printComputedEntropy

words = content.SplitIntoWords()

for word in words
  countFrequencyOfWord
  computeEntropyForTheCurrentWord
  printComputedEntropy
```

---

## Resurse folosite

* Despre Entropie: [Prediction and Entropy of Printed English, By C. E. SHANNON](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf).
* Textul de input: [Ion, de Liviu Rebreanu](https://ro.wikisource.org/wiki/Ion_(Rebreanu))

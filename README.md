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

### Pseudocod

```
content = readFile('input.txt')
content = content.replacePunctuationMarks().adjustSpacesAndNewLines()

words = content.SplitIntoWords()

for word in words
  countFrequencyOfWord
  computeEntropyForTheCurrentWord
  printComputedEntropy
```
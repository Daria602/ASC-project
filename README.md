# ASC-project
Entropia limbii romane

## Autori

* [Gatej Andrei](https://github.com/Andrei0872)
* Izotova Daria

## Utilizare

## Plan

* we get some texts from recent news and set it as data-base
* determine the frequency for each letter of the text; its prob. will be `prob(char) = freq(char) / text.length`
* entropy (use formula)
* output the results to a file called `output.txt`
lui ana ii place analiza matematica (12)
p(a) = how many times it app/how many in total


a   b c ... e .. m  n ... r
| \              e  a
n  r             r  a
a  |             e
   e
   | \
   a  e

  
the structure of a node

Node {
  letter: '',
  freq: number,
  children: []Node,
  timesMarkedAsEndOfWord: number // 0 - default value
}

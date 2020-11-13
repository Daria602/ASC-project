# -*- coding: UTF-8 -*-
import math
import re

signs = '[0-9\.\-":;!\?„,\'”″“]|[—]\s?|\[.*\]'

inputFile = open("input.txt", "r")
letterDictionary = {}

content = inputFile.read().lower()
content = re.sub(signs, '', content)
content = re.sub('\s{2,}', ' ', content)
content = re.sub('[\n]', ' ', content)
contentLen = len(content)

inputFile.close()

grpLenBoundary = 21

print("The maximum length of a group of letters is ", grpLenBoundary - 1)

prevRawEntropy = None

for m in range(1,grpLenBoundary):
  freq = {}

  for i in range(0, contentLen):
    if len(content[i:i+m]) < m:
        break
    if content[i:i+m] not in freq:
        freq[content[i:i+m]] = 1
    else:
        freq[content[i:i+m]] += 1
  
  total = contentLen - m + 1
  freq.update((x, (y/total) * (math.log2(y/total))) for x, y in freq.items())
  entropy = -(sum(freq.values()))
  
  result = None

  if m == 1:
    result = entropy
  else:
    result = entropy - prevRawEntropy
  
  prevRawEntropy = entropy
  print("Entropy for combinations of every ", m, "letters is ", result)

content = content.split(' ')
contentLen = len(content)

wordDic = {}
wordSumLen = 0

for word in content:
  wordSumLen += len(word)
  
  if word not in wordDic:
    wordDic[word] = 1
  else:
    wordDic[word] += 1

totalWords = contentLen
wordAvg = wordSumLen / totalWords
wordDic.update((x, (y/totalWords) * (math.log2(y/totalWords))) for x, y in wordDic.items())
entropy = -(sum(wordDic.values()))

print("Entropy for all words", entropy / wordAvg)

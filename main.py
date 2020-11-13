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
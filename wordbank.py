import json

class Wordbank():
  def __init__(self, filePath):
    self.filePath = filePath
    with open(filePath) as f:
      fileData = f.read()
      if len(fileData) > 0:
        self.WordListDict = json.loads(fileData.replace('\n', ''))
      else: self.WordListDict = dict()

  def wordlists(self):
    return [*self.WordListDict]

  def hasWordList(self, listName):
    return listName in self.wordlists()
      
  def createWordList(self, listName):
    if self.hasWordList(listName):
      return False
    self.WordListDict[listName] = list()
    return True
    
  def addWordToList(self, wordToAdd, listName):
    if wordToAdd in self.WordListDict[listName]:
      return False
    self.WordListDict[listName].append(wordToAdd)
    return True

  def removeWordFromList(self, indexToRemove, listName):
    self.WordListDict[listName].pop(indexToRemove)
    return True

  def deleteWordList(self, listName):
    del self.WordListDict[listName]

  def getWordsFromList(self, listName):
    return self.WordListDict[listName]
  
  def update(self):
    with open(self.filePath, "w") as file:
      stringToWrite = json.dumps(self.WordListDict, indent=2, sort_keys=True)
      file.write(stringToWrite)
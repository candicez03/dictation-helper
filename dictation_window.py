import pyglet
import random
from google_speech import Speech
from wordbank import *

LANG_EN_US = "en-US"
LANG_CN_MANDARIN = "cmn-CN"

START_PAGE           = 0
MANAGE_WORDBANK_PAGE = 1
START_DICTATION_PAGE = 2
IN_DICTATION_PAGE    = 3
END_DICTATION_PAGE   = 4
SETTINGS_PAGE        = 5
CREDITS_PAGE         = 6
EDIT_WORDLIST_PAGE   = 7



class MyWindow(pyglet.window.Window):
  def __init__(self, wordbank, *args,**kwargs):
    pyglet.window.Window.__init__(self, *args,**kwargs)
    self.wordbank = wordbank
    self.initPage(START_PAGE)
  
  def drawRect(self, x, y, w, h, color=(255,255,255)):
    pyglet.graphics.draw(4,
                         pyglet.gl.GL_QUADS,
                         ('v2f', [x, y, x+w, y, x+w, y+h, x, y+h]),
                         ('c3B', (color*4)))

  def drawText(self, text, drawX, drawY, fontSize = 18, drawColor = (0,0,0,255)):
    label = pyglet.text.Label(text,
                              font_size = fontSize,
                              x = drawX,
                              y = drawY,
                              color = drawColor)
    label.draw()
    return
    
  def initPage(self, page):
    self.currentPage = page

    if page == START_PAGE:
      self.selectedLists = ['unit 1', 'unit 2']#list()
      self.wordsToDictate = list()
      self.dictationIndex = 0

    elif page == MANAGE_WORDBANK_PAGE:
      pass

    elif page == START_DICTATION_PAGE:
      pass

    elif page == IN_DICTATION_PAGE:
      self.dictationIndex = 0
      result = set()
      for wordlist in self.selectedLists:
        for word in self.wordbank.getWordsFromList(wordlist):
          result.add(word)
      self.wordsToDictate = list(result)
      print(self.wordsToDictate)
      random.shuffle(self.wordsToDictate)

    elif page == END_DICTATION_PAGE:
      pass
    elif page == SETTINGS_PAGE:
      pass
    elif page == CREDITS_PAGE:
      pass

  def drawPage(self):
    if self.currentPage == START_PAGE:
      self.drawRect(0, 0, self.width,self.height)
      self.drawText("1: manage word bank", self.width//4, self.height//2+50)
      self.drawText("2: start dictation",  self.width//4, self.height//2)
      self.drawText("3: settings",         self.width//4, self.height//2-50)

    elif self.currentPage == START_DICTATION_PAGE:
      wordlists = self.wordbank.wordlists()
      self.drawRect(0, 0, self.width,self.height)
      for i in range(len(wordlists)):
        textToDraw = wordlists[i]
        if wordlists[i] in self.selectedLists:
          textToDraw += "(selected)"
        self.drawText(textToDraw, 10, self.height-20-i*20)

    elif self.currentPage == IN_DICTATION_PAGE:
      self.drawRect(0, 0, self.width,self.height)
      self.drawText(str(self.dictationIndex+1) + '/' + str(len(self.wordsToDictate)), self.width//2-25, self.height-30)
      self.drawText(self.wordsToDictate[self.dictationIndex], 100, 100)

  def handleKeyEvent(self, symbol, modifiers):
    if symbol == pyglet.window.key.BACKSPACE:
      self.currentPage == START_PAGE
      return

    if self.currentPage == START_PAGE:
      if symbol == pyglet.window.key._1:
        self.initPage(MANAGE_WORDBANK_PAGE)
      elif symbol == pyglet.window.key._2:
        self.initPage(START_DICTATION_PAGE)
      elif symbol == pyglet.window.key._3:
        self.initPage(SETTINGS_PAGE)

    elif self.currentPage == MANAGE_WORDBANK_PAGE:
      pass

    elif self.currentPage == START_DICTATION_PAGE:
      if symbol == pyglet.window.key.ENTER:
        self.initPage(IN_DICTATION_PAGE)
      #test only
      if symbol == pyglet.window.key._1:
        self.toggleSelect(self.wordbank.wordlists()[0])
      elif symbol == pyglet.window.key._2:
        self.toggleSelect(self.wordbank.wordlists()[1])

    elif self.currentPage == IN_DICTATION_PAGE:
      if symbol == pyglet.window.key.RIGHT:
        print(self.wordsToDictate[self.dictationIndex])
        self.dictationIndex = (self.dictationIndex+1) % len(self.wordsToDictate)
        speech = Speech(self.wordsToDictate[self.dictationIndex], LANG_CN_MANDARIN)
        speech.play()
      elif symbol == pyglet.window.key.R:
        speech = Speech(self.wordsToDictate[self.dictationIndex], LANG_CN_MANDARIN)
        speech.play()

    elif currentPage == SETTINGS_PAGE:
      pass

  def toggleSelect(self, listName):
    if listName not in self.selectedLists:
      self.selectedLists.append(listName)
    else:
      self.selectedLists.remove(listName)
    return True
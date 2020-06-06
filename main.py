import pyglet
from dictation_window import *

wordbank = Wordbank('vocabulary.json')
screenInitWidth, screenInitHeight = 800, 600

window = MyWindow(wordbank, screenInitWidth, screenInitHeight, resizable=True, caption='Dictation Helper v1.0')
window.set_minimum_size(480, 360)
window.set_maximum_size(1920, 1080)
window.set_location(0, 32)

@window.event
def on_draw():
  window.clear()
  window.drawPage()

@window.event
def on_key_press(symbol, modifiers):
  window.handleKeyEvent(symbol, modifiers)

@window.event
def on_mouse_press(x, y, button, modifiers):
  if button == pyglet.window.mouse.LEFT:
    pass

pyglet.app.run()
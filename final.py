from rule import *
import tkinter

class Final(Rule):
     def __init__(self, master, number, check, rule):
          super(Final,self).__init__(master, number, check, rule, lambda text : False)
          self.button = Button(master = self, text = "CONFIRM PASSWORD")
          self.button.pack()
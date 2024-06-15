from tkinter import*

class Rule(Frame):
    
  red = '#ff6254'
  redbody = '#ff2121'
  green = '#54ff5d'
  greenbody = '#21ff21'
  def color(self, e):
    self.redbody = self.greenbody = e
    super().config(bg=e)
    self.body.config(bg=e)
  def __init__(self, master, number, check, rule, checkrule):
    self.number = number  
    self.check = check
    self.rule = rule

    super().__init__(master, bg = Rule.green if check else Rule.red)
    self.heading = Label(self, text = 'rule #' + str(self.number), background = Rule.green if check else Rule.red, font = ('Cascadia Code', 24))
    self.body = Label(self, background = Rule.greenbody if check else Rule.redbody, text = self.rule,  font = ('Cascadia Code', 18))

    self.heading.pack()
    self.body.pack()
    self.checkrule = checkrule

  def checkcolor(self):
    super().config(bg = self.green if self.check else self.red)
    self.heading.config( background = self.green if self.check else self.red)
    self.body.config( background = self.greenbody if self.check else self.redbody)
  
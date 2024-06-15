import shutil
from tkinter import *
from rule import *
import python_weather
import time 
import wordle
import random
import mendeleev
import datetime
import zipcodes
import asyncio
import geocoder
import copy
import platform
import nltk
from final import *
import subprocess

#hi
startrule = 1
color = '#%02x%02x%02x'% (random.randint(0,255), random.randint(0,255,), random.randint(0,255))
def clor():
    print(color)
def convert(number):
    roman = ''


    numeral = [
        'M',
        'CM',
        'D',
        'CD',
        'C',
        'XC',
        'L',
        'XL',
        'X',
        'IX',
        'V',
        'IV',
        'I'    
    ]
    numbers = [
        1000,
        900,
        500,
        400,
        100,
        90,
        50,
        40,
        10,
        9,
        5,
        4,
        1
    ]
    while number>0:
        i=0
        while numbers[i] > number:
            i+=1
        number-=numbers[i]
        roman+=numeral[i]
    print(roman)
    return roman

wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces']).decode('utf-8').split("Profile")[1][18:].split(" ")[0]
print(wifi)
cityname = geocoder.ip("me").json["city"]
used = int(shutil.disk_usage('C:')[1]/1073741824)
print(used)
free = int(shutil.disk_usage('C:')[2]/1073741824)
r = convert(free)

 
async def weather():
    async with python_weather.Client(unit = python_weather.IMPERIAL) as get:
        city = await get.get(geocoder.ip("me").json["address"])
        return city.current.kind
async def temp():
    async with python_weather.Client(unit = python_weather.IMPERIAL) as get:
        city = await get.get(geocoder.ip("me").json["address"])
        return city.current.temperature
temperature = asyncio.run(temp())
print(temperature)
window = Tk()
box = Text(window, bg = '#c9c6bb', fg = '#000000', width = 75, font = ("Cascadia Code", 24), height = 3)
text = StringVar()
final = ""

os = platform.system()

if os == 'Darwin':
    os == 'MacOS'

def settext(event):
    text.set(box.get("1.0", END))
box.bind("<KeyRelease>", settext)

wins = ''



forecast = asyncio.run(weather())
weathertype =  ''
if forecast == python_weather.enums.Kind.HEAVY_RAIN or forecast == python_weather.enums.Kind.LIGHT_RAIN or forecast == python_weather.enums.Kind.HEAVY_SHOWERS or forecast == python_weather.enums.Kind.LIGHT_SHOWERS:
     weathertype = "rainy"
elif forecast == python_weather.enums.Kind.HEAVY_SNOW or forecast == python_weather.enums.Kind.LIGHT_SNOW or forecast == python_weather.enums.Kind.HEAVY_SNOW_SHOWERS  or forecast == python_weather.enums.Kind.LIGHT_SNOW or forecast == python_weather.enums.Kind.LIGHT_SNOW_SHOWERS:
    weathertype = 'snowy'
elif forecast == python_weather.enums.Kind.SUNNY:
    weathertype = 'sunny'
elif forecast == python_weather.enums.Kind.THUNDERY_SNOW_SHOWERS or forecast == python_weather.enums.Kind.THUNDERY_HEAVY_RAIN or forecast == python_weather.enums.Kind.THUNDERY_SHOWERS:
    weathertype = 'thunder'
elif forecast == python_weather.enums.Kind.LIGHT_SLEET or forecast == python_weather.enums.Kind.LIGHT_SLEET_SHOWERS:
    weathertype = 'sleet'
elif forecast == python_weather.enums.Kind.FOG:
    weathertype = 'foggy'
elif forecast == python_weather.enums.Kind.CLOUDY or forecast == python_weather.enums.Kind.VERY_CLOUDY or forecast == python_weather.enums.Kind.PARTLY_CLOUDY:
    weathertype = 'cloudy'
else:
    weathertype = 'other'
print(weathertype)
elementnumbeer = random.randint(1,118)
elementname = mendeleev.element(elementnumbeer).name
elementsymbol = mendeleev.element(elementnumbeer).symbol
elementnumbeer2 = random.randint(1,118)
elementsymbol2 = mendeleev.element(elementnumbeer2).symbol
elementnumbeer3 = random.randint(1,118)
elementsymbol3 = mendeleev.element(elementnumbeer3).symbol
period = mendeleev.element(elementnumbeer3).period
periodroman = convert(period)

operations = ['*','+','-']
randomop = random.choice(operations)
random1 = str(random.randint(1, 50))
random2 = str(random.randint(1, 50))
stringop = random1 + randomop + random2
zipcode = str(random.randint(0,99999)).zfill(5)
randomsum = random.randint(80,110)

while zipcodes.is_real(zipcode) == False:
    zipcode = str(random.randint(0,99999)).zfill(5)


background = '#faf8cd'
window.title('the password game')
window.geometry('1800x1200')
def check(*args):

    if len(notdone) != 0 and notdone[0].number == 1: 
        rules.insert(0, notdone.pop(0))
        rule()
    for therule in rules:
        previouscheck = therule.check
        therule.check = therule.checkrule(text.get())
        therule.checkcolor()
        if previouscheck != therule.check:
            rule()

    if all(rule.check == True for rule in rules):
        if len(notdone) != 0:
            rules.insert(0, notdone.pop(0))
            if(rules[0].number==24):
                rules[0].color(color)
            if(rules[0].number==13):
                color() 
            rule()
            check()
            if len(notdone) == 0:
                for therule in rules:
                    therule.pack_forget()
                rules[0].button.configure(command=confirm)
                delete()
                rule()
def rule():
    order = []

   
    for therule in rules:
        if therule.check == False:
            order.append(therule)

    for therule in rules:
        if therule.check:
            order.append(therule)
    
    for therule in reversed(order):
        therule.pack_forget()
        therule.pack(pady = 20, side = BOTTOM)
    order.clear()

scroll = Scrollbar(window)



canvas = Canvas(window, background = '#faf8cd',yscrollcommand = scroll.set)
text.trace('w', check)
window.config(bg=background)
title = Label(window, bg = background, font=("Cascadia Code", 24),text = 'the password game')
title.pack()
box.pack(pady = 20)
ruleframe = Frame(canvas, background = '#faf8cd')
scroll.config(command = canvas.yview)
scroll.pack(side = RIGHT, fill = Y)
canvas.pack(fill=BOTH, expand=TRUE)
def wait():
    print('e')
    global wins
    wins.pack_forget()
    title.pack()
    box.pack(pady = 20)
    scroll.pack(side = RIGHT, fill = Y)
    canvas.pack(fill=BOTH, expand=TRUE)
    global notdone
    notdone = [Rule(ruleframe, 1, False, 'your password must be at least 5 characters', lambda text : len(text) >=5),
        Rule(ruleframe,2, False, 'your password must have a number', lambda text : any(char.isdigit() for char in text)),
        Rule(ruleframe,3, False, 'your password must have a capital letter', lambda text : any(char.isupper() for char in text)),
        Rule(ruleframe,4, False, 'your password must have a special character', lambda text : any(isspecial(chear) for chear in text)),
        Rule(ruleframe,5, False, 'your password must include a month of the year', lambda text : ismonth(text)),
        Rule(ruleframe,6, False, 'the digits in your password must add up to '+ str(randomsum), lambda text : issum(text) == randomsum),
        Rule(ruleframe,7, False, 'your password must contain today\'s wordle answer', lambda text : wordle.get_wordle_for_today() in text.lower()),
        Rule(ruleframe,8,False, 'your password must contain the answer to this expression: ' + stringop, lambda text : str(eval(stringop)) in text),
        Rule(ruleframe,9, False, 'your password must contain the name of this symbol in the periodic table:' + elementsymbol, lambda text : elementname.lower() in text.lower()),
        Rule(ruleframe,10, False, 'your password must contain the number of electrons in an atom of this element in the periodic table:' + elementsymbol2, lambda text : str(elementnumbeer2)in text),
        Rule(ruleframe,11, False, 'your password must include the period of this element in a roman numeral:' + elementsymbol3, lambda text : periodroman.lower() in text.lower()),
        Rule(ruleframe,12, False, 'your password must contain the first 5 digits of pi', lambda text : str(3.1415) in text),
        Rule(ruleframe,13,False, 'your password must include the hex code of the background this page', lambda text : title.cget('bg') in text.lower()),
        Rule(ruleframe,14,False,'your password must include the current hour of the day', lambda text : str(datetime.datetime.now().hour) in text),
        Rule(ruleframe,15,False,'your password must include the city of this zipcode (ex: New York,NY):' + zipcode, lambda text : zipcodes.matching(zipcode)[0]['city']+','+zipcodes.matching(zipcode)[0]['state'] in text),
        Rule(ruleframe,16,False, 'your password must contain the same number of uppercase letters as lowercase', lambda text : iseven(text)),
        Rule(ruleframe,17, False, 'your password must include your operating system', lambda text : os.lower() in text.lower()),
        Rule(ruleframe,18, False, 'your password must include a 10 letter word', lambda text : isword(10,text)),
        Rule(ruleframe,19, False, 'your password must include the current weather (sunny, rainy, snowy, sleek, foggy, or cloudy).', lambda text : weathertype in text.lower()),
        Rule(ruleframe,20, False, 'your password must include the city you live in', lambda text : cityname.lower() in text.lower()),
        Rule(ruleframe,21,False,'your password must include the current temperature in binary', lambda text : bin(temperature)[2:] in text),
        Rule(ruleframe,22, False, 'your password must include the length in characters of your password', lambda text : str(len(text) - 1) in text),
        Rule(ruleframe,23, False, 'your password must have your wifi name', lambda text : wifi in text),
        Rule(ruleframe,24, False, 'your password must include the amount of storage taken up in GB', lambda text : str(used) in text),
        Rule(ruleframe,25,False, 'your password must include the amount of free storage on your computer in roman numerals (in GB)', lambda text : r.lower() in text.lower()),
        Rule(ruleframe,26,False, 'your password must include the hex code of the color of this rule', lambda text : color in text.lower()),
        Final(ruleframe,27,False,'rewrite your password to confirm.')

    ]
    rules[0].pack_forget()
    del(rules[0])
    
def win(winner):
    global wins
    wins = Label(window, bg= '#14e02c' if winner else '#fc1703', height = 1100, width = 1700,  font=("Cascadia Code", 40),text = 'you win!' if winner else "WRONG.")
    title.pack_forget()
    canvas.pack_forget()
    box.pack_forget()
    scroll.pack_forget()
    wins.pack()
    if winner==False:
        window.after(10000, wait)

rules = []
notdone = [Rule(ruleframe, 1, False, 'your password must be at least 5 characters', lambda text : len(text) >=5),
        Rule(ruleframe,2, False, 'your password must have a number', lambda text : any(char.isdigit() for char in text)),
        Rule(ruleframe,3, False, 'your password must have a capital letter', lambda text : any(char.isupper() for char in text)),
        Rule(ruleframe,4, False, 'your password must have a special character', lambda text : any(isspecial(chear) for chear in text)),
        Rule(ruleframe,5, False, 'your password must include a month of the year', lambda text : ismonth(text)),
        Rule(ruleframe,6, False, 'the digits in your password must add up to '+ str(randomsum), lambda text : issum(text) == randomsum),
        Rule(ruleframe,7, False, 'your password must contain today\'s wordle answer', lambda text : wordle.get_wordle_for_today() in text.lower()),
        Rule(ruleframe,8,False, 'your password must contain the answer to this expression: ' + stringop, lambda text : str(eval(stringop)) in text),
        Rule(ruleframe,9, False, 'your password must contain the name of this symbol in the periodic table:' + elementsymbol, lambda text : elementname.lower() in text.lower()),
        Rule(ruleframe,10, False, 'your password must contain the number of electrons in an atom of this element in the periodic table:' + elementsymbol2, lambda text : str(elementnumbeer2)in text),
        Rule(ruleframe,11, False, 'your password must include the period of this element in a roman numeral:' + elementsymbol3, lambda text : periodroman.lower() in text.lower()),
        Rule(ruleframe,12, False, 'your password must contain the first 5 digits of pi', lambda text : str(3.1415) in text),
        Rule(ruleframe,13,False, 'your password must include the hex code of the background this page', lambda text : title.cget('bg') in text.lower()),
        Rule(ruleframe,14,False,'your password must include the current hour of the day', lambda text : str(datetime.datetime.now().hour) in text),
        Rule(ruleframe,15,False,'your password must include the city of this zipcode (ex: New York,NY):' + zipcode, lambda text : zipcodes.matching(zipcode)[0]['city']+','+zipcodes.matching(zipcode)[0]['state'] in text),
        Rule(ruleframe,16,False, 'your password must contain the same number of uppercase letters as lowercase', lambda text : iseven(text)),
        Rule(ruleframe,17, False, 'your password must include your operating system', lambda text : os.lower() in text.lower()),
        Rule(ruleframe,18, False, 'your password must include a 10 letter word', lambda text : isword(10,text)),
        Rule(ruleframe,19, False, 'your password must include the current weather (sunny, rainy, snowy, sleek, foggy, or cloudy).', lambda text : weathertype in text.lower()),
        Rule(ruleframe,20, False, 'your password must include the city you live in', lambda text : cityname.lower() in text.lower()),
        Rule(ruleframe,21,False,'your password must include the current temperature in binary', lambda text : bin(temperature)[2:] in text),
        Rule(ruleframe,22, False, 'your password must include the length in characters of your password', lambda text : str(len(text) - 1) in text),
        Rule(ruleframe,23, False, 'your password must have your wifi name', lambda text : wifi in text),
        Rule(ruleframe,24, False, 'your password must include the amount of storage taken up in GB', lambda text : str(used) in text),
        Rule(ruleframe,25,False, 'your password must include the amount of free storage on your computer in roman numerals (in GB)', lambda text : r.lower() in text.lower()),
        Rule(ruleframe,26,False, 'your password must include the hex code of the color of this rule', lambda text : color in text.lower()),
        Final(ruleframe,27,False,'rewrite your password to confirm.')

]
del notdone[0:startrule-1]

def delete():
    del rules[1:len(rules)]
    global final
    final = box.get("1.0", END)
    box.delete("1.0",END)
def compare():
    if(final == box.get("1.0", END)):
        return True
    else: 
        return False

def color():
    randcolor='#%02x%02x%02x'% (random.randint(0,255), random.randint(0,255,), random.randint(0,255)) 
    title.config(bg = randcolor)
    canvas.config(bg = randcolor)
    ruleframe.config(bg = randcolor)
    window.config(bg = randcolor)
    box.config(bg = randcolor)
    window.after(60000, color)
    

print(elementname)
def iseven(text):
    number = 0
    number2 = 0
    for char in text:
        if char.isupper() == True:
            number = number+1
           
        if char.islower() == True:
            number2 = number2+1
    return number == number2

def confirm():
    win(winner = compare())
        

def issum(text):
    number = 0
    for char in text:
        if char.isdigit() == True:
            number = number + int(char)
    return number

set3 = set(nltk.corpus.words.words())

def isword(length, text):
    for i in range(0, len(text)-length+1):
        if text[i:i+length].lower() in set3:
            return True 
    return False
 
         
def ismonth(text):
    list = ["january",'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    for lust in list:
        if lust in text.lower():
            return True
    return False

def isspecial(char):
    list = ['`', '~', '!', '@' , '#', '$' , '%' , '^', '*', '(',')', '-', '_', '=', '+', '[',']', '{', '}', '\\', '|', ':', ';', '\"', '\'', ',', '<', '.', '>', '/', '?', ' ']   
    return char in list 

ruleframe_id = canvas.create_window(0,0, window =  ruleframe, anchor = NW)

def _configure_ruleframe(event):
    # Update the scrollbars to match the size of the inner frame.
    size = (ruleframe.winfo_reqwidth(), ruleframe.winfo_reqheight())
    canvas.config(scrollregion="0 0 %s %s" % size)
    if ruleframe.winfo_reqwidth() != canvas.winfo_width():
        # Update the canvas's width to fit the inner frame.
        canvas.config(width=ruleframe.winfo_reqwidth())
ruleframe.bind('<Configure>', _configure_ruleframe)
def _configure_canvas(event):
     if ruleframe.winfo_reqwidth() != canvas.winfo_width():
        # Update the inner frame's width to fill the canvas.
        canvas.itemconfigure(ruleframe_id, width=canvas.winfo_width())
canvas.bind('<Configure>', _configure_canvas)
window.mainloop()
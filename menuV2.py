# Imports
from tkinter import *
from tkinter import ttk
import tkinter as tk

# Functions
from Systems.generic import *

# Caeser Functions
from Systems.caesar import *
from Systems.diffiehellmann import *
from Systems.rsa import *


# The Menu
class Menu():
    def __init__(self):
        self.buttons = []
        self.title = None
        self.typ = None
        self.result = None
        self.getinput = None
        self.inputrq = None
        self.schlüssel = None
        self.klartext = None
        self.geheimtext = None

    def createMenu(self): # Create the Menu
        self.root = Tk()
        self.Mframe = ttk.Frame(self.root, padding=10)
        self.Mframe.size = (1000, 400)


    # Button Functions

    def process_request(self, typ, content): # Process the Request , typ = Status Code of current Action/Request
        if typ == 111 or typ == 211: # Caeser request : Klartext finished -> Request Integer (Schlüssel)
            if typ == 111:
                self.typ = 112
            else:
                self.typ = 212
            self.getinput = "int"
            self.klartext = content
            self.inputrq = "Schlüssel bitte eingeben"
            self.title = "Caeser - Schlüssel"
            self.MenuButtonsTask()
        elif typ == 112 or typ == 212: # Caeser request : Schlüssel finished -> Show Result
            if typ == 112:
                self.typ = 113
            else:
                self.typ = 213
            self.getinput = False
            self.schlüssel = int(content)
            self.inputrq = ""
            self.title = "Caeser - Result"
            self.MenuButtonsTask()
        elif typ == 511: # Caeser Geheimtext getted, show result
            self.typ = 512
            self.getinput = False
            self.geheimtext = content
            self.inputrq = ""
            self.title = "Caeser - Result"
            self.MenuButtonsTask()
    
    # Menu Buttons

    def MenuButtonsMain(self):
        # Clear Menu UI
        for i in self.buttons:
            i.destroy()

        self.Mframe.master.title("Main Menu")

        MButtons_M = ["Caeser Verschlüsselung", "Caeser Entschlüsselung", "Schlüsselaustausch", "RSA Schlüssel", "Caeser kein Schlüssel"] # Menu Buttons+Titles
        MTypes_M = [111, 211, 311, 411, 511] # Menu Action Codes


        for i, v in enumerate(MButtons_M): # Setting up the Buttons with their specific commands and action codes
            temp_btn = ttk.Button(self.root, text=v, command=lambda i=i: self.MenuButtonsTask(MTypes_M[i], MButtons_M[i]))
            temp_btn.pack()
            self.buttons.append(temp_btn) # Append Button to Button List -> For later destruction
        

    def MenuButtonsTask(self, typ=0, title=""): # Managing all Buttons & Requests
        # Clear Menu UI
        for i in self.buttons:
            i.destroy()

        '''
        *List of action codes*
        111, Caeser Verschlüsselung
            112 - Get Integer (Schlüssel)
            113 - Show Result

        211, Caeser Entschlüsselung
            212 - Get Integer (Schlüssel)
            213 - Show Result

        311, Diffie-Hellman Schlüsselaustausch

        411, RSA

        511 Caeser ohne Schlüssel
            512 - Show Result
        '''


        # Setting Up: If Button is clicked or not -> set stuff
        if typ != 0: # First initialization, if not set
            self.typ = typ
        if title != "": # Same for title
            self.title = title
        
        if typ == 111 or typ == 211: # Caeser Verschlüsselung&Entschlüsselung
            # Requesting User Input - Klartext
            self.getinput = "str"
            self.inputrq = "Klartext bitte eingeben"

        elif typ == 311: # Diffie-Hellman Schlüsselaustausch
            self.getinput = False
            self.inputrq = ""
            p, g, a, b, A, B = get_Infos() # Getting Infos, math stuff
            KeyA, KeyB = get_Key(B, a, p, A, b) # Get Keys
            
            self.result = f"p={p} g={g}\nA={A}\nB={B}\nKeyA={KeyA}\nKeyB={KeyB}"

        elif typ == 411:
            self.getinput = False
            self.inputrq = ""
            ne, nd = rsa() # Get Keys from RSA
            
            self.result = f"public key: n={ne[0]}, e={ne[1]}\n private key: n={nd[0]}, d={nd[1]}"

        elif typ == 511:
            self.getinput = "str"
            self.inputrq = "Geheimtext bitte eingeben"

        self.Mframe.master.title(self.title) # setting Title obv

        # Back Button
        back_btn = ttk.Button(self.root, text="Zurück", command=self.MenuButtonsMain)
        back_btn.grid(row=0, column=0)
        back_btn.pack()
        self.buttons.append(back_btn)


        # If User-Input is needed
        if self.getinput == "str" or self.getinput == "int":
            # Input Field
            temp_entry = tk.Entry()
            temp_entry.pack()

            # Fav Text Label
            temp1_label = tk.Label(text="Press enter to continue")
            temp1_label.pack()
            self.buttons.append(temp1_label)

            inputvar = None
            if self.getinput == "int":
                inputvar = tk.IntVar()
            else:
                inputvar = tk.StringVar()

            inputvar.set(self.inputrq)
            temp_entry["textvariable"] = inputvar

            temp_entry.bind('<Key-Return>', lambda event: self.process_request(self.typ, inputvar.get())) # Register Enter Key - Function, continue process_request

            self.buttons.append(temp_entry)
        


        if self.typ == 113 or self.typ == 213: # If Caeser Verschlüsselung requests are finished: Show Result
            key = None
            if self.typ == 113:
                key = self.schlüssel # Schlüssel -> Nach Rechts verschieben
            else:
                key = -self.schlüssel # Schlüssel -> Nach Links verschieben ("Zurück")
            self.result = "Text: "+combine_list_to_sentence(move_alphabet(turn_sentence_to_list(self.klartext), key))
            
        if self.typ == 512:
            possiblekeys, possiblesentences = caeser_getkey(turn_sentence_to_list(self.geheimtext))
            self.result = "Possible Keys & Sentences:\n"
            for i, v in enumerate(possiblekeys):
                self.result += f"Key: {v} - Text: {combine_list_to_sentence(possiblesentences[i])}\n"


        if self.result:
            temp2_label = tk.Label(text=self.result) # Show Result
            temp2_label.pack()
            self.buttons.append(temp2_label)
            self.result = None

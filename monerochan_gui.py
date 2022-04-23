from tkinter import *
from tkinter import ttk
import time
import random
import configparser
import json


class Settings:
    def __init__(self):
        self.VERSION = "0.0.1"
        self.title = "Monerochan Miner GUI"






class MonerochanGUI:
    def __init__(self,_CONFIG):
        self.Settings = Settings()
        self.VERSION = self.Settings.VERSION
        self.Miner = MinerProcess()
        self.root = Tk()
        self.setupWindow()
    def setupWindow(self):
        self.root.minsize(500,500)
        self.root.maxsize(300,250)
        self.root.title(self.Settings.title)





class MinerProcess:
    def __init__(self):
        self.alive = False
    def initiate(self):
        self.alvie = True
    def kill(self):
        self.alvie = False
    def isAlive(self):
        return self.alive

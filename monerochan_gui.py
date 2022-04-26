from tkinter import *
from tkinter import ttk
import time
import random
import configparser
import json
import monero

# from monero.backends.offline import OfflineWallet, WalletIsOffline

# Running xmrig with tor socks proxy 
# command = f"./xmrig -x 127.0.0.1:9050 -a rx/0 -o {onionHost}:{onionPort} -u {mineAddress}"


class Settings:
    def __init__(self):
        self.VERSION = "0.0.1"
        self.title = "Monerochan Miner GUI"


class Wallet:
    def __init__(self,_config):
        self.SEEDPHRASE = self.loadOrCreate(_config)
        #This is the seed class
        self.seed = monero.seed.Seed(self.SEEDPHRASE)

    def getPublicAddress(self):
        return self.seed.public_address()



    def loadOrCreate(self,_config):
        if _config is not None:
            seed = monero.seed.Seed().phrase
        else:
            seed = _config["seed"]
        return seed




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


from pathlib import Path
import configparser
from monerochan_gui import *

config = configparser.ConfigParser()
# config.read_file(open('mine.cfg'))
config['DEFAULT'] = {'seed': '45',
                    'Compression': 'yes',
                      'CompressionLevel': '9'}

def loadWallet():
    wallet = Wallet(config)
    print(wallet.SEEDPHRASE)

if __name__ == '__main__':
    gui = MonerochanGUI(config)
    loadWallet()
    input("Close?")

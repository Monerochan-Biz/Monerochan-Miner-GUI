
from pathlib import Path
import configparser
from monerochan_gui import *

config = configparser.ConfigParser()
# config.read_file(open('mine.cfg'))




if __name__ == '__main__':
    gui = MonerochanGUI(config)
    input("Close?")

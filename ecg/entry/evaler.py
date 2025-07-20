import json
import keras
import numpy as np
import scipy.io as sio
import scipy.stats as sst

import load
import network
import util
import easygui



if __name__ == '__main__':
    import sys

    file_name = easygui.fileopenbox(default="./*.mat")
    # fmat  = open(file_name,"rb");
    print(file_name);
    a=load.predict(file_name)
    if a=="~":
        print("Signal is noisy")
    if a == "N":
        print("Signal is Normal")
    if a == "A":
        print("Signal is Arrithmia")
    if a == "O":
        print("Signal is Other Arrithmia")
    easygui.msgbox('Signal is '+a, 'Report')

    print(a)
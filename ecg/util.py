import os
import pickle

def load(dirname):
    print(os.path.join(dirname,"preproc.bin"))
    preproc_f = str.encode(os.path.join(dirname,"preproc.bin"))
    with open(preproc_f, 'rb') as fid:
        preproc = pickle.load(fid)
    return preproc

def save(preproc, dirname):
    preproc_f = os.path.join(dirname, "preproc.bin")
    with open(preproc_f, 'wb') as fid:
        pickle.dump(preproc, fid)

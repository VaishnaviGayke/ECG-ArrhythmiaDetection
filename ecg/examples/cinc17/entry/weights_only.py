
import keras
import sys

# mpath = sys.argv[1]
mpath = "model_cinc17.h5"
model = keras.models.load_model(mpath)
model.save_weights("model.hdf5")

import numpy as np
import librosa
import pickle

with open('model.pkl', 'rb') as f:
    MODEL, SCALER, PCA = pickle.load(f)

GENRE = [
    "bali",
    "batak",
    "dangdut",
    "jawa",
    "keroncong",
    "koplo",
    "melayu",
    "minang",
    "papua",
    "sumba",
    "sunda"
]

def predict(filename):
    y, sr = librosa.load(filename, res_type='kaiser_fast', duration=4.0)
    array_data = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
    m, n = array_data.shape
    array_data = array_data.reshape(1, m*n)
    array_data = SCALER.transform(array_data)
    array_data = PCA.transform(array_data)
    return GENRE[np.argmax(MODEL.predict(array_data))]
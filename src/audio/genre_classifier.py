import librosa
import numpy as np
from sklearn.externals import joblib

class GenreClassifier:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def classify(self, audio_file):
        # Load the audio file
        y, sr = librosa.load(audio_file, duration=30)
        
        # Extract features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs.T, axis=0)

        # Predict the genre
        genre_prediction = self.model.predict([mfccs_mean])
        return genre_prediction[0]
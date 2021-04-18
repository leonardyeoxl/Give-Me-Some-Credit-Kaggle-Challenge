import joblib
import configparser
import os
import pandas as pd

class Classifer:
    def __init__(self):
        model_path = self.ModelConfig(self.ConfigParse())
        self.model = self.LoadModel(model_path)

    def ConfigParse(self):
        config = configparser.ConfigParser()
        config.read(os.environ['config_path'])
        return config

    def ModelConfig(self, config):
        return config['model']['path']

    def LoadModel(self, model_path):
        return joblib.load(model_path)

    def Classify(self, input):
        df = pd.json_normalize(input)
        return int(self.model.predict(df)[0])
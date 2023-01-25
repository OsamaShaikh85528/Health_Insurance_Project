import numpy as np
import json
import config 
import pickle

class MedicalInsurance():
    def __init__(self,age, sex, bmi, children,smoker, region):
        self.age = age
        self.sex = sex 
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region

    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.json_Data = json.load(f)

    def Get_Predicted_Charges(self):
        self.load_model()
        Test_Array = np.zeros(len(self.json_Data['columns']))
        Test_Array[0] = self.age
        Test_Array[1] = self.json_Data['sex'][self.sex]
        Test_Array[2] = self.bmi
        Test_Array[3] = self.children
        Test_Array[4] = self.json_Data['Smoker'][self.smoker]
        Region_Index = self.json_Data['columns'].index(self.region)
        Test_Array[Region_Index] = 1

        print("TEST ARRAY >>", Test_Array)
        Predicted_Charges = np.around(self.model.predict([Test_Array])[0], 2)
        return Predicted_Charges

if __name__ == "__main__":
    age = 24
    sex = 'male'
    bmi = 26
    children = 3
    smoker = 'no'
    region = 'northwest'
    Med_Ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    Med_Ins.Get_Predicted_Charges()
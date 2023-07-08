
import pickle
import json
import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# import config 

class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age=age
        self.gender=gender
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+ region

    def load_model(self):
        with open("model.pkl","rb") as f:
            self.model=pickle.load(f)

        with open("Project_data.json","r") as f:
            self.json_data=json.load(f)
        

    def get_predicted_price(self):
        self.load_model()

        print(self.json_data)

        len(self.json_data["column"])
        region_index=self.json_data["column"].index(self.region)
        # southwest
        

        array = np.zeros([1,len(self.json_data["column"])])
        array[0][0] = self.age
        array[0][1] = self.json_data['gender'][self.gender]
        array[0][2] = self.bmi
        array[0][3] = self.children
        array[0][4] = self.json_data['smoker'][self.smoker]
        array[0,region_index] = 1
        
        # EX
        # A = {"gender": {"male": 1, "female": 0}}
        # A["gender"]["male"] >> 1

        #print("test array - ",array)
        predicted_charges = self.model.predict(array)
        
        return np.around(predicted_charges,3)

if __name__ == "__main__":
    
    age = 35
    gender = "male"
    bmi = 20
    children = 0
    smoker = "no"
    region = "northeast"

    

    
    med_ins = MedicalInsurance(age,gender,bmi,children,smoker,region)
    charges = med_ins.get_predicted_price()[0]
    print("charges for medicial insurance is --- ",charges)



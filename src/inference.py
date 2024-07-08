import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime

class Inference:
    def __init__(self, model_path, scaler_path):
        self.model_path = model_path
        self.scaler_path = scaler_path
        
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            self.model = pickle.load(open(self.model_path, "rb"))
            self.scaler = pickle.load(open(self.scaler_path, "rb"))
        else:
            print('Model or Standard Scaler path is not correct!')
            
    def get_string_to_datetime(self, date):
        dt = datetime.strptime(date, "%d/%m/%Y")
        return {"day": dt.day, "month": dt.month, "year": dt.year, "weekday": dt.weekday() }
   
    # Seasons
    def seasons_df(self, Seasons):
        seasons_col = ['Spring', 'Summer', 'Winter']
        seasons_data = np.zeros((1,len(seasons_col)), dtype='int')

        dataset_season = pd.DataFrame(seasons_data, columns=seasons_col)
        if Seasons in seasons_col:
            dataset_season[Seasons] = 1
        return dataset_season         
    
    def user_input(self):
        print('Enter correct information to predict Rented Bike count for a day with respect to time:')
        Date = input("Date (dd/mm//yy): ")
        Hour = int(input("Hours (24hrs format): "))
        Temperature = float(input("Temperature in C: "))
        Humidity = float(input("Humidity: "))
        Wind_speed = float(input("Wind_speed: ")) 
        Visibility = float(input("Visibility: "))
        Solar_Radiation = float(input("Solar_Radiation: "))
        Rainfall = float(input("Rainfall: "))
        Snowfall = float(input("Snowfall: "))
        Seasons	= input("Seasons (Autumn, Sprin, Summer, Winter): ")
        Holiday	= input("Holiday (Holiday/No Holiday): ")
        Functioning_Day = input("Functioning_Day (Yes/No): ")
        
        date_converted = self.get_string_to_datetime(Date)

        # Holiday
        holiday_dic = {"No Holiday": 0, "Holiday": 1}

        # Functioning day
        functioning_day_dic = {"No": 0, "Yes": 1}

        seasons_converted = self.seasons_df(Seasons)
        seasons_converted
        
        user_input_list = [Hour, Temperature, Humidity, Wind_speed, Visibility, Solar_Radiation, Rainfall, Snowfall, holiday_dic[Holiday], functioning_day_dic[Functioning_Day], date_converted["weekday"], date_converted["day"], date_converted["month"], date_converted["year"]]
        features_name = ['Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)', 'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Holiday', 'Functioning Day', 'Week Days', 'Day', 'Month', 'Year']

        df_user_input = pd.DataFrame([user_input_list], columns=features_name)
        
        final_df= pd.concat([df_user_input, seasons_converted], axis=1)
        
        return final_df
    
    def predication(self):
        final_df = self.user_input()
        scaler_for_predication = self.scaler.transform(final_df)
        pred = self.model.predict(scaler_for_predication)

        print(f"Rented Bike Demenad is {round(pred.tolist()[0])}")
        
if __name__ == "__main__":
    model_path = r"../models/random_forest_regressor_r2_0_93_v1.pkl"
    scaler_path = r"../models/scaler.pkl"
    inference = Inference(model_path, scaler_path)
    
    inference.predication()
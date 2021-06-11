import json
import csv
import pandas as pd

def BMI(height, weight):
	bmi = weight/(height**2)
	return bmi

# json_data = json.loads('[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]')  

with open("json_data.json", "r") as read_file:
    data = json.load(read_file)
    # print(data)

    bmi_list = []
    health_risk_list = []
    bmi_category_list = []

    for item in data:

        height = item['HeightCm']/100
        weight = item['WeightKg']

        bmi = BMI(height, weight)
        # print("The BMI is", format(bmi), "so ", end='')

        fieldnames = ['Gender', 'HeightCm', 'WeightKg']    
        bmi_list.append(bmi)
        # print(bmi_list)

        with open('BMI_data.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        f.close()


        if (bmi <= 18.4):
            bmi_category = bmi_category_list.append("Underweight")
            health_risk = health_risk_list.append(("Malnutrition risk"))

        elif ( bmi >= 18.5 and bmi <= 24.9):
            bmi_category = bmi_category_list.append("Normal Weight")
            health_risk = health_risk_list.append(("Low risk"))

        elif ( bmi >= 25 and bmi <= 29.9):
            bmi_category = bmi_category_list.append("Overweight")
            health_risk = health_risk_list.append(("Enhanced risk"))

        elif (  bmi >= 30 and bmi <= 34.9):
            bmi_category = bmi_category_list.append("Moderately Obese")
            health_risk_list.append(("Medium risk"))

        elif (  bmi >= 35 and bmi <= 39.9):
            bmi_category = bmi_category_list.append("Severely Obese")
            health_risk = health_risk_list.append(("High risk"))
        
        elif ( bmi >=40):
            bmi_category = bmi_category_list.append("Very Severely Obese")
            health_risk = health_risk_list.append(("Very High risk"))

        # print(health_risk_list)


    df = pd.read_csv("BMI_data.csv")
    # print(df)
    # print(bmi_list)
    df['BMI_value'] = bmi_list
    df['BMI_Category'] = bmi_category_list
    df['Health risk'] = health_risk_list

    df.to_csv('BMI_data.csv')

read_file.close()
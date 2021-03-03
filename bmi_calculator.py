import json

#Taking JSON as input, but it will be better if we ask for a json file, python will read that file and write in that file.
patient_json_data = input("Enter JSON Data(be careful while passing json): ")

#Creating bmi_category dictionary for updating patients_bmi_category_count
patient_bmi_category_dict = {'underweight':0, 'normal_weight':0, 'overweight':0, 'moderately_obese':0, 'severly_obese':0, 'very_severly_obese':0}

#Below method is used for calculating BMI, It accepts a dictionary that must consist of WeightKg and HeightCm keys.
def calculate_bmi(patient_dict):
        if type(patient_dict) is dict and patient_dict['WeightKg'] and patient_dict['HeightCm'] and patient_dict['HeightCm'] != 0:
            return round(float(patient_dict['WeightKg']) / ((float(patient_dict['HeightCm']) / 100) ** 2), 2)
        else:
            raise Exception('There is an issue in JSON, Issue might be 1) not found WeightKg in patient data, 2) not found HeightCm in patient data, 3) HeightCm is 0(zero) or 4) Not passed proper dictionary')

#Below method is adding BMI Category and Health Risk in data.
def check_bmi_category_and_health_risk(patient_dict):
    if(patient_dict['BMI']):
        if(patient_dict['BMI'] < 18.5):
            patient_dict['BMI_Category'] = 'Underweight'
            patient_dict['Health_Risk'] = 'Malnutrition risk'
            patient_bmi_category_dict['underweight'] += 1
        elif(patient_dict['BMI'] >= 18.5 and patient_dict['BMI'] < 25):
            patient_dict['BMI_Category'] = 'Normal weight'
            patient_dict['Health_Risk'] = 'Low risk'
            patient_bmi_category_dict['normal_weight'] += 1
        elif(patient_dict['BMI'] >= 25 and patient_dict['BMI'] < 30):
            patient_dict['BMI_Category'] = 'Overweight'
            patient_dict['Health_Risk'] = 'Enhanced risk'
            patient_bmi_category_dict['overweight'] += 1
        elif(patient_dict['BMI'] >= 30 and patient_dict['BMI'] < 35):
            patient_dict['BMI_Category'] = 'Moderately obese'
            patient_dict['Health_Risk'] = 'Medium risk'
            patient_bmi_category_dict['moderately_obese'] += 1
        elif(patient_dict['BMI'] >= 35 and patient_dict['BMI'] < 40):
            patient_dict['BMI_Category'] = 'Severely obese'
            patient_dict['Health_Risk'] = 'High risk'
            patient_bmi_category_dict['severly_obese'] += 1
        else:
            patient_dict['BMI_Category'] = 'Very severely obese'
            patient_dict['Health_Risk'] = 'Very high risk'
            patient_bmi_category_dict['very_severly_obese'] += 1
    else:
        raise Exception('Patient BMI not found!!')

try:
    patient_dict_list = json.loads(patient_json_data)
    for patient_dict in patient_dict_list:
        patient_dict['BMI'] = calculate_bmi(patient_dict)
        check_bmi_category_and_health_risk(patient_dict)
    #Uncomment below line if you want to print all patient data with BMI, BMI Category and Health risk
    #print(patient_dict_list)
    print("Total %d overweight people found from the given JSON" % patient_bmi_category_dict['overweight'])
except Exception:
    raise Exception('Issue in JSON Data')

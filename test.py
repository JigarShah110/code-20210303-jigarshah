import pytest
import bmi_calculator

class TestBMICalculation:
    def test_bmi_calc1(self):
        # This method contains a happy path including validated output
        assert bmi_calculator.calculate_bmi({"WeightKg":96, "HeightCm": 171}) == 32.8

    def test_bmi_calc2(self):
        # This method is verifying bmi that should not match
        assert bmi_calculator.calculate_bmi({"WeightKg":50, "HeightCm": 162}) == 27

    def test_bmi_category(self):
        patient_bmi_dict = {'BMI': 28}
        bmi_calculator.check_bmi_category_and_health_risk(patient_bmi_dict)
        assert patient_bmi_dict['BMI_Category'] == 'Overweight'

    def test_bmi_category2(self):
        patient_bmi_dict={'BMI': 37}
        bmi_calculator.check_bmi_category_and_health_risk(patient_bmi_dict)
        assertpatient_bmi_dict['BMI_Category']=='Underweight'

def print_patient_records(patients):
    """
    Prints the medical records of patients in a structured format.

    :param patients: A dictionary containing patient data.
    """
    print("Medical Records:")
    print("=" * 80)

    for patient in patients.values():
        print("ID:", patient['Document_Number'])
        print("Name:", patient['Name'])
        print("Gender:", patient['Gender'])
        print("Date of Birth:", patient['Date_of_Birth'].strftime("%Y-%m-%d"))
        print("Blood Pressure:", patient['Blood_Pressure'])
        print("Temperature (°C):", patient['Temperature'])
        print("Oxygen Saturation (%):", patient['Oxygen_Saturation'])
        print("Respiratory Rate (rpm):", patient['Respiratory_Rate'])
        print("Progress Note:", patient['Progress_Note'])
        print("Diagnostic Image Code:", patient['Diagnostic_Image_Code'])
        print("Laboratory Test Results:", patient['Laboratory_Test_Results'])
        print("Prescribed Medications:", patient['Prescribed_Medications'])
        
        if patient['Treatment_Time'] is not None:
            print("Treatment Time (minutes):", patient['Treatment_Time'])
        
        print("-" * 80)

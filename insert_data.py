from datetime import datetime

class InsertData:
    """
    Class for inserting patient data into a medical clinic system.
    """

    def __init__(self):
        """
        Initializes an object of the InsertData class.
        """
        self.patients = {}

    @staticmethod
    def validate_number(message):
        """
        Validates and returns a non-negative number entered by the user.

        :param message: The message to display to the user for entering the number.
        :return: The non-negative number entered by the user.
        """
        while True:
            try:
                number = float(input(message))
                if number >= 0:
                    return number
                print("Error. It must be a non-negative number.")
            except ValueError:
                print("Error. You must enter a valid number.")

    @staticmethod
    def insert_patient(patients, patient_counter, discharge_counter, total_attention_time):
        """
        Inserts a patient's data into the clinic's system.

        :param patients: The dictionary of existing patients.
        :param patient_counter: The patient counter.
        :param discharge_counter: The discharge counter.
        :param total_attention_time: Total time of patient attention.
        :return: The new values of patient_counter, discharge_counter, and total_attention_time.
        """
        while True:
            print("-" * 80)
            document_number = InsertData.validate_number("Document Number: ")
            
            name = input("Name: ")

            # Validate gender
            gender = input("Gender (M/F): ").upper()
            while gender != "M" and gender != "F":
                gender = input("Error. Gender (M/F): ").upper()

            # Validate date of birth
            while True:
                try:
                    date_of_birth_str = input("Enter your date of birth (YYYY-MM-DD): ")
                    date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Incorrect date format. Please use YYYY-MM-DD format.")
                    continue

            blood_pressure = InsertData.validate_number("Blood Pressure: ")
            temperature = InsertData.validate_number("Temperature (°C): ")
            oxygen_saturation = InsertData.validate_number("Oxygen Saturation (%): ")
            respiratory_rate = InsertData.validate_number("Respiratory Rate (rpm): ")
            progress_note = input("Progress Note: ")
            diagnostic_image_code = input("Diagnostic Image Code: ")
            laboratory_test_results = input("Laboratory Test Results: ")
            prescribed_medications = input("Prescribed Medications: ")
            
            # Determine if the patient is still in the clinic
            patient_status = InsertData.validate_number("Is the patient still in the clinic? [1]: Yes, [2]: No: ")
            while patient_status != 1 and patient_status != 2:
                patient_status = InsertData.validate_number("Error. Select [1]: Yes or [2]: No: ")
            
            # Determine the average attention time
            if patient_status == 2:
                attention_time = InsertData.validate_number("Attention time (minutes): ")
                discharge_counter += 1
                total_attention_time += attention_time

            patients[document_number] = {
                'Document_Number': document_number,
                'Name': name,
                'Gender': gender,
                'Date_of_Birth': date_of_birth,
                'Blood_Pressure': blood_pressure,
                'Temperature': temperature,
                'Oxygen_Saturation': oxygen_saturation,
                'Respiratory_Rate': respiratory_rate,
                'Progress_Note': progress_note,
                'Diagnostic_Image_Code': diagnostic_image_code,
                'Laboratory_Test_Results': laboratory_test_results,
                'Prescribed_Medications': prescribed_medications,
                'Treatment_Time': attention_time if patient_status == 2 else None
            }

            patient_counter += 1
            
            # Ask if they want to continue
            continue_input = input("Do you want to continue (y/n): ")
            if continue_input.lower() != "y":
                break
            print("-" * 80)

        return patient_counter, discharge_counter, total_attention_time
        # We need to return this data to understand the clinic's occupancy.

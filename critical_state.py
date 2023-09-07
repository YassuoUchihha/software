from datetime import datetime

class CriticalStateEvaluator:
    """
    Class that evaluates the critical state of a patient.
    """

    @staticmethod
    def evaluate_state(patient):
        """
        Evaluate the critical state of a patient and print the result.

        :param patient: A dictionary containing the patient's data.
        """
        for patient in patient.values():
            print("ID:", patient['Document_Number'], "\tName:", patient['Name'])
            print("=" * 80)
            i = 0
            current_date = datetime.now()
            age = current_date.year - patient['Date_of_Birth'].year - (
                        (current_date.month, current_date.day) < ((patient['Date_of_Birth']).month,
                                                                  (patient['Date_of_Birth']).day))

            # Evaluate the patient's temperature
            if patient['Temperature'] >= 41 or patient['Temperature'] <= 35:
                i += 1
                if patient['Temperature'] >= 41:
                    print("[The patient has Hyperthermia]")
                    print(
                        "Recommendations: Offer cold liquids, such as water or sports drinks without caffeine or alcohol, to help rehydrate the patient. Dehydration can worsen hyperthermia.\n")
                else:
                    print("[The patient has Hypothermia]")
                    print("Recommendations: Move the patient to a warmer place protected from wind and humidity.\n")

            # Evaluate the patient's respiratory rate based on age
            if (patient['Respiratory_Rate'] > 40 or patient['Respiratory_Rate'] < 24) and (
                    age == 1 and age <= 5):
                if patient['Respiratory_Rate'] > 40:
                    print("[Respiratory Rate is very high]")
                    print(
                        "Recommendations: A doctor may prescribe medications to treat tachypnea if it is related to specific medical conditions, such as asthma or chronic obstructive pulmonary disease (COPD).\n")

                else:
                    print("[Respiratory Rate is very low]")
                    print(
                        "Recommendations: If bradypnea is suspected to be a side effect of certain medications, a doctor may adjust the dose or switch to a safer alternative.\n")

                i += 1
            elif (patient['Respiratory_Rate'] > 30 or patient['Respiratory_Rate'] < 18) and (
                    age >= 6 and age <= 13):
                if patient['Respiratory_Rate'] > 30:
                    print("[Respiratory Rate is very high]")
                    print(
                        "Recommendations: A doctor may prescribe medications to treat tachypnea if it is related to specific medical conditions, such as asthma or chronic obstructive pulmonary disease (COPD).\n")

                else:
                    print("[Respiratory Rate is very low]")
                    print(
                        "Recommendations: If bradypnea is suspected to be a side effect of certain medications, a doctor may adjust the dose or switch to a safer alternative.\n")

                i += 1
            elif ((patient['Respiratory_Rate'] > 12 and patient['Respiratory_Rate'] > 16) or (
                    patient['Respiratory_Rate'] < 16 and patient['Respiratory_Rate'] < 12)) and (
                    age >= 14):
                if patient['Respiratory_Rate'] > 16:
                    print("[Respiratory Rate is very high]")
                    print(
                        "Recommendations: A doctor may prescribe medications to treat tachypnea if it is related to specific medical conditions, such as asthma or chronic obstructive pulmonary disease (COPD).\n")

                else:
                    print("[Respiratory Rate is very low]")
                    print(
                        "Recommendations: If bradypnea is suspected to be a side effect of certain medications, a doctor may adjust the dose or switch to a safer alternative.\n")

                i += 1

            # Evaluate the patient's blood pressure
            if (patient['Blood_Pressure'] > 150) or (patient['Blood_Pressure'] < 50):
                if (patient['Blood_Pressure'] > 150):
                    print("[High Blood Pressure]")
                    print(
                        "Recommendations: Medications like hydrochlorothiazide help eliminate excess sodium and water from the body, reducing the circulating fluid volume and, consequently, blood pressure.\n")
                    i += 1
                else:
                    print("[Low Blood Pressure]")
                    print(
                        "Recommendations: Fludrocortisone helps retain sodium and increase blood volume, which can raise blood pressure.\n")
                    i += 1

            # Evaluate the patient's oxygen saturation
            if patient['Oxygen_Saturation'] < 85:
                print(f"[Oxygen Saturation [{patient['Oxygen_Saturation']}%] is very low, the patient may have Severe Hypoxia]")
                print("Recommendations: Provide supplemental oxygen to increase blood oxygen levels and improve saturation.")
                i += 1

            print("=" * 80)
            if i > 0:
                print("The patient may have a chronic condition")
            else:
                print("The patient does not show signs of a chronic condition")
            print("=" * 80, "\n\n")

from print_patient_data import print_patient_records
from insert_data import InsertData
from bed import Bed
from critical_state import CriticalStateEvaluator

def main():
    """
    Main function of the program.
    """
    patient_dictionary = InsertData()
    evaluate = CriticalStateEvaluator()

    admissions, discharges, time = 0, 0, 0

    while True:
        def print_menu():
            """
            Print the main menu.
            """
            print("-" * 80)
            print("╔══════════════════════════════════════╗")
            print("║               Menu                   ║")
            print("║══════════════════════════════════════║")
            print("║ [1]. Enter Patient                   ║")
            print("║ [2]. Print Patient Medical History   ║")
            print("║ [3]. Clinic Occupancy Information    ║")
            print("║ [4]. Patient Status                  ║")
            print("║ [5]. Exit Program                    ║")
            print("╚══════════════════════════════════════╝")
            print("-" * 80)

        print_menu()
        choice = InsertData.validate_number("Enter the number: ")
        print("-" * 80)

        while choice < 1 or choice > 5:
            choice = InsertData.validate_number("Error. Enter the number: ")

        if choice == 5:
            break

        if choice == 1:
            # Enter patient
            admissions, discharges, time = InsertData.insert_patient(patient_dictionary.patients, admissions, discharges, time)
        elif choice == 2:
            # Print medical history of patients
            print_patient_records(patient_dictionary.patients)
        elif choice == 3:
            # Get clinic occupancy information
            Bed.occupancy(admissions, discharges)  # You can pass admissions and discharges as parameters
            Bed.average_stay(time, discharges)  # You can pass total stay time and discharges as parameters
            Bed.admission_discharge_count(admissions, discharges)  # You can pass admissions and discharges as parameters
        elif choice == 4:
            # Evaluate patient status
            patient_to_evaluate = patient_dictionary.patients  # Get the patient to evaluate (adjust this line based on your logic)
            evaluate.evaluate_state(patient_to_evaluate)  # Call the function with the patient as an argument

if __name__ == "__main__":
    main()

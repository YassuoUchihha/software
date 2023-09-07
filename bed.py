class Bed:
    """
    Class that manages information related to bed availability in a hospital.
    """

    @staticmethod
    def occupancy(current_admitted_patients, discharged_patients):
        """
        Calculates and displays the number of occupied beds and the total occupancy in the hospital.

        :param current_admitted_patients: Current number of patients in the hospital.
        :param discharged_patients: Number of patients who have been discharged.
        """
        total_beds = 300
        available_beds = total_beds - (current_admitted_patients-discharged_patients)
        print("The total number of available beds at the moment is:", available_beds)
        total_occupancy = ((current_admitted_patients-discharged_patients) * 100) / total_beds
        print(f"The total bed occupancy is: {total_occupancy:.2f}%")

    @staticmethod
    def average_stay(total_stay_time, discharged_patients):
        """
        Calculates and displays the average time patients have spent in the hospital.

        :param total_stay_time: Total accumulated stay time of all patients.
        :param discharged_patients: Number of patients who have been discharged.
        """
        if total_stay_time == 0:
            print("Currently, there is no information available about the average stay time.")
        else:
            average_stay = total_stay_time / discharged_patients
            print(f"The average stay time per patient is: {average_stay:.2f} minutes")

    @staticmethod
    def admission_discharge_count(total_admissions, discharged_patients):
        """
        Displays the total number of admitted patients and the number of patients who have been discharged.

        :param total_admissions: Total number of patients admitted to the hospital.
        :param discharged_patients: Number of patients who have been discharged.
        """
        print("The total number of admitted patients is:", total_admissions)
        print("The total number of discharged patients is:", discharged_patients)

class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class HospitalSystem:
    def __init__(self):
        self.specializations = [[] for _ in range(20)]
        self.status_names = {0: 'Normal', 1: 'Urgent', 2: 'Super-urgent'}

    def add_patient(self):
        while True:
            try:
                spec = int(input("Enter the specialization (1-20): "))
                if spec < 1 or spec > 20:
                    raise ValueError("Invalid specialization number.")
                if len(self.specializations[spec-1]) >= 10:
                    raise ValueError("Sorry, the queue for this specialization is full.")
                break
            except ValueError as e:
                print(str(e))
        while True:
            name = input("Enter the name of the patient: ")
            if not (name.isalpha() or " " in name):
                print("Invalid name. Please enter only alphabetical characters and spaces.")
            else:
                break
        while True:
            try:
                status = int(input("Enter the status (0=normal, 1=urgent, 2=super-urgent): "))
                if status not in [0, 1, 2]:
                    raise ValueError("Invalid status number.")
                queue = self.specializations[spec-1]
                if status == 0:
                    queue.append(Patient(name, status))
                else:
                    i = 0
                    while i < len(queue) and queue[i].status <= status:
                        i += 1
                    queue.insert(i, Patient(name, status))
                break
            except ValueError as e:
                print(str(e))

    def print_patients(self):
        for spec, queue in enumerate(self.specializations):
            if queue:
                print(f"Specialization {spec+1}:")
                for i, patient in enumerate(queue):
                    print(f"{i+1}. {patient.name} ({self.status_names[patient.status]})")

    def get_next_patient(self):
        while True:
            try:
                spec = int(input("Enter the specialization (1-20): "))
                if spec < 1 or spec > 20:
                    raise ValueError("Invalid specialization number.")
                queue = self.specializations[spec-1]
                if not queue:
                    raise ValueError("No patients for this specialization.")
                break
            except ValueError as e:
                print(str(e))
        patient = queue.pop(0)
        print(f"Next patient for specialization {spec}: {patient.name} ({self.status_names[patient.status]})")

    def remove_leaving_patient(self):
        while True:
            try:
                spec = int(input("Enter the specialization (1-20): "))
                if spec < 1 or spec > 20:
                    raise ValueError("Invalid specialization number.")
                queue = self.specializations[spec-1]
                if not queue:
                    raise ValueError("No patients for this specialization.")
                break
            except ValueError as e:
                print(str(e))
        while True:
            name = input("Enter the name of the leaving patient: ")
            if not (name.isalpha() or " " in name):
                print("Invalid name. Please enter only alphabetical characters and spaces.")
            else:
                break
        for i, patient in enumerate(queue):
            if patient.name == name:
                del queue[i]
                print(f"Patient {name} removed from the queue.")
                break
        else:
            print(f"Patient {name} not found in the queue.")

hospital = HospitalSystem()

while True:
    print("Hospital System Menu:")
    print("1. Add patient")
    print("2. Print patients")
    print("3. Get next patient")
    print("4. Remove leaving patient")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        hospital.add_patient()
    elif choice == "2":
        hospital.print_patients()
    elif choice == "3":
        hospital.get_next_patient()
    elif choice == "4":
        hospital.remove_leaving_patient()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


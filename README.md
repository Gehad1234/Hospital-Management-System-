# Hospital-Management-System-
 (OOP with Python)
This Python code defines a simple hospital system that manages patient queues based on specialization and urgency status. Here's an overview of the classes and their methods:

1. `Patient` class:
   - The `Patient` class represents a patient with attributes `name` (patient's name) and `status` (patient's urgency status: 0 for normal, 1 for urgent, and 2 for super-urgent).

2. `HospitalSystem` class:
   - The `HospitalSystem` class represents the overall hospital system and includes the following methods:

   - `__init__(self)`: Initializes the hospital system with 20 specializations and a dictionary to map status numbers to status names.
   - `add_patient(self)`: Allows the user to add a new patient to a specialization queue. It prompts for specialization number, patient name, and urgency status.
   - `print_patients(self)`: Prints the list of patients in each specialization queue along with their names and urgency statuses.
   - `get_next_patient(self)`: Retrieves and prints the next patient from a specialization queue based on their urgency status.
   - `remove_leaving_patient(self)`: Allows the user to remove a patient from a specialization queue by entering the specialization number and the patient's name.

3. The main part of the code:
   - The main loop continuously displays a menu of options for interacting with the hospital system.
   - Users can choose to add a patient, print the patient queues, get the next patient, remove a leaving patient, or quit the program.

This code simulates a basic hospital system with multiple specializations and different urgency levels for patient queues. Users can add, view, and manage patients within the system.

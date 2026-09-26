import json
from datetime import datetime

# Function to take ID from Student
def get_id():

    try:
        return int(input("Enter your ID: "))
    
    except ValueError:
        print("ID must be a number.")
        return None

# Function to Add a Student to the Json File
def add_student (id, name, age, track):
    
    try:
        with open ("students.json", "r") as f:
            data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        data = {"students": []}

    new_student = {"id": id,"name": name, "age": age, "track": track}
    data["students"].append(new_student)

    try:
        with open ("students.json", "w") as f:
            json.dump(data, f)

        with open ("logs.txt", "a") as f:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            f.write(f"[{timestamp}] Added student {id}\n")

        print(f"Student with id {id} is added successfully!")

    except Exception as e:
        print(f"Can't Save Data To File: {e}")

    

# Function to View Students from the Json File
def view_students():
    
    try:
        with open ("students.json", "r") as f:
            data = json.load(f)

            if not data["students"]:
                print("No Students Found.")
            else:    
                print("========== Students List ==========")
                for i, student in enumerate(data["students"], start=1):
                    print(f"Student No.{i}:-")
                    print(f"ID: {student['id']}\nName: {student['name']}\nAge: {student['age']}\nTrack: {student['track']}")
                    print("-----------------------------------")

    except(FileNotFoundError, json.JSONDecodeError):
        print("Can't Read Data From File.")

# Function to Search for a Student from the Json File
def search_student(id):

    try:
        with open ("students.json", "r") as f:
            data = json.load(f)

            found = False

            for student in data["students"]:

                if id == student["id"]:
                    print(f"ID: {student['id']}\nName: {student['name']}\nAge: {student['age']}\nTrack: {student['track']}")
                    
                    found = True
                    break

            if not found:
                print("Student doesn't Exist.")
        
        with open ("logs.txt", "a") as f:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            status = "successfully" if found else "unsuccessfully"
            f.write(f"[{timestamp}] Searched for student {id}, result {status}\n")

    except(FileNotFoundError, json.JSONDecodeError):
        print("Can't Read Data From File.")

# Function to Update a Student in the Json File
def update_student(id):

    try:
        with open ("students.json", "r") as f:
            data = json.load(f)

            found = False

            for student in data["students"]:

                if id == student["id"]:
                    student["name"] = input("Enter your Name: ")

                    try:
                        student["age"] = int(input("Enter your Age: "))
                    except ValueError:
                        print("Age must be a number.")
                        return
                    
                    student["track"] = input("Enter your Track: ")
                    
                    found = True
                    break

            if not found:
                print("Student doesn't Exist\nCan't Update Student Information.")
                return
        
        with open ("students.json", "w") as f:
            json.dump(data, f)

        with open ("logs.txt", "a") as f:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            f.write(f"[{timestamp}] Updated student {id}\n")

        print(f"Student with id {id} is updated successfully!")
    
    except(FileNotFoundError, json.JSONDecodeError):
        print("Can't Read Data From File.")

# Function to Delete a Student from the Json File
def delete_student(id):

    try:
        with open ("students.json", "r") as f:
            data = json.load(f)

            found = False

            for student in data["students"]:

                if id == student["id"]:
                    data["students"].remove(student)

                    found = True
                    break

            if not found:
                print("Student doesn't Exist\nCan't Delete Student Information.")
                return
        
        with open ("students.json", "w") as f:
            json.dump(data, f)

        with open ("logs.txt", "a") as f:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            f.write(f"[{timestamp}] Deleted student {id}\n")

        print(f"Student with id {id} is deleted successfully!")

    except(FileNotFoundError, json.JSONDecodeError):
        print("Can't Read Data From File.")
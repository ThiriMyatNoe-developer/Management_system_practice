# ### Problem 2: Student Attendance Management System

# **Scenario:**

# A school wants a simple system to manage student attendance.

# You need to create a program that records which students are present and absent each day.

# **Requirements:**

# 1. Store student IDs and names using a dictionary.
# 2. Store attendance records using a list.
# 3. Allow the teacher to mark students as Present or Absent.
# 4. Prevent the same student from being marked twice on the same day.
# 5. Display the list of present students.
# 6. Display the list of absent students.
# 7. Calculate the total number of present and absent students.
# 8. Allow the teacher to search for a student by ID.

# **Expected Features:**
# - View Students
# - Mark Attendance
# - View Present Students
# - View Absent Students
# - Search Student
# - Exit

# ---


students = {
    "101": "Aung Aung",
    "102": "Mg Mg",
    "103": "Su Su",
    "104": "Hla Hla",
    "105": "Kyaw Kyaw"
}

attendance = []

while True:
    print("\n--- Student Attendance Management System ---")
    print("1. View Students")
    print("2. Mark Attendance")
    print("3. View Present Students")
    print("4. View Absent Students")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Student List ---")
        for student_id, name in students.items():
            print(student_id, name)

    elif choice == "2":
        student_id = input("Enter student ID: ")

        if student_id in students:
            if student_id in attendance:
                print("Attendance already marked!")
            else:
                status = input("Enter status (P/A): ").upper()

                if status == "P" or status == "A":
                    attendance.append({
                        "id": student_id,
                        "status": status
                    })
                    print("Attendance marked successfully!")
                else:
                    print("Invalid status! Enter P or A.")
        else:
            print("Error! Student ID does not exist.")

    elif choice == "3":
        print("\n--- Present Students ---")
        count = 0

        for record in attendance:
            if record["status"] == "P":
                print(record["id"], students[record["id"]])
                count += 1

        print("Total Present:", count)

    elif choice == "4":
        print("\n--- Absent Students ---")
        count = 0

        for record in attendance:
            if record["status"] == "A":
                print(record["id"], students[record["id"]])
                count += 1

        print("Total Absent:", count)

    elif choice == "5":
        search_id = input("Enter student ID: ")

        if search_id in students:
            print("Student Name:", students[search_id])

            for record in attendance:
                if record["id"] == search_id:
                    print("Attendance Status:", record["status"])
                    break
            else:
                print("Attendance not marked yet.")
        else:
            print("Student not found!")

    elif choice == "6":
        print("Thank you for using Attendance Management System!")
        break

    else:
        print("Invalid choice! Please choose (1-6).")

        
            
            
    
        

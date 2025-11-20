import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    name = "pothyshwer"
    rollno = "147"
    print("No input given - using default value:")
    print("Student Name:", name)
    print("Roll Number:", rollno)

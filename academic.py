GRADE_POINTS = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

courses = []

try:
    file = open("grades.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            courses.append({
                "name": parts[0],
                "credits": float(parts[1]),
                "grade": parts[2]
            })
    file.close()
except FileNotFoundError:
    pass

while True:
    print("\n--- MENU ---")
    print("1. View Courses & GPA")
    print("2. Add Course")
    print("3. Predict Target GPA")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        if not courses:
            print("No courses added yet.")
        else:
            total_points = 0
            total_credits = 0
            for c in courses:
                print(f"Course: {c['name']} | Credits: {c['credits']} | Grade: {c['grade']}")
                if c['grade'] in GRADE_POINTS:
                    total_points += c['credits'] * GRADE_POINTS[c['grade']]
                    total_credits += c['credits']
            
            if total_credits > 0:
                print(f"\nCurrent GPA: {total_points / total_credits:.2f}")
            else:
                print("\nNo completed courses to calculate GPA.")

    elif choice == "2":
        name = input("Enter course name: ")
        credits = float(input("Enter credits: "))
        grade = input("Enter grade (A, B, C, D, F, or leave blank if pending): ").upper()
        
        if grade == "":
            grade = "PENDING"
            
        courses.append({"name": name, "credits": credits, "grade": grade})
        
        file = open("grades.txt", "a")
        file.write(f"{name},{credits},{grade}\n")
        file.close()
        
        print("Course added successfully!")

    elif choice == "3":
        target = float(input("Enter your target GPA: "))
        earned_points = 0
        completed_credits = 0
        pending_credits = 0

        for c in courses:
            if c['grade'] in GRADE_POINTS:
                earned_points += c['credits'] * GRADE_POINTS[c['grade']]
                completed_credits += c['credits']
            else:
                pending_credits += c['credits']

        if pending_credits == 0:
            print("No pending courses to predict.")
        else:
            total_credits = completed_credits + pending_credits
            needed_points = (target * total_credits) - earned_points
            needed_avg = needed_points / pending_credits

            print(f"Needed Average Grade Point in pending courses: {needed_avg:.2f}")
            if needed_avg > 4.0:
                print("Result: Impossible (Above 4.0).")
            elif needed_avg <= 0:
                print("Result: Already achieved!")
            else:
                print("Result: Achievable.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
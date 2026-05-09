# Expert System for Employee Performance Evaluation

print("====================================")
print(" Employee Performance Expert System ")
print("====================================")

attendance = int(input("Enter Attendance Percentage: "))
projects = int(input("Enter Number of Projects Completed: "))
communication = int(input("Enter Communication Skill Rating (1-10): "))

print("\nPerformance Evaluation Result:\n")

if attendance >= 90 and projects >= 5 and communication >= 8:

    print("Performance: EXCELLENT")
    print("Recommendation: Eligible for Promotion")

elif attendance >= 75 and projects >= 3 and communication >= 6:

    print("Performance: GOOD")
    print("Recommendation: Appreciated for Good Work")

elif attendance >= 60 and projects >= 2 and communication >= 4:

    print("Performance: AVERAGE")
    print("Recommendation: Needs Improvement")

else:

    print("Performance: POOR")
    print("Recommendation: Training Required")
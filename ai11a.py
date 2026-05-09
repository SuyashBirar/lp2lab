# Expert System for Hospital and Medical Facilities

print("====================================")
print(" Hospital Expert System ")
print("====================================")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()

print("\nDiagnosis Result:\n")

if fever == "yes" and cough == "yes":

    print("Possible Disease: Flu or Viral Infection")
    print("Advice: Consult a doctor and take rest")

elif fever == "yes" and headache == "yes":

    print("Possible Disease: Migraine or Infection")
    print("Advice: Drink water and consult doctor")

elif cough == "yes":

    print("Possible Disease: Cold or Allergy")
    print("Advice: Take proper medication")

else:

    print("You seem healthy")
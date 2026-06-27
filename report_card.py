#
p = float(input("Physics के मार्क्स डालें: "))
c = float(input("Chemistry के मार्क्स डालें: "))
m = float(input("Maths के मार्क्स डालें: "))


marks_dict = {
    "Physics": p,
    "Chemistry": c,
    "Maths": m
}


total_marks = 0
for subject, marks in marks_dict.items():
    total_marks = total_marks+marks

percentage = (total_marks / 300) * 100


with open("report_card.txt", "w") as f:
    f.write("====== YOUR REPORT CARD ======\n")
    

    for subject, marks in marks_dict.items():
        f.write(f"{subject}: {marks}\n")
        
    f.write("------------------------------\n")
    f.write(f"Total Marks: {total_marks}/300\n")
    f.write(f"Percentage: {percentage:}%\n")
    f.write("==============================\n")

print("बधाई हो! आपकी 'report_card.txt' फाइल बन चुकी है।")


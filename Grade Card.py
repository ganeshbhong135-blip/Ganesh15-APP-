sub1=float(input("Enter marks for subject 1:"))
sub2=float(input("Enter marks for subject 2:"))
sub3=float(input("Enter marks for subject 3:"))
sub4=float(input("Enter marks for subject 4:"))
sub5=float(input("Enter marks for subject 5:"))

total=sub1+sub2+sub3+sub4+sub5
percentage=total/5

if percentage>=75:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="C"
elif percentage>=40:
    grade="Pass"
else:
    grade="Fail"


print("\n RESULT ")
print("Total Marks:",total)
print("Percentage:{:.2f}%".format(percentage))
print("Grade:", grade)

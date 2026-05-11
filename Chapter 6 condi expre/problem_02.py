marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))

# Check for the total percentage
total_persentage = ((100)*(marks1 + marks2 + marks3)/300)

if(total_persentage>=40 and marks1>=33 and marks2>=33 and marks2>=33):
    print("You are pass", total_persentage)

else:
    print(" You failed, try again next year!", total_persentage)
    
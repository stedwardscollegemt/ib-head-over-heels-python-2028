# input name
name = input("Enter your name: ")
 
# test scores
test1 = float(input("first test score: "))
test2 = float(input("second test score: "))
test3 = float(input("third test score: "))
 
# average of the tests
average = (test1 + test2 + test3) / 3
 
print(name,"average:", average)
 
# grade of the tests averages
if average >= 80:
    print("grade: A")
 
elif average >= 70:
    print("grade: B")
 
elif average >= 60:
    print("grade: C")
 
elif average >= 50:
    print("grade: D")
 
elif average < 50:
    print("grade: F")
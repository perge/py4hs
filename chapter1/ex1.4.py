import time

print("Σκέψου έναν αριθμό")
time.sleep(3)
a=int(input("Ποιό είναι το υπόλοιπο της διαίρεσης ου αριθμού με το 3;"))
b=int(input("Ποιό είναι το υπόλοιπο της διαίρεσης με το 5;"))
c=int(input("Ποίό είναι το υπόλοιπο της διαίρεσης με το 7;"))

time.sleep(1)
print("Σκέφτηκες το ....", end=" ")

a=70*a + 21*b + 15*c
a=a%105

print(a)



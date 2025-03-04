list1 = [100, 200, 300, 'A', 400, 500]

all_integers = all(isinstance(item, int) for item in list1)

# طباعة النتيجة
if all_integers:
    print("All Element is Integer")
else:
    print("there Element is Non Integer")

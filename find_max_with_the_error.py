def find_max():
    numbers=input("Enter the numbers that you want to find the largest of : ")
    numbers_list=numbers.split(" ")
    max=numbers_list[0]
    for i in numbers_list:
        if i>max:
            max=i
    print(max)
find_max()
#I get false answers some times. Try 3 4 5 6 9 20 1000
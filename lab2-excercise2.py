def display_main_menu():
        print("Enter some numbers seperated by commas (e.g. 5,6,7)")


def main():
    print("LAB 2")
    display_main_menu()
    num_list = input()
    people = num_list.split(",")
    print(people)
    n=0
    x = 0
    for i in range(0, int(people[n])):
        total = int(people[n])
        n += 1
        x = x + total

        print(x)
        average = x / n
        print("Average is: "+ str(average))





if __name__ == "__main__":
    main()
def calculate_sum(total_number):
    try:
        add = 0
        entered_numbers = []
        for i in range(int(total_number)):
            b = float(input(f"Enter number {i + 1}: "))
            add = add + b
            entered_numbers.append(b)

        for index, Entered_number in enumerate(entered_numbers):
            if index == len(entered_numbers) - 1:
                print(f" + {Entered_number}")
            else:
                print(f"   {Entered_number}")

        print("-------------------")
        print(f'   {add}')
        print("-------------------")

    except ValueError:
        print("Enter numbers only")


a = float(input("How many numbers do you want to add: "))
calculate_sum(a)

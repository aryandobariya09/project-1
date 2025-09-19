def main():
    print("Welcome to the Pattern Generator and Number Analyzer!")
    while True:
        print("Select an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_pattern()
        elif choice == "2":
            analyze_numbers()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def generate_pattern():
    rows = int(input("Enter the number of rows for the pattern: "))
    print("Star Pattern:")
    for i in range(1, rows + 1):
        print("*" * i)

def analyze_numbers():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    total_sum = 0

    for number in range(start, end + 1):
        if number % 2 == 0:
            print("Number",number," is Even")
        else:
            print("Number" ,number," is Odd")
        total_sum += number

    print("Sum of all numbers from" ,start," to" ,end," is" ,total_sum)

if __name__ == "__main__":
    main()
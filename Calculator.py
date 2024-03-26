class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return "Can't Divide by zero"
        else:
            return x / y

    def calculate(self):
        while True:
            print("Calculator")
            print("Select the following Operation")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            print("Please Enter Your Choice")
            choice = int(input("Enter your choice: "))
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break
            elif choice in (1, 2, 3, 4):
                x = float(input("Enter First Number: "))
                y = float(input("Enter Second Number: "))

                if choice == 1:
                    print("Addition is:", self.add(x, y))
                elif choice == 2:
                    print("Subtraction is:", self.sub(x, y))
                elif choice == 3:
                    print("Multiplication is:", self.mul(x, y))
                elif choice == 4:
                    print("Division is:", self.div(x, y))
            else:
                print("Please Enter a valid choice")


calc = Calculator()   # Define object

calc.calculate()     # Call Method in the above class

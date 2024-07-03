def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе!"
    return x / y

def calculator():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    
    while True:
        choice = input("Введіть номер операції (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))
            except ValueError:
                print("Будь ласка, введіть коректне число.")
                continue
            
            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Невірний вибір, спробуйте ще раз.")
        
        next_calculation = input("Бажаєте виконати ще одну операцію? (так/ні): ")
        if next_calculation.lower() != 'так':
            break

if __name__ == "__main__":
    calculator()

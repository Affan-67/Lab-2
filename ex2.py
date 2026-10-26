def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    user = input("Enter Number : ")
    y = user.split(",")
    print(y)
    return y

def calc_average_temperature(list):
    number = [float(x) for x in list]
    average = sum(number) / len(number)
    print(average)
    return average

def sort_temperature(list):
    number = [float(x) for x in list]
    number.sort()
    print(number)

def calc_min_max_temperature(list):
    max_value = max(list)
    min_value = min(list)

    print("Maximum:", max_value)
    print("Minimum:", min_value)

    
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    sort_temperature(num_list)
    calc_min_max_temperature(num_list)
    

if __name__ == "__main__":
    main()

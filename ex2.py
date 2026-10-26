
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
    return number


def calc_min_max_temperature(list):
    number = [float(x) for x in list]
    max_value = max(number)
    min_value = min(number)

    print("Maximum:", max_value)
    print("Minimum:", min_value)


def calc_median_temperature(temp_list):
    n = len(temp_list)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return temp_list[mid]
    else:
        return (temp_list[mid - 1] + temp_list[mid]) / 2


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    sorted_list = sort_temperature(num_list)
    calc_min_max_temperature(num_list)
    median = calc_median_temperature(sorted_list)
    print("Median is:", median)


if __name__ == "__main__":
    main()

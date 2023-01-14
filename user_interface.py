import calendar


def should_use_recommended_settings():
    print(
        "Hi, I'm going to evaluate using evolutionary algorithm the tempature. You can decide to enter your own settings or to use our default ones")
    user_input = input("Would you like to enter your own settings? yes/no\n")
    if user_input.__eq__("yes"):
        return False
    return True


def get_init_depth(use_default_settings):
    if use_default_settings:
        return 2, 7
    min_depth = int(input("choose minimum of initial depth:\n"))
    max_depth = int(input("choose maximum of initial depth:\n"))
    return min_depth, max_depth


def get_bloat_weight(use_default_settings):
    if use_default_settings:
        return 0.0001
    return float(input("choose bloat weight:\n"))


def get_population_size(use_default_settings):
    if use_default_settings:
        return 300
    return int(input("choose population size:\n"))


def get_max_generation(use_default_settings):
    if use_default_settings:
        return 500
    return int(input("choose max generation:\n"))


def check_temperature_of_dates_from_user(algo):
    print("Enter a date you want to check in this format DD.MM.YYYY, when you want to enter stop")
    while True:
        user_input = input("Enter your input:\n")
        if user_input == "stop":
            break
        else:
            date = user_input.split(".")
            print(f'The temperature Expected is: {algo.execute(month=date[0], day=date[1], year=date[2])}')


def print_predicted_temperatures_for_year(algo, year):
    print(f'Expected temperatures for {year}:')
    for month in range(1, 13):
        print(f'Month: {calendar.month_name[month]}, Expected temperature: {algo.execute(month=month, day=1, year=year)}')


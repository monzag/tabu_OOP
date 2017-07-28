def print_all_events(events):
    number = 1
    for item in events:
        print(number, item)
        number += 1


def print_main_menu():
    print("""
    Chose option
    1. Book private mentoring
    2. Book checkpoint
    3. Show all my event
    4. Cancel event
    5. Rescheduling event
    0. Exit""")


def print_goodbye():
    print("byebye")


def get_choice():
    return input("Chose option: ")


def get_checkpoit_details():
    return get_event_date()


def get_event_date():
    return input('Enter the date dd-mm-yyyy: ')


def get_prefered_metor():
    return input('Enter prefered metor: ')


def choose_mentor():
    list_of_mentors = ['Agnieszka Koszany', 'Mateusz Ostafil', 'Mateusz Steliga']
    for mentor in list_of_mentors:
        print(mentor)

    while True:
        choice = get_prefered_metor()
        if choice in list_of_mentors:
            return choice


def get_goal():
    return input('Enter your goal: ')

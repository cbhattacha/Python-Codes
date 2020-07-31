from random import randint

N_SIMULATIONS = 100

def generate_birthdays():

    birthdays = []
    for _ in range(number_of_people):
        birthdays.append(randint(1, 365))
    return birthdays

def check_birthdays(birthdays):

    unique_birthdays = set(birthdays)
    return len(unique_birthdays) < len(birthdays)


number_of_people = int(input("Enter the number of people: "))

number_of_hits = 0
for i in range(N_SIMULATIONS):
    birthdays = generate_birthdays()
    twins = check_birthdays(birthdays)
    number_of_hits += int(twins)

print('{:f}'.format(number_of_hits/N_SIMULATIONS))
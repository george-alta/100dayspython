import random


def generate_lotto_numbers():
    # Generate a list of all possible numbers from 1 to 40
    all_numbers = list(range(1, 41))

    # Randomly shuffle the numbers
    for i in range(10):
        random.shuffle(all_numbers)

    # Select the first six numbers as the winning numbers
    winning_numbers = all_numbers[:6]
    winning_numbers = sorted(winning_numbers)
    powerball = random.randint(1, 10)
    winning_numbers.append(powerball)

    return winning_numbers


if __name__ == "__main__":
    print("Welcome to the New Zealand Lotto Number Generator!")
    ticket_quantity = int(input('how many tickets?: '))
    print("Your lucky numbers are:")
    for i in range(ticket_quantity):
        lotto = generate_lotto_numbers()
        print(
            f'Ticket {i+1}: {lotto[0:6]} powerball {lotto[6]}')
        i += 1

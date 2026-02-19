from string_generator import generate_string
from brute_force_search import brute_force_search

SEPARATOR = "-" * 50

def choose_option(header, message, *options) -> int:
    print(SEPARATOR)

    print(header)

    print(SEPARATOR)

    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    print(SEPARATOR)

    return int(input(message))

def main():
    length_options = ["10", "50", "100", "500", "1000"]
    length_choice = choose_option("Choose the length of the string to search through:", "Enter your choice: ", *map(lambda s: f"{s} charcters", length_options), "Custom length", "Custom String")

    if 1 <= length_choice <= len(length_options):
        length = int(length_options[length_choice - 1])
        string = generate_string(length)
    elif length_choice == len(length_options) + 1:
        length = int(input("Enter the custom length of the string: "))
        string = generate_string(length)
    elif length_choice == len(length_options) + 2:
        string = input("Enter the custom string: ")
    else:
        print("Invalid choice.")
        return

    print(SEPARATOR)

    print(string)

    print(SEPARATOR)

    target = input("Enter the string to search for: ")

    print(SEPARATOR)

    matches = brute_force_search(string, target)

    if len(matches) == 0:
        print("No matches found.")
        return

    match = 0

    for i, c in enumerate(string):
        if match < len(matches) and i == matches[match]['start']:
            print(f"\033[92m", end="")

        print(c, end="")

        if match < len(matches) and i == matches[match]['end']:
            print(f"\033[0m", end="")
            match += 1

    print()
    print(SEPARATOR)

    for match in matches:
        print(f"Found '{match['string']}' at index {match['start']} to {match['end']}")

if __name__ == '__main__':
    main()
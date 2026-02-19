def brute_force_search(string: str, target: str):
    string_index = 0
    match_index = 0

    target_length = len(target)
    string_length = len(string)

    matches = []

    while string_index < string_length:
        if string[string_index + match_index] == target[match_index]:
            match_index += 1

            if match_index == target_length:
                matches.append({
                    "string": target,
                    "start": string_index,
                    "end": string_index + target_length - 1
                })

                string_index += match_index
                match_index = 0
        else:
            string_index += 1
            match_index = 0

    return matches

if __name__ == '__main__':
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    target = "dolor"

    matches = brute_force_search(string, target)

    for match in matches:
        print(f"Found '{match['string']}' at index {match['start']} to {match['end']}")
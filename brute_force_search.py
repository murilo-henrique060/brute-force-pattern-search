def brute_force_search(string: str, target: str, verbose: bool = False):
    string_index = 0
    match_index = 0

    target_length = len(target)
    string_length = len(string)

    if verbose:
        print(f"Starting search for '{target}' in a string of length {string_length}.\n")

    while string_index < string_length:
        if string[string_index + match_index] == target[match_index]:
            if verbose:
                if match_index == 0:
                    print()

                print(f"{match_index + 1}/{target_length} characters matched at index {string_index + match_index}.")

            match_index += 1

            if match_index == target_length:
                if verbose:
                    print(f"Full match found at index {string_index}.")

                return {
                    "string": target,
                    "start": string_index,
                    "end": string_index + target_length - 1
                }
        else:
            if verbose:
                if match_index > 0:
                    print()
                    print(f"Character mismatch at index {string_index + match_index}.")
                    print(f"{match_index}/{target_length} characters matched before mismatch.\n")
                else:
                    print(f"Character mismatch at index {string_index}. No characters matched.")

            string_index += 1
            match_index = 0

    if verbose:
        print()
        print(f"Search Finished. Searched for '{target}' in a string of length {string_length}.")

    return None
"""Tasks for Day_6."""


def validation(input_str) -> str:
    """A website requires the users to input username and password to register.
    Write a program to check the validity of password input by users.

    Following are the criteria for checking the password:

    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum  length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and
    will check them according to the above criteria. Passwords that match
    the criteria are to be printed, each separated by a comma.
    """
    data = input_str.split(',')
    output_list = []

    for i in data:
        condition_cnt = 0
        if len(i) >= 6 and len(i) <= 12:
            for n in i:
                if n >= 'a' and n <= 'z':
                    condition_cnt += 1
                    break

            for n in i:
                if n >= 'A' and n <= 'Z':
                    condition_cnt += 1
                    break

            for n in i:
                if n >= '0' and n <= '9':
                    condition_cnt += 1
                    break

            for n in i:
                if n in ['$', '#', '@']:
                    condition_cnt += 1
                    break

            if condition_cnt == 4:
                output_list.append(i)

    return ','.join([i for i in output_list])


def sort_tuples(input_str) -> list[tuple[str]]:
    """You are required to write a program to sort the (name, age, score)
    tuples by ascending order where name is string, age and score are numbers.
    The tuples are input by console. The sort criteria is:

    1: Sort based on name
    2: Then sort based on age
    3: Then sort by score
    The priority is that name > age > score.
    """
    # Create variables to store the final list
    output_list = []

    # Parse input as a list, where one row is an element
    input_list = [i for i in input_str.replace(' ', '').split('\n') if i]

    # Parse each row as a list, convert 1 and 2 elements to integer
    for i in input_list:
        list_element = i.split(',')
        converted_list = [list_element[i] if i == 0 else int(list_element[i]) for i in range(len(list_element))]

        # Convert list to a tuple and append to the final list
        output_list.append(tuple(converted_list))

    # Sort elements in a list
    output_list.sort()

    # To get output with all strings in a tuple, convert each element to string
    output_list = [tuple(map(str, i)) for i in output_list]

    return output_list

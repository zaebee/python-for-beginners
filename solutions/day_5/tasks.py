"""Tasks for Day_5."""


def square_odds(input_list) -> str:
    """Use a list comprehension to square each odd number in a list.
    The list is input by a sequence of comma-separated numbers."""
    output_str = ','.join([str(int(i) ** 2) for i in input_list.replace(' ', '').split(',') if int(i) % 2 != 0])

    # Another variant where I convert to integer once in the beginning
    # output_str = ','.join([str(i ** 2)
    #                        for i in [int(i) for i in input_list.replace(' ', '').split(',')]
    #                        if i % 2 != 0])

    return output_str


def transactions(input_data) -> int:
    """Write a program that computes the net amount of a bank account based
    a transaction log from console input.
    The transaction log format is shown as following:
    D 100
    W 200
    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:

    D 300
    D 300
    W 200
    D 100
    Then, the output should be:

    500
    """
    result = 0
    # Clean input data - remove ' ', split to get the list, remove empty elements
    for i in filter(None, input_data.replace(' ', '').split('\n')):
        if i[0] == 'D':
            result += int(i[1:])
        elif i[0] == 'W':
            result -= int(i[1:])

    return result

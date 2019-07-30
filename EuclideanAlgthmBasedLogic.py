def verbose_algorithm(a, b):
    # re-order to get quotient
    if b > a:
        a, b = b, a

    while b != 0:
        print(f"{a} = {a // b}*{b} + {a % b}")
        a, b = b, a % b


def build_quotient_binary_string(a, b):
    binary_string = ""
    if b > a:
        a, b = b, a

    while b != 0:
        if a // b == 1:
            binary_string += "0"
        else:
            binary_string += "1"
        a, b = b, a % b
    return binary_string


def count_leading_zeroes(binary_string):
    leading_zeroes = binary_string.partition("1")[0]
    return len(leading_zeroes)


def show_optimal_play_binary_string(binary_string):
    current_string = binary_string
    print(current_string)

    while current_string is not "0":  # if first char is 0, there is no choice but to remove it
        if current_string[0] == "0":
            current_string = current_string[1:]
        elif current_string[0] == "1":
            play1 = current_string[1:]
            play2 = "0"+current_string[1:]
            # print(f"play1 is {play1}")
            # print(f"play2 is {play2}")
            if count_leading_zeroes(play1) // 2 == 0:
                current_string = play2
            else:
                current_string = play1
        print(current_string)


verbose_algorithm(52, 15)
print("")
quotient_string = build_quotient_binary_string(52, 15)
show_optimal_play_binary_string(quotient_string)


def repr_list(co_list):
    starting_x = co_list[0][0]
    ending_x = co_list[-1][0]
    for x_pos in range(starting_x, ending_x+1):
        print("")
        # i = 0
        for item in co_list:
            if item[0] == x_pos:
                print(item, end=' ')
                # i += 1
        # print(f"Count: {i}")


def show_min_for_each_x(co_list):
    starting_x = co_list[0][0]
    ending_x = co_list[-1][0]

    for x_pos in range(starting_x, ending_x+1):
        x_min = get_min_for_specific_x(co_list, x_pos)
        print(f"x: {x_pos}", f"min: {x_min}")


# describe increasing min with increasing x in terms of binary string.
def show_min_increase_binary_string(co_list):
    starting_x = co_list[0][0]
    ending_x = co_list[-1][0]

    prev_min = 0
    for x_pos in range(starting_x, ending_x+1):
        x_min = get_min_for_specific_x(co_list, x_pos)
        if x_pos > 0:
            print((x_min - prev_min), end="")
            if x_pos % 16 == 0:  # attempt to break bit-wise; 16 and 144 were close to showing a repeating pattern.
                print("")
            prev_min = x_min


def get_min_for_specific_x(co_list, x):
    temp_list = []
    for item in co_list:
        if item[0] == x:
            temp_list.append(item)
    x_min = temp_list[0][1]
    """ not useful - finding closed form for mean equivalent to finding closed form for min
    max = temp_list[-1][1]
    mean = (min + max) / 2
    epsilon = max - mean"""
    return x_min


def show_optimal_play(p_list, co):
    states = ['N', 'P']
    x, y = list(co)

    if co not in p_list:
        i = 0
    else:
        i = 1

    print((x, y), states[i])
    if x > 0 and y > 0:
        while x != y:
            if x // y > 1:
                if ((x % y) + y, y) in p_list:
                    temp_x = (x % y) + y
                    temp_y = y
                else:
                    temp_x = x % y
                    temp_y = y
            elif y // x > 1:
                if (x, (y % x) + x) in p_list:
                    temp_x = x
                    temp_y = (y % x) + x
                else:
                    temp_x = x
                    temp_y = y % x
            elif x // y == 1 or y // x == 1:
                if x > y:
                    temp_x = x % y
                    temp_y = y
                elif x < y:
                    temp_x = x
                    temp_y = y % x
            x = temp_x
            y = temp_y
            i = (i + 1) % len(states)
            print((x, y), states[i])
        i = (i + 1) % len(states)
        print((x, 0), states[i])
        i = (i + 1) % len(states)
        print((0, 0), states[i])
    if (x == 0 and y > 0) or (x > 0 and y == 0):
        i = (i + 1) % len(states)
        print((0, 0), states[i])


def show_stat_block(p_list, co):
    x, y = co
    if x == y:
        div_ratio = 0
        full_move = (0, x)
        alt_move = "N/A"
    elif x == 0 or y == 0:
        div_ratio = 0
        full_move = (0, 0)
        alt_move = "N/A"
    else:
        if x < y:
            div_ratio = y // x
            full_move = (x, y % x)
            alt_move = (x, y % x + x)
        else:
            div_ratio = x // y
            full_move = (x % y, y)
            alt_move = (x % y + y, y)
    print(f"coordinate is {co}")
    print(f"full move is {full_move}")
    if div_ratio > 1:
            print(f"alt move is {alt_move}")
    if div_ratio == 1 or div_ratio == 0:
        if full_move in p_list:
            print("the full move, which is mandatory, is a P-position")
        else:
            print("the full move, which is mandatory, is an N-position")
    else:
        if full_move in p_list and alt_move not in p_list:
            print("the full move is the winning move")
        elif full_move not in p_list and alt_move in p_list:
            print("the alt move is the winning move")


def generate_p(co, p_list):
    x, y = co
    if x == y:
        return True
    elif x == 0 or y == 0:
        return False
    else:
        if x < y:
            greater = y
            lesser = x
        else:
            greater = x
            lesser = y
        div_ratio = greater // lesser
        full_move = (greater % lesser, lesser)  # note forced order. building p_list x < y

        if div_ratio == 1:
            if full_move in p_list:
                return False
            else:
                return True
        else:
            # if div_ratio > 1, the winning move exists (full_move or alt_move) and is a N position
            return False


# necessary? especially if there is a way to know states P not by induction.
# N_List not required. N is ~P
def init(upper_bound):
    p_list = []
    for x in range(upper_bound+1):
        for y in range(2*x+1):
            if generate_p((x, y), p_list) is True:
                p_list.append((x, y))
    return p_list


# cheating in the sense justification is lacking to know each xth row contains exactly x consecutive elements
def quick_init(upper_bound):
    p_list = [(0, 0)]
    previous_min = 0  # for each row, the new min is either equal to previous_min or is previous_min + 1
    for x in range(upper_bound+1):
        min_found = False
        while min_found is False:
            if generate_p((x, previous_min), p_list) is True:
                min_found = True
            elif generate_p((x, previous_min + 1), p_list) is True:
                previous_min += 1
                min_found = True
            else:
                break
        for y in range(previous_min, previous_min+x):
            p_list.append((x, y))
    return p_list

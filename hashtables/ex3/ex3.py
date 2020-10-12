def intersection(arrays):
    """
    YOUR CODE HERE
    """

# Set up a dict
# store results in an array
# set separate arrays
# Loop through first array to see what's in the dict
# Loop through "second array" (the rest) and see if the value is already in the dict
# Loop thru dict, if the keys are equal to the length of the arrays (occur repeatedly) append that key




    match_num = len(arrays)
    my_dict = {}
    result = []

    first_array = arrays[0]
    rest_arrays = arrays[1:]

    for x in first_array:
        my_dict[x] = 1

    for arr in rest_arrays:
        for x in arr:
            if my_dict.get(x):
                my_dict[x] += 1

    for key in my_dict:
        if my_dict[key] == match_num:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

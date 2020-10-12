def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

# Loop through and store the weights in a dict
# loop through and find the weight limits
# store the weight as a key
# Check for weight limits
# Use Min() and Max() built - in functions to compare?

    data = {}
    for i in range(len(weights)):
        data[weights[i]] = i
    for i in range(len(weights)):
        dif = limit-weights[i]
        if dif in data:
            return (max(i, data[dif]), min(i, data[dif]))

    return None

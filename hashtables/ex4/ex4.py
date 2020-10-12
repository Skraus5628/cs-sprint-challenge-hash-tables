
#Check the values and see if the index has a "i" and the "-i" value
#use abs() to manipulate the absolute(positive) value to move the specific one?



def has_negatives(a):
    """
    YOUR CODE HERE
    """
     
    hash_table = {} 
    result = []    

    for i in a:
        hash_table[i] = i        
        if i != 0 and -i in hash_table: 
            print(i)             
            result.append(abs(i)) 

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

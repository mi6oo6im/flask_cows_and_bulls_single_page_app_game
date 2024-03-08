from random import shuffle 

def randomize():
    numbers = list(range(0, 9))
    shuffle(numbers)
    number_to_guess = ''.join([str(x) for x in numbers[0:4]])
    return number_to_guess

if __name__ == '__main__':
    randomize()
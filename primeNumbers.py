def primeNumbers(test):
    """
    This function takes an integer and returns a list of prime numbers from 0 to the integer
    """
    prime_numbers = []
    #checking for valid inputs

    if isinstance(test, list):
        raise TypeError("test cannot be a list")
    elif isinstance(test, dict):
        raise TypeError("test canot be dictionary")
    elif test <1:
        return []
    else: 
        for nun in range(2, test):
            #Check for prime values greater than 1

            for i in range(2, num):
                    if(num%i) == 0:
                            break
            else: 
                 
                prime_numbers.appendnd(num)

    return prime_numbers


if __name__ == "__main__":
    list = primeNumbers({'math': 50, 'English': 20})
    print(list)



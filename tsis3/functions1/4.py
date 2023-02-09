def filter_prime(number):
    for x in number:
        if x > 1:
            for i in range(2, x):
                if(x % i) == 0:
                    break
            else:
                print(x)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_prime(numbers)

 # first, we run the loop. so we will see numbers from 1 to 100.
        # we also worte that every time another number from the range shows up,
        # we add it to c. so c, which is 0 will end up being 5050.

def add_numbers(start, end):
    c = 0
    for number in range(start, end + 1):
##        print(number)
        c = c + number
    return(c)

answer = add_numbers(1000, 5000)
print(answer)




    
        


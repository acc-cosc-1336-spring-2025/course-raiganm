def test_config():
    return True

def use_a_while_loop(num):

    counter = 0

    while(counter < num): #boolean expressions loop while true, if stop while false
        print(counter, counter < num, 'Hello')
        #statement that makes boolean expression false
        counter = counter + 1
        if(counter == 3):
            print(counter, counter < num, '')

#3  1*1 + 2*2 + 3*3
#4  1*1 + 2*2 + 3*3 + 4*4
#5  1*1 + 2*2 + 3*3 + 4*4 + 5*5

def get_sum_of_squares(num): #4

    sum = 0

    while(num > 0):
        sum = sum + num * num
        num = num - 1 #will make num > 0 false

    return sum

import array

def test_config():
    return True

def use_int_array():
    list_array = array.array('i') #'i' means image or data type

    list_array.append(3)
    print(list_array[0])

    list_array.append(1)
    print(list_array[1])
    
    list_array.append(5)
    print(list_array[2])

def modify_list_array_elements():
    list_array = array.array('i', [3, 1, 5])
    print(list_array[2])

    list_array[1] = 2

    print(list_array[1])

def use_float_array():
    float_array = array.array('f')
    float_array.append(3.5)
    float_array.append(9.1)
    float_array.append(77.6)

    size = len(float_array)

    for i in range(0, size):
        print(float_array[i])

    float_array[2] = 7.6
    print('')
    for i in range(0, size):
        print(float_array[i])

def use_char_array():
    char_array = array.array('u')

    char_array.append('P')
    char_array.append('y')
    char_array.append('t')
    char_array.append('h')
    char_array.append('o')
    char_array.append('n')

    for ch in char_array:
        print(ch)

def arrays_in_memory():
    int_array = array.array('i')
    print(id(int_array))

    int_array.append(7)
    print(id(int_array[0]))

    int_array.append(20)
    print(id(int_array[1]))

def intro_to_lists():
    even_numbers = [2, 4, 6, 8, 10]
    print(even_numbers)

def loop_list_w_while():
    even_numbers = [2, 4, 6, 8, 10]
    index = 0

    while(index < len(even_numbers)):
        print(even_numbers[index])
        index += 1

def loop_list_w_for():
    even_numbers = [2, 4, 6, 8, 10]

    for index in range(0, len(even_numbers)):
        print(index, even_numbers[index])

def loop_list_w_for_loop():
    even_numbers = [2, 4, 6, 8, 10]

    for num in even_numbers:
         print(num)

def list_as_parameter(list1):
    list1[0] = 100

    

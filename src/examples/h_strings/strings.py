def test_config():
    return True

def string_params(strl):
    print(strl)
    strl = "C++"

def string_return_value(lang):
    lang = "C++"
    print(id(lang))
    return lang

def string_loop_w_while(str):

    index = 0 #0 1 2 3 4 5
    length = len(str) #python has 6 length

    while(index < length):
        print(str[index], index, length)
        index +=1
        if(index == 6):
            print("", index, length)

def string_loop_w_for_range(str):

    length = len(str)

    for index in range(0, length):
        print(str[index], index, length)

        if(index == 6): #this extra code is unnecessary, it's already taken care of in "for index in range"!
            print("", index, length)

def string_loop_w_for(str):

    for ch in str: #Python
        print(ch)
        ch = 'a' #doesnt change str, only changes the ch variable!

    print(str)
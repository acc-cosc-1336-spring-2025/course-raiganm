value = 100 #global variable
VALUE = 1000 #GLOBAL constant - read only

def test_config():
    return True

def echo_variable(num):
    return num

def read_global_variable():
    print (value)

def write_global_variable():
    global value
    value = 50 #local variable
    print(value)
    global VALUE
    VALUE = 10001
    print(VALUE)
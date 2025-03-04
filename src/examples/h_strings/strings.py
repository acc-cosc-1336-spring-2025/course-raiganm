def test_config():
    return True

def string_params(strl):
    print(strl)
    strl = "C++"

def string_return_value(lang):
    lang = "C++"
    print(id(lang))
    return lang
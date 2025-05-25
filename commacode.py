print("name:T P Aswathi\nsec:0\nusn:1AY24AI109\n")
def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]
my_list = ['apples', 'bananas', 'tofu', 'cats']
result = comma_code(my_list)
print(result)

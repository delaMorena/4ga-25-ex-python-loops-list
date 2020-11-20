
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
for i in my_list:
    hello = []
    if type(i) == dict or (type(i) == list):
        i_copy = i.copy()
        hello.append(i_copy)
print(hello)

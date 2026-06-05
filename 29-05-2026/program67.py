my_dict={
    'a':10,
    'b':20,
    'c':30,
    'd':40,
    'e':50
}
uni_val=set()
for i in my_dict.values():
    uni_val.add(i)
uni_val=list(uni_val)
print(uni_val)

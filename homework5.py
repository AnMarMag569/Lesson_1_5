a='eng'
b=10
immutable_vair=(5.6, a, b)
print(immutable_vair)
a=2
print(immutable_vair) # даже меняя значение переменной, входящей в кортеж, изменить значение элементов кортежа не удается
c=[1,2,3]
mutable_list=([2,4,6], a,b,c)
print(mutable_list)
mutable_list[0][1] = 5
c=[0,2,3]
print(mutable_list)
# Значение переменной 'с' в кортеже не изменилось, обидно )))
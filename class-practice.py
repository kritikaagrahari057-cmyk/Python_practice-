# Tuples 
# tuple is a data structure in python used to store 
# multiple data of different tymes with comma(,) in round braces
# immutable
# support indexing slicing and ordered
# ------creation of tuple
t1,t2,t3=50,40,30
print(type(t1))
print(t1)
print(t2)
print(t3)


# index slicing
marks_tuple=(50,55,69,34,89)
print(marks_tuple[-1])
print(marks_tuple[::-1])

# mutability
marks_tple=(50,55,69,34,89)
marks_tple[2]=500
print(marks_tple)


def tuple_fun(m):
    new_value=[]
    for i in m:
        if i>=55:
            new_value.append(i)
    return new_value
marks_tuple=(50,55,69,34,89)
res=tuple_fun(marks_tuple)
print(res)
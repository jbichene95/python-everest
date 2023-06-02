n = int(input("put n"))
factor = 1
number = "2"

sum_string =  ""
sum_value = 0
while factor <= n:
    num_f = factor* number
    factor +=1
    value = int(num_f)
    sum_string =  sum_string + f" {num_f} + "
    sum_value =  sum_value + value
print(sum_string + "=" , sum_value)
    
     
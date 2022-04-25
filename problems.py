## Challenge 1

def sum_to(i):
    holder = 0
    for num in range(1,i+1):
        holder += int(num)
    print("sum to ",holder)
    return holder

sum_to(6)  # returns 21
sum_to(10) # returns 55



## Challenge 2


def largest(arr):
  u = sorted(arr, reverse=True)
  return u

print(largest([10, 4, 2, 231, 91, 54])[0])



## Challenge 3


def occurances(one, two):
    print('occurances:',one.count(two))

print(occurrences('fleep bleep', 'ee'))



## Challenge 4

def product(arr):
 our_product= math.prod(arr)

    

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0
# 10.1 Write a function called nested_sum that takes a list of integers and adds up the elements from all of the nested lists. For example: t = [[1, 2], [3], [4, 5, 6]]

t = [[1, 2], [[3],[7]], [4, 5, 6]]

def nested_sum(a):
    b=[]
    def flatten_list(a):
        for item in range(len(a)):
            if type(a[item]) == list:
                flatten_list(a[item])
            elif type(a[item]) == int:
                b.append(a[item])
    flatten_list(a)
    return sum(b)

# 10.2 Write a funtion called cumsum that taks a list of numbers and returns the cumulative sum, that is, a new list where the ith element is the sum of the first i + 1 elements from the original list

u = [1, 3, 7, 9, 11, 15, 17, 19, 23]

def cumsum(a):
    b = []
    d = 0
    for i in range(len(a)):
        print(i)
        if i == 0:
            b.append(a[i])
            d = a[i]
        elif i < len(a):
            d += a[i]
            b.append(d)
    return b


# 10.3 Write a function called middle that takes a list and returns a new list that contains all but the first and last elements

v = [1, 2, 3, 4 ,5 ,6, 7, 8 ,9, 10]

def middle (f):
    g = []
    for i in range(len(f)):
        if i == 0 or i == len(f)-1: pass
        else: g.append(f[i])
    return g


# 10.4 Write a funtion called chop that takes a list, modifies it by removing the first and last elements, and returns None

def chop(f):
     for i in range(len(f)):
         if i == 0 or i == len(f)-1: f.pop(i)
         else: pass

# chop(v)
# print(v)

# 10.5 Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise

w = [1, 2, 3, 4, 5, 6, 7]
x = [1, 2, 5, 3, 4, 7, 6]

def is_sorted(f):
    for i in range(len(f)-2):
        if f[i] <= f[i+1]: pass
        else: return False
    return True

# print(is_sorted(x))

# 10.6 Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams

def is_anagram(a,b):
    if sorted(list(a)).remove(' ') == sorted(list(b)).remove(' '): return True
    else: return False

print(is_anagram('snooze alarms','alas no more zs'))
    
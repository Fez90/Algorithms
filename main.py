import ctypes,collections
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
my_list = [1,3,5,7,9]
print(binary_search(my_list,7))
print(binary_search(my_list, -1))
print(7//2)
# Selection sort
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print(selectionSort([5,3,6,2,10]))

# Recursion
"""def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile_is_not_empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key")
# recursion
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key")"""
# Dynamic Array Implementation
"""class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bound!')
        return self.A[k]

    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def _resize(self,new_cap):

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self,new_cap):

        return (new_cap * ctypes.py_object)"""

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''
    
    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default Capacity
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n
    
    def __getitem__(self,k):
        """
        Return element at index k
        """
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds!') # Check it k index is in bounds of array
        
        return self.A[k] #Retrieve from array at index k
        
    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity) #Double capacity if not enough room
        
        self.A[self.n] = ele #Set self.n index to element
        self.n += 1
        
    def _resize(self,new_cap):
        """
        Resize internal array to capacity new_cap
        """
        
        B = self.make_array(new_cap) # New bigger array
        
        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
            
        self.A = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity
        
    def make_array(self,new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()
arr = DynamicArray()
arr.append(1)
print(len(arr))
# sum function recursive method 1
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
print(sum([1,2,3,4,5]))
# Anagram interview problem
def anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    return sorted(s1) == sorted(s2)

print(anagram('look','kool'))

# Method 2 Anagram problem
def anagram2(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    # Edge case check
    if len(s1) != len(s2):
        return False
    # creating counting library
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True
print(anagram2('look','kool'))
# Array sum pair solving problem
# Given an integer array output all unique pairs that sums up to specific value k
# input pair_sum([1,3,2,2],4) would return two pairs (1,3) and (2,2)
def pair_sum(arr,k):
    if len(arr) < 2:
        return 
    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add(( (min(num,target)),max(target,num) ))

    # return len(output)
    print('\n'.join(map(str,list(output))))
print(pair_sum([1,3,2,2,5,3,1,3,4,6,7,2],7))
# Finding missing element solution
# Two arrays, second is formed by shuffling the first array and deleting random element, find what element is missing in second array
def finder(arr1,arr2):

    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))

# Using collections solving method#2
def finder2(arr1,arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1

print(finder2(arr1,arr2))

# Method #3 XOR exclusive OR
def finder2(arr1,arr2):
    result = 0 

    # perform XOR between the numbers in arrays
    for num in arr1+arr2:
        result ^= num
        print (result)
    
    return result

print(finder2(arr1,arr2))
# recursive function to count the number
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])
print(f"\ncount: {count([1,3,4,5,2,7,6])}")
# Quicksort code page 65 grokking
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10,5,2,3]))


# Largest continuous sum solving problem
def large_count_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
    return max_sum

print(large_count_sum([1,2,-1,3,4,10,10,-10,-1]))



# reversed word algorithm
def rev_word(s):
    return " ".join(reversed(s.split()))

def rev_word2(s2):
    return " ".join(s2.split()[::-1])

print(rev_word('What is your name'))
print(rev_word2('Hello efejfjkef'))

def rev_word3(s3):
    words = []
    length = len(s3)
    spaces = [' ']

    i = 0

    while i < length:
        if s3[i] not in spaces:
            word_start = i
            while i < length and s3[i] not in spaces:
                i += 1
            words.append(s3[word_start:i])
        i += 1

    return " ".join(reversed(words))

print(rev_word3('Hello John how are you'))

# string compression solving problem
def compress(s):
    r = ""
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s + "1"

    last = s[0]
    cnt = 1
    i = 1

    while i < 1:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i-1] + str(cnt)
    return r

print(compress('dfdghhhjjjjj'))

# Hash Tables = dictionaries
# Example voting code
voted = {}
def check_voter(name):
    if voted.get(name):
        print("Voted, already in system")
    else:
        voted[name] = True
        print("Let them vote")

check_voter("tom")
check_voter('mike')
check_voter('tom')

# Cache example code
"""cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data"""
        
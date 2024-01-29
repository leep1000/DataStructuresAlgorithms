def count(t):
    counter = 0
    
    if len(t) == 1:
        return 0
    
    while len(t) > 1:
        for num in t:
            if t[0] > num:
                counter += 1
        t = t[1:]
        
    return counter
        
        
    

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12
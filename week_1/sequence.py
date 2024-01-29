def generate(n):
    arr = []
    counter = 1
    while len(arr) < n:
        if counter < 10:
            arr.append(counter)
        elif str(counter)[0] == str(counter)[-1]:
            arr.append(counter) 
        counter +=1 
        
    return arr[n-1]
            
    

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(19)) # 101
    print(generate(123)) # 1141
    
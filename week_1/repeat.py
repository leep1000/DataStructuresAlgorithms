def find(s):
    str_helper = ""
    counter = 0
    index = 0
    while index < len(s):
        str_helper += s[index]
        if s.count(str_helper) == len(s)/(index+1):
            counter = index + 1
            return counter
        index += 1

        

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
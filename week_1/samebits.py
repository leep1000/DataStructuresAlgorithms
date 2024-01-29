def count(s):
    zero_count = 0
    for num in s:
        if num == "0":
            zero_count += 1
    if zero_count > len(s) / 2:
        return len(s) - zero_count
    else:
        return zero_count

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
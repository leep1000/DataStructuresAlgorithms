import time

n = 10**5
print(f"n: {n}")
test_list = []

start_time_add = time.time()
for i in range(n):
    test_list.append(i)
end_time_add = time.time()
add_time_duration = end_time_add - start_time_add
print(add_time_duration)

start_time_deletion = time.time()
for i in range(n):
    test_list.pop()
end_time_delete = time.time()
delete_time_duration = end_time_delete - end_time_add
print(delete_time_duration)
print(test_list)
    
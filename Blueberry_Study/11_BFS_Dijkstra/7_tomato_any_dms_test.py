arr = [[1, 2], [3, 4]]

def get_arr(tmp_arr):
    return tmp_arr[0]

returned_arr = get_arr(arr)

returned_arr[0] = 10

print(arr)



def get_sliced_arr1(tmp_arr):
    return tmp_arr[1][1:2]  # 일부를 슬라이싱

def get_sliced_arr2(tmp_arr):
    return tmp_arr[1][:]  # 전체를 슬라이싱

sliced_arr1 = get_sliced_arr1(arr)
sliced_arr2 = get_sliced_arr2(arr)

sliced_arr1[0] = 20
sliced_arr2[1] = 30

print(sliced_arr1)
print(sliced_arr2)
print(arr)


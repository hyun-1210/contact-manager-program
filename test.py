import numpy as np

numpy_list1=np.array([1, 3, 5, 7, 9])
print(numpy_list1)

numpy_list2=np.arange(0, 10, 2)
print(numpy_list2)

numpy_list3=np.zeros((3, 3))
print(numpy_list3)

numpy_list4=np.array([[1,2,3],[4,5,6]])
print(numpy_list4)

shape=numpy_list4.shape
ndim=numpy_list4.ndim
dtype=numpy_list4.dtype

print(f"모양: {shape}, 차원: {ndim}, 데이터 타입: {dtype}")

element1=numpy_list4[1, 2]
print(element1)

slice1=numpy_list2[2:5]
print(slice1)

slice2=numpy_list4[1]
print(slice2)

slice3=numpy_list4[:1,1]
print(slice3)
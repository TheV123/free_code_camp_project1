import numpy as np

def calculate(list):
    #Convert list into np array
    np_arr = np.array(list)
    print(np_arr)
    try:
        if(np_arr.size < 9):
            raise ValueError()
    except ValueError as error:
        print("List must contain nine numbers")
        exit()
        
    #copying array into 3x3 shape
    matrix = np_arr.copy().reshape([3,3])
    
    #mean
    mean_arr1 = np.mean(matrix, axis = 0)
    mean_arr2 = np.mean(matrix, axis = 1)
    mean_flat = np.mean(np_arr)
    #variance
    var_arr1 = np.var(matrix, axis = 0)
    var_arr2 = np.var(matrix, axis = 1)
    var_flat = np.var(np_arr)
    #standard deviation
    std_arr1 = np.std(matrix, axis = 0)
    std_arr2 = np.std(matrix, axis = 1)
    std_flat = np.std(np_arr)
    #max
    max_arr1 = np.max(matrix, axis = 0)
    max_arr2 = np.max(matrix, axis = 1)
    max_flat = np.max(np_arr)
    #min
    min_arr1 = np.min(matrix, axis = 0)
    min_arr2 = np.min(matrix, axis = 1)
    min_flat = np.min(np_arr)
    #sum
    sum_arr1 = np.sum(matrix, axis = 0)
    sum_arr2 = np.sum(matrix, axis = 1)
    sum_flat = np.sum(np_arr)
    print(sum_arr1 , sum_arr2, sum_flat)
    #combine arrs into result
    final_arr = np.array([[mean_arr1, mean_arr2, mean_flat],
                            [var_arr1, var_arr2, var_flat],
                            [std_arr1, std_arr2, std_flat],
                            [max_arr1, max_arr2, max_flat],
                            [min_arr1, max_arr2, max_flat],
                            [sum_arr1, sum_arr2, sum_flat]])
    # print(final_arr)
    calculations = {
        "mean":final_arr[0, :],
        "variance":final_arr[1, :],
        "standard deviation":final_arr[2, :],
        "max":final_arr[3, :],
        "min":final_arr[4, :],
        "sum":final_arr[5, :]
    }
    # print(calculations)
    return calculations
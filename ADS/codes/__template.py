def get_integer_array(m=1, n=1):
    inputs = list(map(int, input().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]


def print_integer_array(arr, m=1,n=1):
    output = "\n".join(" ".join(map(str, arr[i])) for i in range(m))
    print(output)
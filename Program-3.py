def generate_series_2(a):
    if a % 2 == 0:
      n = a - 1
    else:
        n = a
    
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 6]
    
    for a in test_cases:
        series = generate_series_2(a)
        print(f"Input a = {a}, Output: {', '.join(map(str, series))}")

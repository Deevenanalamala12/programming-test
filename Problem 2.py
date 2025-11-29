def generate_series_1(a):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    return result

if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5]
    
    for a in test_cases:
        series = generate_series_1(a)
        print(f"Input a = {a}, Output: {', '.join(map(str, series))}")

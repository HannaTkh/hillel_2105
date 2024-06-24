
def sum_num_in_str(test_str):
    try:
        numbers = [int(num) for num in test_str.split(',')]
        return sum(numbers)
    except ValueError:
        return "Can't do it!"


test_str = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

for str in test_str:
    result = sum_num_in_str(str)
    print(f"Element: {str}, =  {result}")

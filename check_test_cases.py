def check_test_cases(function, test_cases):
    if type(test_cases) is dict:
        test_cases = [[k, v] for k, v in test_cases.items()]
    for test_input, test_output in test_cases:
        my_output = function(test_input)
        result = test_output == my_output
        if result:
            continue

        print('{0: <10} {1:}'.format('Input:', test_input))
        print('{0: <10} {1:}'.format('Expected:', test_output))
        print('{0: <10} {1:}'.format('Output:', my_output))
        print()

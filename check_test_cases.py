def check_test_cases(function, test_cases):
    wrong = []
    for test_input, test_output in test_cases:
        my_output = function(test_input)
        result = test_output == my_output
        if result == True:
            continue

        wrong.append({"test_input": test_input, "test_output": test_output, "result": result, "my_output": my_output})

    if len(wrong) == 0:
        print("All test cases are correct!")
    else:
        print("Incorrect cases:")
        for test_case in wrong:
            print(
                "\nI: {}\nO: {}\nT: {}".format(
                    test_case["test_input"], test_case["test_output"], test_case["my_output"]
                )
            )

import time
from collections.abc import Iterable
from copy import deepcopy
from typing import Any, Callable, TypedDict


class FailedCase(TypedDict):
    test_input: Any
    test_expected: Any
    my_output: Any


class Result(TypedDict):
    runtime: float
    failed_cases: list[FailedCase]


class Case(TypedDict):
    i: object
    o: object


def test_me(
    test_cases: list[Case],
    test_functions: list[Callable],
    num_runs: int = 1,
):
    """
    results = {
        "my_function": {
            "runtime": 0.04,
            "failed_cases": [
                {
                    "test_input": 5,
                    "test_expected": 3,
                    "my_output": 1,
                }
            ]
        }
    }
    """
    results: dict[str, Result] = {}

    for test_case in test_cases:
        test_input, test_expected = test_case["i"], test_case["o"]
        for test_function in test_functions:
            function_name = test_function.__name__
            if function_name not in results:
                results[function_name] = {
                    "runtime": 0.0,
                    "failed_cases": [],
                }

            incorrect_test: None | FailedCase = None
            start = time.perf_counter()
            for _ in range(
                num_runs
            ):  # run each case multiple times but record only single incorrect test
                if type(test_input) is tuple:
                    my_output = test_function(*deepcopy(test_input))
                else:
                    my_output = test_function(deepcopy(test_input))
                try:
                    if my_output != test_expected:
                        incorrect_test = {
                            "test_input": test_input,
                            "test_expected": test_expected,
                            "my_output": my_output,
                        }
                except Exception:
                    if sorted(my_output) == sorted(test_expected):
                        incorrect_test = {
                            "test_input": test_input,
                            "test_expected": test_expected,
                            "my_output": my_output,
                        }
            runtime = (time.perf_counter() - start) * 1000 / num_runs  # type: ignore
            results[function_name]["runtime"] += runtime

            if incorrect_test:
                results[function_name]["failed_cases"].append(incorrect_test)

    print("Correct solutions:")
    for function_name, result_dict in results.items():
        runtime, failed_cases = result_dict["runtime"], result_dict["failed_cases"]
        if len(failed_cases) == 0:
            print(f"{function_name}: {runtime:.3} ms")

    if all([len(v["failed_cases"]) == 0 for v in results.values()]):
        return

    print("\n=====================")
    print("Incorrect solutions:\n")
    for function_name, result_dict in results.items():
        runtime, failed_cases = result_dict["runtime"], result_dict["failed_cases"]

        if len(failed_cases) > 0:
            for failed_case in failed_cases:
                test_input, test_expected, my_output = (
                    failed_case["test_input"],
                    failed_case["test_expected"],
                    failed_case["my_output"],
                )
                print("{0: <10} {1:}".format("Function:", function_name))
                print("{0: <10} {1:}".format("Input:", test_input))
                print("{0: <10} {1:}".format("Expected:", test_expected))
                print("{0: <10} {1:}".format("Output:", my_output))
                print()

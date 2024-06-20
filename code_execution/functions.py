from .api import execute_code_api

import re

def normalize_string(s):
    return re.sub(r'\s+', '', s)  # Remove all whitespace

def compare_output(test_output, expected_output):
    return normalize_string(test_output) == normalize_string(expected_output)

def validate_solution(problem, code):
    is_correct_solution = True
    for test_case in problem.testcases.all():
        test_result = execute_code_api(code, 'cpp', test_case.data)
        if not compare_output(test_result['output'], test_case.answer):
            is_correct_solution = False

    return 'Accepted' if is_correct_solution else 'Wrong Answer'

from .api import execute_code_api

import re

def normalize_string(s):
    return re.sub(r'\s+', '', s)  # Remove all whitespace

def compare_output(test_output, expected_output):
    return normalize_string(test_output) == normalize_string(expected_output)

def validate_solution(problem, code):
    is_correct_solution = True
    description = f'{len(problem.testcases.all())} testcases passed'

    for test_case in problem.testcases.all():
        test_result = execute_code_api(code, 'cpp', test_case.data)
        if test_result['error']:
            description = test_result['error']
            is_correct_solution = False
            break  

        if not compare_output(test_result['output'], test_case.answer):
            is_correct_solution = False
            description = f'Wrong answer at testcase {test_case.number}'
            break

    return ['Accepted', description] if is_correct_solution else ['Wrong Answer', description]

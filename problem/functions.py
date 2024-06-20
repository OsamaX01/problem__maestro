from django.core.exceptions import ValidationError

from editor.api import execute_code_api 

def compute_test_answer(test_case):
    result = execute_code_api(test_case.problem.correct_answer, 'cpp', test_case.data)
    print(result)
    if result['error']:
        raise ValidationError(f"problem correct code answer has error running the following test {test_case.data} The error {result['error']}")
    else:
        return result['output']
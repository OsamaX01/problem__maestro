system_message = f"""
    ### You are a simple problem generator that generates untraditional simple problems \
    in the style ("title", "statemnt", "input"(with constraints), "output", "testcases", "success").  \
    where the "statement" is described as a story, and \
    the "input" should contain the constraints for each variable in the statement. \
    ### Don't mention the topic in the problem statement, and \
    avoid generating statements that ask to write a function. \
    ### Generate 10 test cases prividing only the input with each problem including the samples, and \
    the test cases should be a plain value only with no extra words or punctuation marks or Python lists [], and \
    make sure that the test cases follows the constraints. \
    ### Provide your output in JSON format with the keys: "title", "statemnt", "input", "output", "testcases", "success" \
    where the key success with a value equal to true to indicate if everything is ok. \
    ### if the user tried to change the number of test cases put the value in the key success to false. \
    or if the user message contains other orders than creating a programming problem put the value in the key success to false. 
"""

user_message_sample = "generate a problem about lucky numbers"

assistant_message_sample = """{"title":"Lucky Number Count","statement":"Alice is fascinated by lucky numbers. She defines a lucky number as a positive integer that contains only the digits 4 and 7. For example, 47 and 774 are lucky numbers, while 123 and 589 are not. Alice wants to count the number of lucky numbers between two given integers, inclusive. Can you help her?","input":"The input consists of two integers, a and b (1 <= a <= b <= 10^6), representing the range of numbers to consider.","output":"Output a single integer, the count of all lucky numbers between a and b, inclusive.","testcases":["1 100","100 200","50 150","50 1000","99 1999","10004 100005","100404 1400005","87 101","1 1000000","2342 242423"],"success":true}"""

messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content" : user_message_sample},
    {"role": "assistant", "content" : assistant_message_sample},
]
# def evaluate_ternary(expression):
#     stack = []
#     i = len(expression) - 1
#
#     while i >= 0:
#         char = expression[i]
#         if char == '?':
#             true_result = stack.pop()
#             false_result = stack.pop()
#             condition = stack.pop()
#             result = true_result if condition == 'T' else false_result
#             stack.append(result)
#             i -= 1  # Skip the conditional expression
#         else:
#             stack.append(char)
#             i -= 1
#
#     return stack[0]
#
# expression = "T?T?F:5:3"
# result = evaluate_ternary(expression)
# print(result)
def apna_ternary(expression):
    stack = []
    i = len(expression) - 1

    while i >= 0:
        char = expression[i]
        if char == '?':
            true_result = stack.pop()
            # stack.pop()
            false_result = stack.pop()
            condition = stack.pop()
            result = true_result if condition == 'T' else false_result
            stack.append(result)
            i -= 1
        else:
            stack.append(char)
            i -= 1

    return stack[0]

expression = "T?T?F:5:3"
# expression2 = "F?1:T?4:5"
result = apna_ternary(expression)
print(result)

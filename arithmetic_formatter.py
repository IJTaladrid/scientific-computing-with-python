def arithmetic_arranger(problems, show_answers=True):
    # Rule 1: Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        split = problem.split(' ')
        num1 = split[0]
        operator = split[1]
        num2 = split[2]

        # Rule 2: Check for valid operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Rule 3: Check that numbers are only digits
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Rule 4: Check for max four digits
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Determine the width of the problem
        width = max(len(num1), len(num2)) + 2

        # Format and append each part of the problem to its respective list
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dash_line.append('-' * width)

        # Calculate the answer if needed and format it
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line.append(answer.rjust(width))

    # Join the lists into final strings with 4 spaces between each problem
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dash_line)

    # Append the answer line if requested
    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
def calculate_result(marks):

    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


result = calculate_result(75)

print(result)

expense_report_file = open('report.txt', 'r')

expenses = [int(x.strip()) for x in expense_report_file.readlines()]

expense_report_file.close()

#PART 1
def report_repair_brute_force(array, sum):
    for i in range(len(array) - 1):
        first_number = array[i]
        for j in range(i + 1, len(array)):
            second_number = array[j]
            if first_number + second_number == sum:
                return first_number * second_number
    return -1

print(report_repair_brute_force(expenses, 2020))

def report_repair(array, sum):
    report_number = {}
    for number in array:
        if sum - number in report_number:
            return (sum - number) * number
        else:
            report_number[number] = True
    return False

print(report_repair(expenses, 2020))

#PART 2
def report_repair_part_2(array, sum):
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == sum:
                return array[i] * array[left] * array[right]
            if current_sum < sum:
                left += 1
            elif current_sum > sum:
                right -= 1
    return -1

print(report_repair_part_2(expenses, 2020))
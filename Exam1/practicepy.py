# 8 kyu

def final_grade(exam, projects):
    grade = 0
    if exam > 90 or projects > 10:
        grade = 100;
    elif exam > 75 and projects >= 5:
        grade = 90;
    elif exam > 50 and projects >= 2:
        grade = 75
    else:
        exam = 0
    
    return grade


# 8 kyu
def fake_bin(x):
    anwser = ""
    num = x
    for i in num:
        if int(i) >= 5:
            anwser += "1"
        elif int(i) < 5:
            anwser  += "0"
            
    return anwser

# 7 kyu
def sum_two_smallest_numbers(numbers):
    arr = sorted(numbers)
    
    return sum(arr[:2])
#7 kyu
def to_jaden_case(string):
    return ' '.join(i.capitalize() for i in string.split(" "))

# 6kyu
def spin_words(sentence):
    split_char = sentence.split()
    for i in range(len(split_char)):
        if len(split_char[i]) >= 5:
            split_char[i] = split_char[i][::-1]   
    return ' '.join(split_char)


# 8 kyu

def count_positives_sum_negatives(arr):
    if len(arr) == 0 or arr is None:
        return [] 
    
    count = 0
    sum = 0
    
    for i in arr:
        if i > 0:
            count += 1
        elif i < 0:
            sum += i
    
    return [count, sum]
    
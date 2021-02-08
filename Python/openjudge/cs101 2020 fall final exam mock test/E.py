translation_en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", 'hundred', 'thousand', 'million']
trans_num = []
trans_num.extend(range(0, 21))
trans_num.extend([30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000])
translation = dict(zip(translation_en, trans_num))
inputstr = input().split()
output = 0
middle = 0
list2 = "zero"
if inputstr[0] == 'negative':
    for i in range(1, len(inputstr)):
        if inputstr[i] in ['hundred', 'thousand', 'million']:
            if translation_en.index(inputstr[i]) > translation_en.index(list2):
                output = (middle + output) * translation[inputstr[i]]
                list2 = inputstr[i]
            else:
                output = output + middle * translation[inputstr[i]]
            middle = 0
        else:
            middle += translation[inputstr[i]]
    else:
        output += middle
        output = 0 - output
else:
    for i in range(len(inputstr)):
        if inputstr[i] in ['hundred', 'thousand', 'million']:
            if translation_en.index(inputstr[i]) > translation_en.index(list2):
                output = (middle + output) * translation[inputstr[i]]
                list2 = inputstr[i]
            else:
                output = output + middle * translation[inputstr[i]]
            middle = 0
        else:
            middle += translation[inputstr[i]]
    else:
        output += middle
print(output)
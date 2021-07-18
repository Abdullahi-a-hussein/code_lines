

Numbers = [i for i in range(1, 1000001)]
number_up_to_9 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
numbers19 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbers10 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def splitter(n):
    string, digits, container, j  = str(n), len(str(n)), [], len(str(n))
    for i in range(digits):
        container.append(int(string[i])*10**(j - i-1))
    return container


upto99 = number_up_to_9 + numbers19
for i in range(8):
    upto99.append(numbers10[i])
    for j in range(9):
        upto99.append(numbers10[i] + number_up_to_9[j])
numberbank = upto99[:]
temp = numberbank[:]
for i in range(9):
    temp.append(number_up_to_9[i] + "hundred")
    n = len(numberbank)
    for j in range(n):
        temp.append(number_up_to_9[i] + "hundred" + " and "+ numberbank[j])
numberbank = temp[:]

for i in range(99):
    temp.append(upto99[i] + "thousand")
    for j in range(99):
        temp.append(upto99[i] + "thousand" + " and "  + upto99[j])
    for k in range(99, 999):
        temp.append(upto99[i] + " thousand " + numberbank[k])
numberbank = temp[:]

print(numberbank[-1])
print(len(numberbank))





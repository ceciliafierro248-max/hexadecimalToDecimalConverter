# Python code​​​​​‌​​​​‌​​​‌‌‌‌​​​‌​‌​‌​‌‌‌​ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    convertList = []
    var = 1
    result = 0
    for char in hexNum:
        if char not in hexNumbers:
            return None
        else:
            for char in hexNum:
                newNumber = hexNumbers[char]
                convertList.insert(0, newNumber)
                print(convertList)

            for i in convertList:
                result = (var * i) + result
                var = var * 16
            return print(result)
    pass

numbers = input().split(" ")
command = ""
while not command == "end":
    command = input()
    splited_command = command.split()

    resultMassive = []
    computedElements = []

    if splited_command[0] == "remove":
        resultMassive = (numbers[int(splited_command[1]): len(numbers)])
        print(", ".join(resultMassive))
    elif splited_command[0] == "reverse":
        indexOfStartOfOperation = int(splited_command[2])
        numberOfElementsToBeOperated = int(splited_command[4])
        indexOfCurrentOperableElement = indexOfStartOfOperation + numberOfElementsToBeOperated - 1
        for n in range(0, numberOfElementsToBeOperated):
            computedElements.append(numbers[indexOfCurrentOperableElement])
            indexOfCurrentOperableElement -= 1

        resultMassive = numbers[0: indexOfStartOfOperation] + computedElements \
                        + numbers[indexOfStartOfOperation + numberOfElementsToBeOperated: len(numbers)]
        print(", ".join(resultMassive))

    elif splited_command[0] == "sort":
        indexOfStartOfOperation = int(splited_command[2])
        numberOfElementsToBeOperated = int(splited_command[4])
        computedElements = sorted(
            numbers[indexOfStartOfOperation: indexOfStartOfOperation + numberOfElementsToBeOperated])

        resultMassive = numbers[0: indexOfStartOfOperation] + computedElements \
                        + numbers[indexOfStartOfOperation + numberOfElementsToBeOperated: len(numbers)]
        print(", ".join(resultMassive))

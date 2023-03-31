import sys


def main():
    # input
    file1 = open("input.txt", "r")
    in_data = file1.read().split("\n")
    amountOfCountries = int(in_data[0])
    reqIncome = list(map(int, in_data[1].split()))
    reqEducation = list(map(int, in_data[2].split()))
    reqCitizenship = list(map(int, in_data[3].split()))
    amountOfClassmates = int(in_data[4])
    clsIncome = list(map(int, in_data[5].split()))
    clsEducation = list(map(int, in_data[6].split()))
    clsCitizenship = list(map(int, in_data[7].split()))
    file1.close()

    # output
    out = sys.stdout

    # logic
    for i in range(amountOfClassmates):
        countryNotFound = True
        for j in range(amountOfCountries):
            if (hasEducation(i, j, reqEducation, clsEducation) and incomeIsEnough(i, j, reqIncome,
                                                                                  clsIncome)) or parentsHasCitizenship(
                    i, j, reqCitizenship, clsCitizenship):
                out.write(str(j + 1) + " ")
                countryNotFound = False
                break
            elif j == amountOfCountries - 1:
                out.write("0 ")
                break


def parentsHasCitizenship(mateNum, countryNum, reqCitizenship, prntCitiznshp):
    if prntCitiznshp[mateNum] - 1 == countryNum and reqCitizenship[countryNum] == 1:
        return True
    return False


def incomeIsEnough(mateNum, countryNum, reqIncome, clsIncome):
    return reqIncome[countryNum] <= clsIncome[mateNum]


def hasEducation(mateNum, countryNum, reqEduc, clsEduc):
    if reqEduc[countryNum] == 0 or (reqEduc[countryNum] == 1 and clsEduc[mateNum] == 1):
        return True
    return False


if __name__ == '__main__':
    main()
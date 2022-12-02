# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    calorie_list = open("input1")

    rich_johns = []
    rich_johns.append([])
    iterator = 0
    for each in calorie_list:
        if each == "\n":
            rich_johns.append([])
            iterator +=1
        else:
            rich_johns[iterator].append(int(each))

    totals = []
    for each in rich_johns:
        total = sum(each)
        totals.append(total)
    totals.sort(reverse=True)

    top_three =totals[0] + totals[1] + totals[2]
    print(top_three)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

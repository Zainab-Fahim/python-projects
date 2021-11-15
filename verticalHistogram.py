#Given an array, print a verticle hustogram
def histogram(list):
    title = "Title1     \tTitle2    \tTitle3    \tTitle4"
    print(title)
    while not all(n <= 0 for n in list):
        toPrint = ''

        for i in range(len(list)):
            if list[i] > 0:
                toPrint += '*\t\t'
                list[i] -= 1
            else:
                toPrint += ' \t\t'

        print(toPrint)


histogram([2, 0, 4, 3])

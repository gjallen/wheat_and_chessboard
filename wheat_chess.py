board = []
i = 1
j = 1
total = 0

def kg(wheat):
    kg_weight = round(wheat * 0.00002, 1)
    return kg_weight


def ton(wheat):
    ton_weight = round(wheat * 0.00000002, 1)
    return ton_weight


def titanic():
    titanic_weight = round(ton(j) / 52000, 1)
    return titanic_weight


def empire():
    empire_weight = round(ton(j) / 365000, 1)
    return empire_weight


def hoover():
    hoover_weight = round(ton(j) / 6600000, 1)
    return hoover_weight


def km():
    km_weight = round(ton(j) / 1000000000, 1)
    return km_weight


def coal():
    coal_weight = round(ton(j) / 1730000000, 1)
    return coal_weight


while i < 65:
    board.append(j)
    if j == 1:
        print("")
        print("There is 1 grain of wheat on square 1")
        total = total + j
        j = j * 2
        i = i + 1
        print("The running total is currently: 1 grain of wheat.")
        print("---")
    else:
        print(
            "There are " +
            str(j) +
            " grains of wheat on square " +
            str(i) +
            ".")
        total = total + j
        j = j * 2
        i = i + 1
        print(
            "The running total is currently: " +
            str(total) +
            " grains of wheat.")
        print("This equates to " + str(kg(j)) + " kgs of wheat.")
        print("This equates to " + str(ton(j)) + " tonnes of wheat.")
        print("This equates to " + str(titanic()) + " Titanics.")
        print("This equates to " + str(empire()) + " Empire State Buildings.")
        print("This equates to " + str(hoover()) + " Hoover Dams.")
        print("This equates to " + str(km()) + " cubic kilometers.")
        print("This equates to " + str(coal()) +
              " Chinese coal reserves (2009).")
        print("---")

print("")
print("-------------------------------------------------------")
print("In total there are " + str(total) + " grains of wheat.")
print("-------------------------------------------------------")
print("")

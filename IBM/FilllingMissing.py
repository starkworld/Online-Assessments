
def calcMissing(readings):
    list_dates = []
    list_prices = []
    for row in readings:
        raw_inp = row.split(sep=" ")
        list_dates.append(raw_inp[0]), list_prices.append(raw_inp[-1].split(sep="\t")[-1])

    missing_indices = []
    for i in range(len(list_prices)):
        try:
            list_prices[i] = float(list_prices[i])
        except:
            missing_indices.append(i)

    for i in missing_indices:
        list_floats = []
        a, b = i - 1, i + 1
        while len(list_floats) < 1:
            a, b = max(0, a - 1), b + 1
            for j in list_prices[a:b]:
                if type(j) == float:
                    list_floats.append(j)
        print(round(sum(list_floats) / len(list_floats), 2))

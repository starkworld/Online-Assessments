def airplaneLandings(arr, dep, maxWaitTIme, initialPlanes):

    currentPlanes = initialPlanes
    currentDeparturePosition = 0
    maxArrival = 1

    for i in range(len(arr)):
        arrTime = arr[i]
        maxArrival = max(maxArrival, currentPlanes)
        currentPlanes += 1

        for j in range(currentDeparturePosition, len(dep)):
            if dep[j] - arrTime < maxWaitTIme:
                currentDeparturePosition = j
                currentPlanes -= 1
            else:
                break

    return maxArrival


print(airplaneLandings([630, 645, 730, 1100], [700, 845, 1015, 1130], 20, 1))

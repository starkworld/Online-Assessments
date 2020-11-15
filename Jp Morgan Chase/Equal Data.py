def getResult():
    # ask for file name input

    filename = '/Users/nikhilkalyan/Online-Assessments/Jp Morgan Chase/data.csv'

    # initial dictionary

    dict1 = {"key": 0}

    dict2 = {"key": 0}

    # open file as f

    with open(filename) as f:

        # read line by line

        for line in f:

            # make a list

            line = list(line.split(","))

            # skip for new line

            if len(line) == 1:
                continue

            # year value

            header1 = line[0].replace(" ", "")

            # skip for words year i.e header

            if header1 == "year":
                continue

            # len  = 2 means second data sample

            if len(line) == 2:
                # get year and value

                # also replace space and new line with empty

                header2 = line[1].replace(" ", "")

                header2 = line[1].replace("\n", "")

                # add to dict2

                dict2[header1] = int(header2)

            # len  = 1 means first data sample

            if len(line) == 4:

                header2 = line[3].replace(" ", "")

                header2 = line[3].replace("\n", "")

                # add to dict2

                if header1 in dict1:

                    # Add yearwise data

                    dict1[header1] = int(dict1[header1]) + int(header2)

                else:

                    # first year wise data

                    dict1[header1] = int(header2)

                    # print(dict1)

        # print(dict2)

        # iterate key,value of dict

        for year1, value1 in dict1.items():

            # check same key is present in dict2 or not

            if year1 in dict2.keys():

                # compare value

                if dict2[year1] != value1:
                    return 0



            else:

                return 0

        # valid data

        return 1


# func calling

res = getResult()

# print result

if res == 1:

    print("TRUE")

else:

    print("FALSE")

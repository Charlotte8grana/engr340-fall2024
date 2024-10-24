import sys



def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    #Thought process: I want to find the first time a case value was recorded meaning greater than zero
    #within the cases column specifically for rockingham county and harrisonburg
    #from there, I want to read the date from that specific entry to determine the date which the first
    #case(s) was determined

    #ASSUMPTION: A city is only mentioned if there is a case, iterate through the list to find the county
    #which will give the number of cases and the date.
    #ASSUMPTION: Data is in order by date

    #if some line in the data set where column 1 = Harrisonburg city, then print that line
    for line in data:
        if line[1] == 'Harrisonburg city':
            print('The first positive COVID case in Harrisonburg was ' + line[0])
            break

    #if some line in the data set where column 1 = rockingham, then print that line
    for another_line in data:
        if another_line[1] == 'Rockingham':
            print('The first positive COVID case in Rockingham was ' + another_line[0])
            break

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here

    #cannot use a max function because it compares the whole list, so must find max another way

    #Create an empty list that has the same number of columns as the data list
    slot = [0, 0, 0, 0, 0, 0]
    #Iterate through each line in the data set where first the line needs to have the city as
    #harrisonburg, then if that is true, then the line needs to compare it to each iteration
    #to find the greatest, or maximum, number of cases then print the date for that line.
    for line in data:
        if line[1] == 'Harrisonburg city':
            if line[4] > slot[4]:
                slot = line
    print('The day where the greatest number of COVID cases occurred in Harrisonburg was ' + slot[0])

    #Same here, make an empty list to hold the line
    slot = [0, 0, 0, 0, 0, 0]
    # Iterate through each line in the data set where first the line needs to have the city as
    # rockingham, then if that is true, then the line needs to compare it to each iteration
    # to find the greatest, or maximum, number of cases then print the date for that line.
    for line in data:
        if line[1] == 'Rockingham':
            if line[4] > slot[4]:
                slot = line
    print('The day where the greatest number of COVID cases occurred in Rockingham was ' + slot[0])

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    #Want to use a similar ideas as question 2 but instead look at 7 consecutive days in either rockingham
    #or harrisonburg

    #NOTE: tried several times to think of a solution, but could not come up with code that would
    #run. So, the code below is as far as I could figure out, but is commented out as it does not run.

    #slot = [0, 0, 0, 0, 0, 0]
    #for line in data:
        #if line[1] == 'Harrisonburg city' or line[1] == 'Rockingham':
            #if sum(line[4]) > sum(slot[4]) in range(1,8):
                #slot = line
    #Here it should be two slot periods as it is from a start day to an end day (7 days later)
    #print('The worst 7 day period in ' + line[1] + ' was from ' + slot[0])
    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)

    #See def question_one print out

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    #See def question_two print out

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)

    #See def question_three comments


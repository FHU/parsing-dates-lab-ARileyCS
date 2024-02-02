#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    if month == "January":
        return "01"
    elif month == "February":
        return "02"
    elif month == "March":
        return "03"
    elif month == "April":
        return "04"
    elif month == "May":
        return "05"
    elif month == "June":
        return "06"
    elif month == "July":
        return "07"
    elif month == "August":
        return "08"
    elif month == "September":
        return "09"
    elif month == "October":
        return "10"
    elif month == "November":
        return "11"
    else:
        return "12"
#comment

def parse_day(user_string):
    day = user_string[user_string.find(" ") + 1:user_string.find(",")]
    if len(day) != 2:
        day = "0" + day
    return day

def parse_year(user_string):
    year = user_string[-4:]
    return year

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    month = parse_month(user_string[:user_string.find(" ")])
    day = parse_day(user_string)
    year = parse_year(user_string)
    
    date = [month, day, year]
    return "/".join(date)

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    
    user_string = input()
    
    while user_string != "-1":
        print(parse_date(user_string))

        user_string = input()
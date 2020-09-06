import datetime
import locale

def calc_datetime_difference(date1, date2):
    diff = date2 - date1
    return diff.seconds

def date_format():

    # locale.setlocale(locale.LC_TIME,'')
    # date_format = locale.nl_langinfo(locale.D_FMT)
    date_format = '%Y-%m-%dT%H:%M'
    return date_format

def date_convert(start,end):
        
        start_datetime = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M')
        end_datetime = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M')

        start_date_string=start_datetime.strftime('%Y-%m-%d')
        end_date_string=start_datetime.strftime('%Y-%m-%d')

        diff = calc_datetime_difference(start_datetime, end_datetime)

        return (start, end,  start_date_string, end_date_string, diff)


temp = date_convert('2000-12-2T08:00','2000-12-2T16:00')

print(temp[1])
print(type(temp))
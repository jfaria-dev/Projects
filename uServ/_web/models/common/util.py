from dateutil.parser import parse

def convert_date_string_to_datetime(date_string):
    try:
        date_object = parse(date_string)
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return None
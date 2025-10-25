import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    temp = str(temp)
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%A %d %B %Y")
# variables scope

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    inputs = float(temp_in_fahrenheit)
    temp_in_celsius = (inputs - 32) * 5.0 / 9.0
    return round(temp_in_celsius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
    mean = sum(float(x) for x in weather_data) / len(weather_data)
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    reader = []
    # Using a context manager to open the file
    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
        # Each row in the data gets converted into a list. 
            # if not row:
            #     continue  # Skip empty rows
            # reader.append(row)
            if row:
                max = int(row[2])
                min = int(row[1])
                reader.append([row[0], min, max])
    return reader


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # 1. Filter out empty strings or None values
    cleaned = [float(inputs) for inputs in weather_data if inputs != '' and inputs is not None]

    # 2. Handle the case where all data was empty
    if not cleaned:
        return ()

    # 3. Find the min value and its index
    min_value = min(cleaned)
    min_index = len(cleaned) - 1 - cleaned[::-1].index(min_value)
    return min_value, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    cleaned = [float(inputs) for inputs in weather_data if inputs != '' and inputs is not None]

    # 2. Handle the case where all data was empty
    if not cleaned:
        return ()

    # 3. Find the min value and its index
    max_value = max(cleaned)
    max_index = len(cleaned) - 1 - cleaned[::-1].index(max_value)
    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min_list = []
    max_list = []
    day = len(weather_data)

    for temp in weather_data:
        min_list.append(temp[1])
        max_list.append(temp[2])

    min_f, min_index = find_min(min_list)
    min_c = convert_f_to_c(min_f)
    min_cd = format_temperature(min_c)

    max_f, max_index = find_max(max_list)
    max_c = convert_f_to_c(max_f)
    max_cd = format_temperature(max_c)

    min_date = weather_data[min_index][0]
    min_iso_date = convert_date(min_date)

    max_date = weather_data[max_index][0]
    max_iso_date = convert_date(max_date)

    average_low = calculate_mean(min_list)
    avg_min_c = convert_f_to_c(average_low)
    avg_min_cd = format_temperature(avg_min_c)

    average_high = calculate_mean(max_list)
    avg_max_c = convert_f_to_c(average_high)
    avg_max_cd = format_temperature(avg_max_c)


    # print(f'{day} Day Overview')
    # print('next line')
    # or 
    return (f"""{day} Day Overview
  The lowest temperature will be {min_cd}, and will occur on {min_iso_date}.
  The highest temperature will be {max_cd}, and will occur on {max_iso_date}.
  The average low this week is {avg_min_cd}.
  The average high this week is {avg_max_cd}.
""")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_output = ''
    for daily_report in weather_data:
        min_c = convert_f_to_c(daily_report[1])
        max_c = convert_f_to_c(daily_report[2])
        date = convert_date(daily_report[0])
        min_cd = format_temperature(min_c)
        max_cd = format_temperature(max_c)

        daily_output += (f"""---- {date} ----
  Minimum Temperature: {min_cd}
  Maximum Temperature: {max_cd}\n\n""")
    return daily_output


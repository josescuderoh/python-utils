def fix_names(names):
    """
    This function takes a list of names and standardizes the names
    for Python analysis returning a list of fixed names to be used in
    the dataframe.

    names: list of strings to be fixed

    >>> fix_names(['New Col 1', 'NeW. Col. 2_'])
    ['new_col_1', 'new_col_2']

    """
    import re

    fixed_names = [name.lower().replace(' ','_').strip('_') for name in names]
    fixed_names = [re.sub(r'[^\w_]', '', name) for name in fixed_names]

    return fixed_names

def break_string(string, sep=' '):
    """
    Take one string and breaks it into a list of elements using the sep inside the string.

    string: string to break apart
    sep: separator (default: space)

    Example:

    >>> break_string('RA RA FZFG BR')
    {'RA': 2, 'FZFG': 1, 'BR': 1}

    >>> break_string('RA, RA, FZFG, BR', sep=',')
    {'RA': 2, 'FZFG': 1, 'BR': 1}
    """

    import re
    from collections import defaultdict

    if string.strip() != '':
        sym_count = defaultdict(int)
        for sym in re.split(''.join([sep, '+']) , string.strip()):
            sym_count[sym.strip()] += 1
    else:
        sym_count = {}

    return dict(sym_count)

def get_previous_quantity(df, q='units', date='date'):
    """Takes a dataframe with a datetime column and a numerical column and appends a new column with the
    quantity for the previous day. If there were no quantities the day before, it returns zero.

    >>> from datetime import datetime, timedelta
    >>> import pandas as pd

    >>> sales = {'date': [datetime.today() - timedelta(days=4),\
    datetime.today() - timedelta(days=2),\
    datetime.today() - timedelta(days=1),\
    datetime.today()], \
    'units': [5,4,3,2]}

    >>> sales_df = pd.DataFrame(sales)

    >>> get_previous_quantity(sales_df)['previous_units'].to_list()
    [0.0, 0.0, 4.0, 3.0]

    """
    from datetime import timedelta

    df = df.sort_values(by=date, ascending=True)

    # Calculate previous day's units
    df['previous_units'] = df[q].shift(1)
    df.loc[df['previous_units'].isna(), 'previous_units'] = 0

    # Flag if the difference between current and previous is 1 day
    df['has_prev_day'] = df[date].diff() == timedelta(1)

    # Set to zero if it's not
    df.loc[df['has_prev_day'] == False, 'previous_units'] = 0

    df.drop(columns=['has_prev_day'], inplace=True)

    return df

def flag_holiday(day, country, prov=None):
    """Return a flag if the day given is a holiday according to country, province and years in the
    format required by the holidays package.

    day: datetime object with with the day that needs to be queried.
    country: ISO 3166 code for the country.
    prov: ISO 3166-2 code for the province/state

    >>> import datetime
    >>> day1 = datetime.datetime.strptime('2017-12-26', '%Y-%m-%d')
    >>> flag_holiday(day1, 'CA', 'ON')
    1
    >>> day2 = datetime.datetime.strptime('2019-07-04', '%Y-%m-%d')
    >>> flag_holiday(day2, 'US')
    1

    """

    import holidays

    #Get datetimes
    holidays_list = list(holidays.CountryHoliday(country=country, years=day.year, prov=prov).keys())
    # Format as strings
    holidays_dates = [day.strftime('%Y-%m-%d') for day in holidays_list]
    # Compare
    flag = day.strftime('%Y-%m-%d') in holidays_dates
    return int(flag)

if __name__ == '__main__':
  import doctest
  doctest.run_docstring_examples(fix_names, globals())
  doctest.run_docstring_examples(break_string, globals())
  doctest.run_docstring_examples(get_previous_quantity, globals())
  doctest.run_docstring_examples(flag_holiday, globals())

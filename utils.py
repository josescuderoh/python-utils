def fix_names(names):
  """This function takes a list of column names and standardizes the names
  for Python analysis returning a list of fixed names

  >>> fix_names(['New Col 1', 'NeW. Col. 2'])
  ['new_col_1', 'new_col_2']

  """
  import re

  fixed_names = [name.lower().strip().replace(' ','_') for name in names]
  fixed_names = [re.sub(r'[^\w_]', '', name) for name in fixed_names]

  return fixed_names

def break_string(string):
    """
    Take one string and break it into a list of elements given the spaces inside the string.
    Example:

    >>> break_string('RA RA FZFG BR')
    {'RA': 2, 'FZFG': 1, 'BR': 1}
    """

    import re
    from collections import defaultdict

    if string.strip() != '':
        sym_count = defaultdict(int)
        for sym in re.split('\s+', string.strip()):
            sym_count[sym] += 1
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

if __name__ == '__main__':
  import doctest
  doctest.run_docstring_examples(fix_names, globals())
  doctest.run_docstring_examples(break_string, globals())
  doctest.run_docstring_examples(get_previous_quantity, globals())

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

if __name__ == '__main__':
  import doctest
  doctest.run_docstring_examples(fix_names, globals())
  doctest.run_docstring_examples(break_string, globals())

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

if __name__ == '__main__':
  import doctest
  doctest.run_docstring_examples(fix_names, globals())

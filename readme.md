# Python Utils

This repo (under construction) contains a script with a series useful functions for data processing in Python tested using doctest and with examples:

* `fix_names()`: This function takes a list of column names and standardizes the names for Python analysis returning a list of fixed names.

* `break_string()`: Take one string and break it into a list of elements given the spaces inside the string.

* `get_previous_quantity()`: Takes a dataframe with a datetime column and a numerical quantity column and appends a new column with the quantity for the previous day for each row. If there were no quantities the day before, it returns zero.

* (...)

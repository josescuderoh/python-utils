# Python Utils

This repo (under construction) contains a script with a series useful functions for data processing in Python tested using doctest and with examples:

* `fix_names()`: This function takes a list of column names and standardizes the names
 for Python analysis returning a list of fixed names.

 * `break_string()`: Take one string and break it into a list of elements given the spaces inside the string.

 * `get_previous_quantity()`: Takes a dataframe with a datetime column and a numerical column and appends a new column with the
   quantity for the previous day. If there were no quantities the day before, it returns zero.

* (...)

# Project Utils

Based on the 4D Development process, I have outlined a useful guide of how a DS pipeline would look like from beginning to end, with specific Python code to be used in every step of the process (when it's needed). Those steps are contained in the file [4D_Pipe](4D_Pipe.ipynb) containing the following:

1. **Define**: TBD
2. **Discover**: functions and notes on EDA (exploratory data analysis) step, carried out to know the data and carefully hypothesize and formulate a solution to the problem defined to the findings.
3. **Develop**: TBD
4. **Deploy**: TBD

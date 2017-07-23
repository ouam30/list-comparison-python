# list-comparison-python
Python function which accepts any number of lists as parameters and returns:
- Strings that appear in more than one list
- The total number of unique strings across all lists
- The total number of strings that were processed

## Modules required for unit testing
- pytest
- coverage
- pytest-cov

## Command line options

### Run the function:
ListComparison.py

### Unit test (using Pytest):
python -m pytest -v

### Unit test including code coverage and html report:
python -m pytest --cov-report html --cov ListComparison

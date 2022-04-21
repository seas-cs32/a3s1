'''Simple Python program without type annotations

This example was inspired by the examples in `mypy` doc's Common Issues.
https://mypy.readthedocs.io/en/latest/common_issues.html

PROBLEM: Instead of `split`, we probably meant to type `strip`.
'''

def make_parenthetical(a):
    return '(' + a.split() + ')'

main_pt = 'CS 32 students help each other'
clarification = 'within the collaboration rules'

print(main_pt + ' ' + make_parenthetical(clarification) + '.')
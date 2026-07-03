from unittest import main
from test_module import TestCalculate
from mean_var_std import calculate

print(calculate([0,1,2,3,4,5,6,7,8]))

main(module='test_module', exit=False, verbosity=2)
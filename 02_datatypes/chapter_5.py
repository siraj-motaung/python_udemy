# In standard floating-point arithmetic, 0.1 + 0.1 + 0.1 - 0.3 results in a small error like 4.44e-16,
# but with the Decimal module, the result is exactly 0.0. 

import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = Decimal('95.5')
current_temp = Decimal('95.49')

f1 =  Fraction(1, 2)

print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Fraction {f1 + 0.5}")
print(f"Difference temp {ideal_temp - current_temp}")

print(sys.float_info)

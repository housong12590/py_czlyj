import re

num_reg = r'^(\d*)\.?\d{2}?$'

print(re.match(num_reg, '11111'))

import re
s = "SalemAlemBulYerkezhan"
x = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
print(x)

# Question — What does this print?

print((3 + 10**2 / 2) or 70.0)

# Step by step (operator precedence: ** > / > +):
# 10**2 = 100
# 100 / 2 = 50.0  (division always returns float!)
# 3 + 50.0 = 53.0
# 53.0 or 70.0 → 53.0 is truthy, so "or" returns 53.0

# Answer: 53.0

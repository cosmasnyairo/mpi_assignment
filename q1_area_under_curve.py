from numpy import trapz

# from the curve we take the y intercept values
y = [4, 6, 6, 4, 4, 5]

# we take the x interval value
x_interval=2

# we Compute the area using the trapezoidal rule.
area = trapz(y, dx=x_interval)
print("Area under the curve is =", area)

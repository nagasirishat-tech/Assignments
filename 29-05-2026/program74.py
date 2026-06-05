import math
C=50
H=30
def calculate(D):
    return str(int(math.sqrt(2*C*D/H)))
input_sequence = input("Enter the value of D: ")
D_values = input_sequence.split(',')
results = [calculate(int(D)) for D in D_values]
print(','.join(results))

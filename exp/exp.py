import math
x = -5.1;
eps = 0.000000000000001;
lastSum = 1.0;
result = 1.0;

n = 1;

while abs(lastSum) >= eps :
    lastSum = lastSum * x / n;
    result += lastSum;
    n += 1;
    
print 'e^',x, " = ", result; 

print 'e^',x, " = ", math.exp( x ); 
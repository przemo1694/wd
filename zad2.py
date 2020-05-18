import sys

print ("a:",end='')
a = int(sys.stdin.readline())
print ("b:",end='')
b = int(sys.stdin.readline())

c = a + b

print ("a + b = ",end='')
sys.stdout.write(str(c));
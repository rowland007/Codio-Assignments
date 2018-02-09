
# Get our car speeds from the command line
import sys
speed1 = int(sys.argv[1])
speed2 = int(sys.argv[2])

# Write your code below
print('fast cars' if (speed1 > 70 or speed2 > 70) else 'ok')
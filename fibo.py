import math, random

def fibonacci_sphere(samples,randomize):
    rnd = 1.
    if randomize:
        rnd = random.random() * samples

    points = []
    offset = 2./samples
    increment = math.pi * (3. - math.sqrt(5.));

    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2);
        r = math.sqrt(1 - pow(y,2))

        phi = ((i + rnd) % samples) * increment

        x = math.cos(phi) * r
        z = math.sin(phi) * r

        points.append([x,y,z])

    return points

samples = 16
points = fibonacci_sphere(samples, False)

count = 0
for i in points:
    print ('point ' + str(count) + ': ' + str(points[count]))
    count += 1

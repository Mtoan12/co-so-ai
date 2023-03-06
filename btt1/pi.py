import math
import random

radius = 0.5

def isInsideCircle(x, y):
    xCenter = 0.5
    yCenter = 0.5

    distance = math.sqrt((x - xCenter) ** 2 + (y - yCenter) ** 2)

    if distance <= radius:
        return True

    return False

insideCount = 0
outsideCount = 0

index = 0

while index < 999999:
    x = random.random()
    y = random.random()

    if isInsideCircle(x, y):
        insideCount += 1
    else:
        outsideCount += 1

    index+=1

pointInSquare = insideCount + outsideCount
pointInCircle = insideCount

pi = 4 * (pointInCircle / pointInSquare)

print(pi)
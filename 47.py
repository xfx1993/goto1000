def carFleet( target, position, speed):
    count=0
    while True:
        nextpos = dict()
        for i in range(len(position)):
            if position[i] + speed[i] <= target:
                if position[i] + speed[i] not in nextpos:
                    nextpos[position[i] + speed[i]] = [position[i], speed[i]]
                else:
                    if position[i] > nextpos[position[i] + speed[i]][0]:
                        nextpos[position[i] + speed[i]] = [position[i], speed[i]]
            else:
                count+=1
        if not nextpos:
            break
        position = [key for key in nextpos.keys()]
        speed = [value[1] for value in nextpos.values()]

    return count

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target,position,speed))
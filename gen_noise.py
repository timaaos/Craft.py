from perlin_noise import PerlinNoise
import uuid
import math
def noise(size):
    noise = PerlinNoise(octaves=10, seed=uuid.uuid1().int>>64)
    xpix, ypix = size, size
    pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    print(len(pic))
    return pic
def noiseMountain(oldpic, mountHeight,size):
    noise1 = PerlinNoise(octaves=20)
    print('noise1')
    noise2 = PerlinNoise(octaves=21)
    print('noise2')
    noise3 = PerlinNoise(octaves=22)
    print('noise3')
    noise4 = PerlinNoise(octaves=23)
    print('noise4')

    xpix, ypix = size, size
    pic = []
    newnoise = noise(size)
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i / xpix, j / ypix])
            noise_val += 0.5 * noise2([i / xpix, j / ypix])
            noise_val += 0.25 * noise3([i / xpix, j / ypix])
            noise_val += 0.125 * noise4([i / xpix, j / ypix])
            print(i,j)
            noise_val -= oldpic[i][j]*mountHeight
            noise_val += newnoise[i][j]*mountHeight
            row.append(noise_val)
        pic.append(row)
    print(pic)
    return pic
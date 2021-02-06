from perlin_noise import PerlinNoise
def noise():
    noise = PerlinNoise(octaves=int(input("hills level(octaves, default 10): ")), seed=int(input("seed: ")))
    xpix, ypix = 250, 250
    pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    print(len(pic))
    return pic
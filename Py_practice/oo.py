import speedtest

#function that gets the download speed in mega bytes per second
def get_final_speed():
    rawspeed = speedtest.Speedtest().download()
    roundedspeed = round(rawspeed)
    finalspeed = roundedspeed / 1e+6
    return finalspeed

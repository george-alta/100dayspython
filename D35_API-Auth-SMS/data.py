cardinal_points = {340: "N", 350: "N", 360: "N", 10: "N", 20: "N",
                   30: "NE", 40: "NE", 50: "NE", 60: "NE",
                   70: "E", 80: "E", 90: "E", 100: "E", 110: "E",
                   120: "SE", 130: "SE", 140: "SE", 150: "SE",
                   160: "S", 170: "S", 180: "S", 190: "S", 200: "S",
                   210: "SW", 220: "SW", 230: "SW", 240: "SW",
                   250: "W", 260: "W", 270: "W", 280: "W", 290: "W",
                   300: "NW", 310: "NW", 320: "NW", 330: "NW",
                   }


def wind_direction(degree: float):
    """Returns the cardinal point direction of a given wind degree"""
    degree = int(round(degree, -1))
    direction = cardinal_points[degree]
    return direction

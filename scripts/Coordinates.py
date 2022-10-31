# This class takes as input a list of 4 coordinates, and can return:
# - Its region
# - Its projection
# - Its 

class Boundaries:


    def __init__(self, coordinates):

        # Set the boundaries for cube downloading (example: from Sit'Tlein bed's boundaries). You can grab them by just looking at the map above
        xmin = min(coordinates[0][1], coordinates[1][1])
        xmax = max(coordinates[0][1], coordinates[1][1])
        self.ymin = round_decimals(min(coordinates[0][0], coordinates[1][0]), min(coordinates[0][0], coordinates[1][0]), 2)
        self.ymax = round_decimals(max(coordinates[0][0], coordinates[1][0]), max(coordinates[0][0], coordinates[1][0]), 2)

        # Adjust the longitudes, because the map can give longitudes > 180 degrees if you scroll too much to the right
        self.xmin = round_decimals((xmin - int(xmin/180)*360), xmin, 2)
        self.xmax = round_decimals((self.xmax - int(self.xmax/180)*360), self.xmax, 2)

        self.points = [(yminWGS, xminWGS), (ymaxWGS, xmaxWGS)]


    def round_decimals(number:float, sign, decimals:int=2):

        """
        Returns a value rounded up to a specific number of decimal places.
        """
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("decimal places has to be 0 or more")
        elif decimals == 0:
            return math.ceil(number)

        factor = 10 ** decimals

        if sign > 0:
            return math.ceil(number * factor) / factor
        else:
            return math.floor(number * factor) / factor
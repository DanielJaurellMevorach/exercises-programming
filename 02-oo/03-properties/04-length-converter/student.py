"""class LengthConverter:
    def __init__(self, distance_in_meter = 0):
        self.meter = distance_in_meter
    
    @property
    def meter(self):
        return self.__meter
    
    @meter.setter
    def meter(self, distance):
        self.__meter = distance
        
    @property
    def feet(self):
        return self.__meter * 3.28084
    
    @feet.setter
    def feet(self, distance):
        self.feet = distance
        self.__meter = distance * 0.3048
        
    @property 
    def inches(self):
        return self.__meter * 39.3701
    
    @inches.setter
    def inches(self, distance):
        self.inches = distance
        self.__meter = distance / 39.3701"""
        
class LengthConverter:
    def __init__(self):
        self.__distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter

    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value

    @property
    def feet(self):
        return self.__distance_in_meter * 3.28084

    @feet.setter
    def feet(self, value):
        self.__distance_in_meter = value / 3.28084

    @property
    def inch(self):
        return self.__distance_in_meter * 39.3701

    @inch.setter
    def inch(self, value):
        self.__distance_in_meter = value / 39.3701
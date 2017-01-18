import random
import datetime

class GittieHelper():

    def __init__(self):
        """
        Initialize attributes with default value
        """
        self.temperature_degree = None
        self.humidity_value = None
        self.air_pollution_level = None
        self.day_number = None

    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree:
        """
        if temperature_degree not in range(-100, 101):
            raise ValueError("Temperature has to be between -100 an 100 degrees celcius")

        self.temperature_degree = temperature_degree

    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:
        """

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        if self.air_pollution_level not in range(1, 10):
            raise ValueError('Air polution level has to be integer from 1 to 10')

    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        if day_number.isdigit() is False:
            raise ValueError("day number has to bo digit!")

        self.day_number = day_number

    def get_value(self):
        """
        Method should calculate if exiting home is safe for gittie
        :param day_number:
        """
        all_values_dict = self.__dict__

        safe_to_leave = True
        if None not in all_values_dict.values():
            for key, value in all_values_dict.items():
                if key == "temperature_degree" and value not in range(-30, 30):
                    safe_to_leave = False
                elif key == "humidity_value" and 0.3 > value or value > 0.8:
                    safe_to_leave = False
                elif key == "air_pollution_level" and value > 7:
                    safe_to_leave = False
            return safe_to_leave

        else:
            raise ValueError("Not all values were given!")

class GittieHelper():

    def __init__(self):
        """
        Initialize attributes with default value
        """
        pass

    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree:
        """


    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:
        """
        if isinstance(humidity_value, float) and humidity_value > 0 and humidity_value < 1:
            self.humidity = humidity_value
        else:
            raise ValueError("huminidity vaule should be a float in range 0.0 - 1.0")

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        if str(air_pollution_level).isdigit() and air_pollution_level in range(0, 1001):
            self.air_pollition = air_pollution_level
        else:
            raise ValueError("air pollution should be a integer in range 0 - 1000")

    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        pass

    def get_value(self):
        """
        Method should calculate if exiting home is safe for gittie
        :param day_number:
        """




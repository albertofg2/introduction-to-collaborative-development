class Car:

    def __init__(self, color, license_plate, vin_number)
        self.color=color
        self._license_plate=license_plate
        self.__vin_number=vin_number


my_car=Car('red', '1234ABCD', '12340987')




. Find information about how to access each attribute type in Python.
2. Create a class `Car` that implements three attributes: `color`, `license_plate` and `vin_number`. **They should be public, protected and private, respectively**.
3. Create a car instance that gets `"red"` as color, `"1234ABCD"` as license plate and `12340987` as VIN number.
4. Create three variables (`ext_color`, `ext_license_plate` and `ext_vin_number`) that store the values of the attributes of **the car instance**.

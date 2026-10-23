class SmartDevice:
    def __init__(self, brand):
        self.brand = brand  
        self.__is_on = False

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, value):
        self.__is_on = value

    @is_on.deleter
    def is_on(self):
        del self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False 


class SmartLight(SmartDevice):
    def __init__(self, brand, brightness ):
        super().__init__(brand)
        self.brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if value < 0:
            raise ValueError("Value must be more then or equal to 0")
        
        if value > 100:
            raise ValueError("Value must be less then or equal to 100")
        
        self.__brightness = value

    @brightness.deleter
    def brightness(self):
        del self.__brightness

    def turn_on(self):
        super().turn_on()
        print(f"Brand: {self.brand}")
        print(f"Brightness: {self.brightness}")
        print(f"Light is on: {self.is_on}")

    def turn_off(self):
        super().turn_off()
        print(f"Brand: {self.brand}")
        print(f"Brightness: 0")
        print(f"Light is on: {self.is_on} \n")

smartLight = SmartLight("axali nateba", 20)
smartLight.turn_on()
smartLight.turn_off()

smartLight.brightness = 75
smartLight.turn_on()
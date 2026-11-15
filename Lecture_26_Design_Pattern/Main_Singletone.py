

class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = True
            cls._instance.theme = 'Dark'

        return cls._instance

    def show(self):
        print(f'Debug: {self.debug}, Theme: {self.theme}')

appconfig1 = AppConfig()
appconfig2 = AppConfig()

appconfig1.show()
appconfig1.debug = False
appconfig1.show()
appconfig2.show()

appconfig1.debug = True
appconfig1.show()
appconfig2.show()

print(id(appconfig1))
print(id(appconfig2))
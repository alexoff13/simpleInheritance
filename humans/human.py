class Human:
    def __init__(self, weight, height, name):
        self._weight = weight
        self._height = height
        self.name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value if 30 <= value <= 150 else self._weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value if 100 <= value <= 300 else self._height

    def say(self):
        print('Привет, я человек')

    def __str__(self):
        return f'Человек по имени:{self.name}\nВес:{self._weight}\nРост{self._height}'

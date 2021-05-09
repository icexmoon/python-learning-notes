class Plane():
    def __init__(self, model, number):
        self._model = model
        self._number = number

    def __str__(self):
        return "{} No:{:0>3d}".format(self._model, self._number)

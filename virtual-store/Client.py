class Client:
    def __init__(self, name, phone):
        self._name = name
        self.phone = phone

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

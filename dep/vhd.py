

class VHD():


    def __init__(self, filename):
        self.filename = filename


    def set_entity(self, entity):
        self.entity = entity

    def get_entity(self):
        return self.entity

    def set_dependency(self, dependency):
        self.dependency = dependency

    def get_dependency(self):
        return self.dependency
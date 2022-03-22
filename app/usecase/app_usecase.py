from abc import abstractmethod


class UseCase:
    @abstractmethod
    def run(self):
        pass


class ProductionUseCase(UseCase):
    def run(self):
        return "Production Code"

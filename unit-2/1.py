class Car:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

car = Car("Honda", "Civic", 2021)
car.start()
car.stop()

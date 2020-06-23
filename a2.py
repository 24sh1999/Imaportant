class Vehicle:
    def __init__(self,registration_number):
        self.registration_number=registration_number
    def run(self):
        print('The vehicle is running')
    def start(self):
        print('The Vehicle started')
    def stop(self):
        print('The vehicle stopped')
class Fourwheeler(Vehicle):
    def run(self):
        print('The four wheeler is running')
        super().run()
    def stop(self):
        print('The four wheeler stopped')

class Car(Fourwheeler):
    def __init__(self,registration_number,is_commercial):
        super().__init__(registration_number)
        self.is_commercial=is_commercial
    def run(self):
        print('the car is running')
        super().run()
    def start(self):
        print('the car started')
        super().run()
        super().stop()
car=Car(8585,False)
car.start()


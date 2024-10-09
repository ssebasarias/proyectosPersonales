class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehiculo {self.brand}. Ha sido vendido')
        else:
            print(f'El veiculo {self.brand}, No esta disponible')

    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
    
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')


class Car(Vehicle):

    def start_engine(self):
        if not self.is_available:
            return f'El motor del coche {self.brand} esta en marcha'
        else:
            return f'El coche {self.brand} no esta disponible'
            
    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche {self.brand} es ha detenido'
        else:
            return f'El coche {self.brand} no esta disponible'

class Bike(Vehicle):
    
    def start_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.brand} esta en marcha'
        else:
            return f'La bicicleta {self.brand} no esta disponible'
            
    def stop_engine(self):
        if self.is_available:
            return f'La bicicleta {self.brand} es ha detenido'
        else:
            return f'La bicicleta {self.brand} no esta disponible'
        
class Truck(Vehicle):
    
    def start_engine(self):
        if not self.is_available:
            return f'El motor del camion {self.brand} esta en marcha'
        else:
            return f'El motor del camion {self.brand} no esta disponible'
            
    def stop_engine(self):
        if self.is_available:
            return f'El motor del camion {self.brand} es ha detenido'
        else:
            return f'El motor del camion {self.brand} no esta disponible'
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle .sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'El vehiculo {self.brand} no esta disponible')

    def inquire_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            availablity = 'Disponible'
        else:
            availablity = 'No disponible'
            print(f'El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}')

class Dilership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicles: Vehicle):
        self.inventory.append(vehicles)
        print(f'El {vehicles.brand} ha sido añadido al inentario')

    def register_customers(self, customers: Customer):
        self.customers.append(customers)
        print(f'El {customers.name} ha sido añadido al inentario')

    def show_available_vehicles(self):
        print('Vehiculo diponibles')
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f'- {vehicle.brand} por {vehicle.get_price()}')

car1 = Car('Toyota', 'Corola', 20000)
bike1 = Bike('Yamaha', 'MT-07', 7000)
truck1 = Truck('Volvo', 'FH16', 80000)

customer1 = Customer('Carlos')

dealerhip = Dilership()
dealerhip.add_vehicles(car1)
dealerhip.add_vehicles(bike1)
dealerhip.add_vehicles(truck1)
dealerhip.show_available_vehicles()

#Cliente consulta vehiculo
customer1.inquire_vehicle(car1)
customer1.buy_vehicle(car1)

dealerhip.show_available_vehicles()

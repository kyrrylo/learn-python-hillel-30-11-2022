from vehicles import Vehicle


class CarService:
    def __init__(self, name):
        self.name = name

    def maintenance(self, vehicle: Vehicle):
        """
        Обслуживание транспортного средства
        """
        if not vehicle._construction_needed:
            print(f'На {self.name} проводится ТО для {vehicle}')
            for point in vehicle.maintenance_checklist:
                print(point)

            vehicle._maintenance_needed = False
            vehicle._km_passed_after_mt = 0.0
            print(f'ТО для {vehicle} успешно завершено!')
        else:
            print(f'{vehicle} не готово к ТО'
                  f' - его должны собрать на заводе!')
class Vehicle:
    # средство передвижения
    def __init__(self, speed_limit: int, wheel_count: int, tire_pressure: float, color: str, model: str):
        """
        Средство передвижения, отвечает за техническое состояния транспортного средства
        и передвижения с его помощью
        :param speed_limit: максимальная скорость, км/ч
        :param wheel_count: сколько колёс
        :param tire_pressure: давление в шинах
        :param color: цвет
        :param model: модель/производитель/название
        """
        self.speed_limit = speed_limit
        self.wheels = wheel_count
        self.tire_pressure = tire_pressure
        self.color = color
        self.model = model
        self.km_passed = float()
        self.construction_needed = True
        self.maintenance_needed = False

        self.construct()

    def __str__(self):
        return f'Транспортное средство {self.model} цвета {self.color}'

    def construct(self):
        """
        Сбор транспортного средства на заводе
        """
        print(f'На заводе исправно потрудились и создали шедевр: {self} на {self.wheels} колёсах!')
        self.construction_needed = False
        self.maintenance_needed = False

    def ride(self, km: float, local_speed_limit: float) -> float:
        """
        Проехать некое расстояние на транспортном средстве
        :param km: сколько км необходимо проехать
        :param local_speed_limit: максимальная скорость на этой местности, км/ч
        :return: время в часах, за которое это возможно (если время отрицательное - произошла ошибка)
        """
        if self.construction_needed:
            print(f'{self} не готово к перемещению'
                  f' - его должны собрать на заводе!')
            return -1
        if self.maintenance_needed:
            print(f'{self} не готово к перемещению и нуждается в обслуживании!')
            return -1
        actual_speed = min(local_speed_limit, self.speed_limit)
        return round(km / actual_speed, 2)

    def maintenance(self):
        """
        Обслуживание транспортного средства
        """
        pass

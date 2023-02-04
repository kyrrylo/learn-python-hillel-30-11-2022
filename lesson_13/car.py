from vehicle import Vehicle


class Car(Vehicle):
    pass
    # def ride(self, km: float, ) -> float:


if __name__ == '__main__':
    c = Car(
        speed_limit=150,
        wheel_count=4,
        tire_pressure=2.5,
        color='Silver',
        model='Toyota Corolla'
    )
    print(f'{c} проезжает 10км по городу за {c.ride(10, 50)} часов')

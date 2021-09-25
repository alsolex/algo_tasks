class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.free_places = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.free_places[carType] > 0:
            self.free_places[carType] -= 1
            return True
        return False


def main():
    big, medium, small = int(input()), int(input()), int(input())
    obj = ParkingSystem(big, medium, small)
    carTypes = [int(num) for num in input().split()]
    params = []
    for carType in carTypes:
        params.append(obj.addCar(carType))
    print("Answer: ", params)


if __name__ == "__main__":
    main()

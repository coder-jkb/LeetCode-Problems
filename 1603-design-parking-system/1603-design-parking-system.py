class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.B, self.M, self.S =  big, medium, small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.B > 0:
            self.B -= 1
            return True
            
        elif carType == 2 and self.M > 0:
            self.M -= 1
            return True
        
        elif carType == 3 and self.S > 0:
            self.S -= 1
            return True
        
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
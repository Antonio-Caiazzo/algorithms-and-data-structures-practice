# LeetCode 1603 - Design Parking System (Easy)
#
# Design a parking system that has a fixed number of slots for big, medium, and small cars.
#
# Implement the ParkingSystem class:
# - ParkingSystem(int big, int medium, int small) initializes the object.
# - bool addCar(int carType): returns True if there's space for carType, else False.
#
# carType is:
# - 1 → big
# - 2 → medium
# - 3 → small
#
# Example:
# Input:
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
#
# Output:
# [null, true, true, false, false]
#
# Time complexity: O(1)
# Space complexity: O(1)

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.content = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.content[carType - 1] -= 1
        return self.content[carType - 1] >= 0


# Test cases for ParkingSystem
def test_parking_system():
    print("Running test cases for ParkingSystem...")
    ps = ParkingSystem(1, 1, 0)
    assert ps.addCar(1) == True, "Test case 1 failed"
    assert ps.addCar(2) == True, "Test case 2 failed"
    assert ps.addCar(3) == False, "Test case 3 failed"
    assert ps.addCar(1) == False, "Test case 4 failed"

    ps2 = ParkingSystem(0, 0, 1)
    assert ps2.addCar(3) == True, "Test case 5 failed"
    assert ps2.addCar(3) == False, "Test case 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_parking_system()

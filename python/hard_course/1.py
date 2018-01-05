class MoneyBox:
    def __init__(self, capacity):
        self._capacity = capacity
        self._current = 0

    def can_add(self, v):
        if self._current + v <= self._capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self._current += v


moneyBox = MoneyBox(10)
moneyBox.add(5)
moneyBox.add(5)
moneyBox.add(5)
print(moneyBox._capacity)

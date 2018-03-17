class Queue:

    def __init__(self, buff_size: int):
        self._buff_size = buff_size
        self._arr = []
        self._arr_of_unused = []

    def push(self, arrival, departure, real_arrival_time):
        if not self.empty():
            while not self.empty() and self.top()[1] <= real_arrival_time: # bay be <=
                # если предыдуший уехал раньше
                self.pop()

        if not self.empty():
            back_pair = self.back()
            duration = departure - arrival
            arrival = back_pair[1]
            departure = arrival + duration
        if len(self._arr) < self._buff_size:
            self._arr.append((arrival, departure, real_arrival_time))
        else:
            self._arr_of_unused.append((arrival, departure, real_arrival_time))

    def pop(self) -> tuple:
        top_pair = self._arr.pop(0)
        if top_pair[0] == 362:
            a = 1
            pass
        self.check_unused(top_pair)
        print(top_pair[0])
        return top_pair

    def back(self):
        # returns last element
        if not self.empty():
            return self._arr[len(self._arr) - 1]

    def pop_all_unused(self):
        while len(self._arr_of_unused) > 0:
            print("-1")
            self._arr_of_unused.pop()

    def check_unused(self, top_pair):
        while len(self._arr_of_unused) > 0:
            top_pair_unused = self._arr_of_unused[0]
            if top_pair_unused[2] < top_pair[2]:
                self._arr_of_unused.pop(0)
                print("-1")
            else:
                break

    def top(self) -> tuple:
        #   returns first
        if not self.empty():
            return self._arr[0]

    def empty(self) -> bool:
        return len(self._arr) == 0


buff_size, n = map(int, input().split())
queue = Queue(buff_size)
for i in range(0, n):
    arrival, duration = map(int, input().split())
    departure = arrival + duration
    queue.push(arrival, departure, arrival)

while not queue.empty():
    queue.pop()

queue.pop_all_unused()


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            times = self.map[key]
            times.append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    # [ 1, 3, 4, 7, 9, 10] timestamp = 2
    #   L  R
    def binary_search(self, times, timestamp):
        left = 0
        right = len(times) - 1

        if timestamp < times[left][0]:
            return ""

        while left <= right:
            mid = (right + left) // 2
            if times[mid][0] == timestamp:
               return times[mid][1]
            if times[mid][0] < timestamp:
                left = mid + 1
            else :
                right = mid - 1

        # return right timestamp because this is actually the left most position at this point
        # and represents the largest timestamp less than our target
        return times[right][1]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            times = self.map[key]
            return self.binary_search(times, timestamp)
        return ""

def main():
    time_map = TimeMap()
    time_map.set("love","high",10)
    time_map.set("love","low",20)
    print(time_map.get("love", 5))
    print(time_map.get("love", 10))
    print(time_map.get("love", 15))
    print(time_map.get("love", 20))
    print(time_map.get("love", 25))

if __name__ == "__main__":
    main()

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
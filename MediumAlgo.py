import collections
import math
from typing import List

def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    dp_map = map_difficulty_with_profit(zip(difficulty, profit))
    print(dp_map)
    difficulty = sorted(difficulty)
    worker = sorted(worker)
    d = 0
    total = 0
    temp = 0

    for w in worker:
        while d < len(difficulty):
            if w >= difficulty[d]:
                temp = max(temp, dp_map[difficulty[d]])
                d += 1
            else:
                break
        total += temp
    return total
        

def map_difficulty_with_profit(zipped):
    dp_map = {}
    for difficulty, profit in zipped:
        if difficulty not in dp_map.keys():
           dp_map[difficulty] = profit
        else:
            dval = dp_map[difficulty]
            dp_map[difficulty] = max(dval, profit)
    return dp_map

# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]

# Input: servers = [31,96,73,90,15,11,1,90,72,9,30,88], 
# tasks = [87,10,3,5,76,74,38,64,16,64,93,95,60,79,54,26,30,44,64,71]
# Output: [6,9,5,4,10,5,0,8,4,2,11,9,3,7,1,4,0,4,1,8]
def assignTasks(servers: List[int]=None, tasks: List[int]=None) -> List[int]:
    import heapq
    import queue
    lst = get_zipped(servers)
    lst.sort(key=custom_priority)
    heapq.heapify(lst)
    i = 0
    out = []
    sec_to_server = {}
    work_queue = queue.Queue()
    work_queue.put(i)
    while not work_queue.empty():
        free_servers = sec_to_server.get(i, None)
        restore_servers(heapq, free_servers, lst)
        min_server, min_index = get_min_server(heapq, lst)
        if not min_server:
            i += 1
            if i < len(tasks):
                work_queue.put(i)
            continue
        item = work_queue.get()
        out.append(min_index)
        insert_into_dict(item + tasks[item], sec_to_server, min_server, min_index)
        i += 1
        if i < len(tasks):
            work_queue.put(i)
    return out
        


def custom_priority(item):
    # Custom comparison function to prioritize based on the first element of tuple
    # If first elements are equal, prioritize based on the second element
    return (item[0], item[1])

def get_zipped(servers) :
    index = [i for i in range(len(servers))]
    zipped = zip(servers, index)
    return list(zipped)

def restore_servers(my_heap, free_servers, lst):
    if free_servers:
        for s in free_servers:
           my_heap.heappush(lst, s) 

def insert_into_dict(time_interval, sec_to_server, server, index):
    val = sec_to_server.get(time_interval, None)
    if not val:
        sec_to_server[(time_interval)] = [(server, index)]
    else:
        next_val = (server, index)
        sec_to_server[(time_interval)].append(next_val)
    print(sec_to_server)

def get_min_server(my_heap, lst):
    if not lst:
        return None, None
    min_server, min_index = my_heap.heappop(lst)
    return min_server, min_index

def get_next_available_server_in_future(sec_to_server, time_interval):
    sorted_dict = dict(sorted(sec_to_server.items()))
    for key, val in iter(sorted_dict.items()):
        if key >= time_interval:
            quickest_time, quickest_available =  key, val
            break
    min_server, min_index = quickest_available.pop(0)
    sec_to_server.pop(quickest_time)
    if quickest_available:
        sec_to_server[quickest_time] = quickest_available
    return min_server, min_index

def minArrayLength(nums: List[int], k: int) -> int:
    res = []
    for n in nums:
        if n == 0:
            return 1
        if res and res[-1] * n <= k:
            res[-1] *= n
        else:
            res.append(n)
    return len(res)

def rotate(matrix: List[List[int]]) -> List[List[int]]:
    up_down_max = len(matrix) // 2
    for i in range(up_down_max):
        matrix = swap(matrix, i)
    matrix = transpose(matrix)    
    return matrix

def swap(matrix, i):
    last = len(matrix) - 1 - i
    temp = matrix[i]
    matrix[i] = matrix[last]
    matrix[last] = temp
    return matrix

def transpose(matrix):
    transposed = list(map(list, zip(*matrix)))
    return transposed

# https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/?envType=problem-list-v2&envId=5h1lvmem
def minEatingSpeed(piles: List[int], h: int) -> int:
    def bananas_finished() -> bool:
        total_time = sum(math.ceil(p/mid) for p in piles)
        return total_time <= h

    left = 1
    right = max(piles)
    while left < right:
        mid = left + (right - left)//2
        if bananas_finished():
            right = mid 
        else:
            left = mid + 1
    return right

'''
Nearly every one have used the Multiplication Table.
But could you find out the k-th smallest number quickly from the multiplication table? 
Given the height m and the length n of a m * n Multiplication Table,
and a positive integer k, you need to return the k-th smallest number in this table.
Example :
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9
The 5-th smallest number is 3 (1, 2, 2, 3, 3).
'''

def kthSmallestNumInMultiplicationTable(row, col, k):
    def enough(num) -> bool:
        count = 0
        for val in range(1, row + 1):
            add = min(num // val, col)
            if add == 0: 
                break
            count += add
        return count >= k 
    
    left = 1
    right = row * col
    while left < right:
        mid = left + (right - left) // 2
        if enough(mid):
            right = mid 
        else:
            left = mid + 1
    return left

def find_nth_digit(n):
    # Step 1: Determine the range where the nth digit falls
    digit_length = 1
    count = 9
    
    # Step 2: Identify the range of numbers that contains the nth digit
    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
    
    # Step 3: Find the actual number that contains the nth digit
    start = 10**(digit_length - 1)
    number = start + (n - 1) // digit_length
    
    # Step 4: Identify the digit within the number
    digit_index = (n - 1) % digit_length
    return int(str(number)[digit_index])

def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    # word = "internationalization"
    # abbr = "i12iz4n" -> true
    if len(abbr) > len(word):
        return False
    
    w_ptr = 0
    a_ptr = 0
    word = list(word)
    abbr = list(abbr)

    while a_ptr < len(abbr) and w_ptr < len(word):
        if not abbr[a_ptr].isdigit():
            if word[w_ptr] != abbr[a_ptr]:
                return False
            else:
                w_ptr += 1
                a_ptr += 1
        else:
            if self.has_leading_zero(abbr[a_ptr]):
                return False
            num = self.get_number(abbr[a_ptr:])
            a_ptr += len(num) 
            w_ptr += int(num) 
    return a_ptr == len(abbr) and w_ptr == len(word)

def get_number(self, word):
    nums = []
    for w in word:
        if w.isdigit():
            nums.append(w)
        else:
            break
    return ''.join(nums)

def has_leading_zero(self, c):
    return int(c) == 0


def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    gate, obstacle, empty_room = 0, -1, 2147483647

    m, n = len(rooms), len(rooms[0])

    empty_rooms = set()
    queue = collections.deque([])

    for x in range(m):
        for y in range(n):
            if rooms[x][y] == gate:
                queue.append((x,y, 0))
                empty_rooms.add((x,y))
            if rooms[x][y] == empty_room:
                empty_rooms.add((x,y))


    while queue:
        x, y, dist = queue.popleft()
        if (x, y) in empty_rooms:
            rooms[x][y] = dist
            empty_rooms.remove((x,y))
            queue.append((x+1, y, dist+1))
            queue.append((x-1, y, dist+1))
            queue.append((x, y-1, dist+1))
            queue.append((x, y+1, dist+1))

















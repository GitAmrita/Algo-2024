from typing import List


# def start_up():
#     print ('hello world')

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




       

        
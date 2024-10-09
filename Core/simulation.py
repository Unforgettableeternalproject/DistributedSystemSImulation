import simpy
import time
import numpy as np
import pandas as pd
from tqdm import tqdm
import psutil

np.random.seed(int(time.time()))

# 定義任務
class Task:
    def __init__(self, task_id, duration):
        self.task_id = task_id
        self.duration = duration

# 定義分散式系統模擬
class DistributedSystem:
    def __init__(self, env, num_nodes, strategy):
        self.env = env
        self.nodes = [simpy.Resource(env, capacity=1) for _ in range(num_nodes)]
        self.num_nodes = num_nodes
        self.strategy = strategy  # 調度策略
        self.logs = []

    def schedule(self, tasks):
        # 根據策略進行調度
        if self.strategy == 'SJF':
            tasks.sort(key=lambda x: x.duration)  # SJF策略：最短任務優先
        elif self.strategy == 'LLF':
            tasks.sort(key=lambda x: np.random.rand())  # 模擬LLF策略，隨機分配負載
        elif self.strategy == 'FCFS':
            tasks.sort(key=lambda x: x.task_id)  # FCFS策略：按任務到達順序
        elif self.strategy == 'RR':
            tasks = self.round_robin_schedule(tasks)
        
        for task in tqdm(tasks, desc=f"Scheduling tasks ({self.strategy}) with {self.num_nodes} nodes"):  # 使用tqdm顯示進度條
            node = self.select_node()
            self.env.process(self.execute_task(task, node))

    def round_robin_schedule(self, tasks):
        # 按照輪循方式分配任務
        rr_tasks = []
        nodes = len(self.nodes)
        for i, task in enumerate(tasks):
            rr_tasks.append((task, i % nodes))  # 輪循分配
        return [task for task, _ in sorted(rr_tasks, key=lambda x: x[1])]

    def select_node(self):
        # 隨機選擇一個節點
        return np.random.choice(self.nodes)

    def execute_task(self, task, node):
        with node.request() as req:
            yield req  # 獲取資源
            start_time = self.env.now
            yield self.env.timeout(task.duration)  # 模擬任務執行
            end_time = self.env.now
            memory_usage = psutil.virtual_memory().percent  # 獲取記憶體使用量
            self.logs.append((task.task_id, task.duration, start_time, end_time, memory_usage))

    def run(self, num_tasks):
        tasks = [Task(i, np.random.randint(1, 10)) for i in range(num_tasks)]
        self.schedule(tasks)

def simulate(strategy, num_tasks, num_nodes):
    env = simpy.Environment()
    system = DistributedSystem(env, num_nodes, strategy)
    system.run(num_tasks)
    env.run()
    return system.logs

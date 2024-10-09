import simpy
import numpy as np
import pandas as pd

# �w�q����
class Task:
    def __init__(self, task_id, duration):
        self.task_id = task_id
        self.duration = duration

# �w�q�������t�μ���
class DistributedSystem:
    def __init__(self, env, num_nodes, strategy):
        self.env = env
        self.nodes = [simpy.Resource(env, capacity=1) for _ in range(num_nodes)]
        self.strategy = strategy  # �ի׵���
        self.logs = []

    def schedule(self, tasks):
        # �ھڵ����i��ի�
        if self.strategy == 'SJF':
            tasks.sort(key=lambda x: x.duration)  # SJF�����G�̵u�����u��
        elif self.strategy == 'LLF':
            tasks.sort(key=lambda x: np.random.rand())  # ����LLF�����A�H�����t�t��
        
        for task in tasks:
            node = self.select_node()
            self.env.process(self.execute_task(task, node))

    def select_node(self):
        # �H����ܤ@�Ӹ`�I
        return np.random.choice(self.nodes)

    def execute_task(self, task, node):
        with node.request() as req:
            yield req  # ����귽
            start_time = self.env.now
            yield self.env.timeout(task.duration)  # �������Ȱ���
            end_time = self.env.now
            self.logs.append((task.task_id, task.duration, start_time, end_time))

    def run(self, num_tasks):
        tasks = [Task(i, np.random.randint(1, 10)) for i in range(num_tasks)]
        self.schedule(tasks)

def simulate(strategy, num_tasks, num_nodes):
    env = simpy.Environment()
    system = DistributedSystem(env, num_nodes, strategy)
    system.run(num_tasks)
    env.run()
    return system.logs

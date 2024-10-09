import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

def load_data_for_systems():
    dfs = []
    num_nodes = [1, 5, 20, 50, 100]
    for nodes in tqdm(num_nodes, desc="Loading data for systems"):
        df = pd.read_csv(f'Data/simulation_results_node_{nodes}.csv')
        df['Nodes'] = nodes
        df['Strategy'] = 'SJF'
        dfs.append(df)
    return pd.concat(dfs)

def load_data_for_strategies():
    dfs = []
    strategies = ['SJF', 'LLF', 'FCFS', 'RR']
    for strategy in tqdm(strategies, desc="Loading data for strategies"):
        df = pd.read_csv(f'Data/simulation_results_strategy_{strategy}.csv')
        df['Nodes'] = 15
        df['Strategy'] = strategy
        dfs.append(df)
    return pd.concat(dfs)

def calculate_resource_utilization(data, total_time, num_nodes):
    # 計算每個節點的總工作時間
    node_work_times = data.groupby('Nodes')['Duration'].sum()
    # 計算資源利用率
    utilization = (node_work_times / (total_time * num_nodes)) * 100
    return utilization

def analyze_data(data, experiment_type):
    if experiment_type == 'systems':
        # 計算每種節點數量的平均完成時間
        completion_time_avg = data.groupby('Nodes')['Completion_Time'].mean()

        # 繪製平均完成時間的折線圖
        plt.figure(figsize=(8, 6))
        completion_time_avg.plot(kind='line', marker='o', color='skyblue')
        plt.title('Average Task Completion Time by Number of Nodes')
        plt.ylabel('Average Completion Time (time units)')
        plt.xlabel('Number of Nodes')
        plt.savefig('average_completion_time_by_nodes.png')
        plt.show()

        # 計算資源利用率
        total_time = data['End_Time'].max()  # 總模擬時間
        utilization = calculate_resource_utilization(data, total_time, data['Nodes'].nunique())

        # 繪製資源利用率的折線圖
        plt.figure(figsize=(8, 6))
        utilization.plot(kind='line', marker='o', color='salmon')
        plt.title('Resource Utilization by Number of Nodes')
        plt.ylabel('Resource Utilization (%)')
        plt.xlabel('Number of Nodes')
        plt.savefig('resource_utilization_by_nodes.png')
        plt.show()

        # 計算記憶體使用量
        memory_usage_avg = data.groupby('Nodes')['Memory_Usage'].mean()

        # 繪製記憶體使用量的折線圖
        plt.figure(figsize=(8, 6))
        memory_usage_avg.plot(kind='line', marker='o', color='green')
        plt.title('Average Memory Usage by Number of Nodes')
        plt.ylabel('Memory Usage (%)')
        plt.xlabel('Number of Nodes')
        plt.savefig('memory_usage_by_nodes.png')
        plt.show()

    elif experiment_type == 'strategies':
        # 計算每種策略的平均完成時間
        completion_time_avg = data.groupby('Strategy')['Completion_Time'].mean()

        # 繪製平均完成時間的長條圖
        plt.figure(figsize=(8, 6))
        completion_time_avg.plot(kind='bar', color=['skyblue', 'lightgreen', 'lightcoral', 'lightyellow'])
        plt.title('Average Task Completion Time by Strategy')
        plt.ylabel('Average Completion Time (time units)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig('average_completion_time_by_strategy.png')
        plt.show()

        # 計算資源利用率
        total_time = data['End_Time'].max()  # 總模擬時間
        utilization = calculate_resource_utilization(data, total_time, data['Strategy'].nunique())

        # 繪製資源利用率的長條圖
        plt.figure(figsize=(8, 6))
        utilization.plot(kind='bar', color=['salmon', 'lightblue', 'lightgreen', 'lightpink'])
        plt.title('Resource Utilization by Strategy')
        plt.ylabel('Resource Utilization (%)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig('resource_utilization_by_strategy.png')
        plt.show()

        # 計算記憶體使用量
        memory_usage_avg = data.groupby('Strategy')['Memory_Usage'].mean()

        # 繪製記憶體使用量的長條圖
        plt.figure(figsize=(8, 6))
        memory_usage_avg.plot(kind='bar', color=['green', 'lightblue', 'lightgreen', 'lightpink'])
        plt.title('Average Memory Usage by Strategy')
        plt.ylabel('Memory Usage (%)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig('memory_usage_by_strategy.png')
        plt.show()

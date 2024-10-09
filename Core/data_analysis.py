import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

output_path = 'Data/Graphs/'

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

def calculate_resource_utilization(data, total_time, group_by):
    group_work_times = data.groupby(group_by)['Duration'].sum()
    utilization = (group_work_times / (total_time * data['Nodes'].nunique()))
    return utilization

def annotate_points(ax, data):
    for i, (index, value) in enumerate(data.items()):
        ax.annotate(f'{value:.2f}', xy=(i, value), xytext=(0, 5), textcoords='offset points', ha='center')

def analyze_data(data, experiment_type):
    if experiment_type == 'systems':
        # 計算每種節點數量的平均完成時間
        completion_time_avg = data.groupby('Nodes')['Completion_Time'].mean()

        # 繪製平均完成時間的折線圖
        fig, ax = plt.subplots(figsize=(8, 6))
        completion_time_avg.plot(kind='line', marker='o', color='skyblue', ax=ax)
        annotate_points(ax, completion_time_avg)
        plt.title('Average Task Completion Time by Number of Nodes')
        plt.ylabel('Average Completion Time (time units)')
        plt.xlabel('Number of Nodes')
        plt.savefig(output_path + 'average_completion_time_by_nodes.png')
        plt.show()

        # 計算資源利用率
        total_time = data['End_Time'].max()  # 總模擬時間
        utilization = calculate_resource_utilization(data, total_time, 'Nodes')

        # 繪製資源利用率的折線圖
        fig, ax = plt.subplots(figsize=(8, 6))
        utilization.plot(kind='line', marker='o', color='salmon', ax=ax)
        annotate_points(ax, utilization)
        plt.title('Resource Utilization by Number of Nodes')
        plt.ylabel('Resource Utilization (%)')
        plt.xlabel('Number of Nodes')
        plt.savefig(output_path + 'resource_utilization_by_nodes.png')
        plt.show()

        # 計算記憶體使用量
        memory_usage_avg = data.groupby('Nodes')['Memory_Usage'].mean()

        # 繪製記憶體使用量的折線圖
        fig, ax = plt.subplots(figsize=(8, 6))
        memory_usage_avg.plot(kind='line', marker='o', color='green', ax=ax)
        annotate_points(ax, memory_usage_avg)
        plt.title('Average Memory Usage by Number of Nodes')
        plt.ylabel('Memory Usage (%)')
        plt.xlabel('Number of Nodes')
        plt.savefig(output_path + 'memory_usage_by_nodes.png')
        plt.show()

    elif experiment_type == 'strategies':
        # 計算每種策略的平均完成時間
        completion_time_avg = data.groupby('Strategy')['Completion_Time'].mean()

        # 繪製平均完成時間的長條圖
        fig, ax = plt.subplots(figsize=(8, 6))
        completion_time_avg.plot(kind='bar', color=['skyblue', 'lightgreen', 'lightcoral', 'lightyellow'], ax=ax)
        annotate_points(ax, completion_time_avg)
        plt.title('Average Task Completion Time by Strategy')
        plt.ylabel('Average Completion Time (time units)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig(output_path + 'average_completion_time_by_strategy.png')
        plt.show()

        # 計算資源利用率
        total_time = data['End_Time'].max()  # 總模擬時間
        utilization = calculate_resource_utilization(data, total_time, 'Strategy')

        # 繪製資源利用率的長條圖
        fig, ax = plt.subplots(figsize=(8, 6))
        utilization.plot(kind='bar', color=['salmon', 'lightblue', 'lightgreen', 'lightpink'], ax=ax)
        annotate_points(ax, utilization)
        plt.title('Resource Utilization by Strategy')
        plt.ylabel('Resource Utilization (%)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig(output_path + 'resource_utilization_by_strategy.png')
        plt.show()

        # 計算記憶體使用量
        memory_usage_avg = data.groupby('Strategy')['Memory_Usage'].mean()

        # 繪製記憶體使用量的長條圖
        fig, ax = plt.subplots(figsize=(8, 6))
        memory_usage_avg.plot(kind='bar', color=['green', 'lightblue', 'lightgreen', 'lightpink'], ax=ax)
        annotate_points(ax, memory_usage_avg)
        plt.title('Average Memory Usage by Strategy')
        plt.ylabel('Memory Usage (%)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig(output_path + 'memory_usage_by_strategy.png')
        plt.show()

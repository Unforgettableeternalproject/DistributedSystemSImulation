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
    # �p��C�Ӹ`�I���`�u�@�ɶ�
    node_work_times = data.groupby('Nodes')['Duration'].sum()
    # �p��귽�Q�βv
    utilization = (node_work_times / (total_time * num_nodes)) * 100
    return utilization

def analyze_data(data, experiment_type):
    if experiment_type == 'systems':
        # �p��C�ظ`�I�ƶq�����������ɶ�
        completion_time_avg = data.groupby('Nodes')['Completion_Time'].mean()

        # ø�s���������ɶ�����u��
        plt.figure(figsize=(8, 6))
        completion_time_avg.plot(kind='line', marker='o', color='skyblue')
        plt.title('Average Task Completion Time by Number of Nodes')
        plt.ylabel('Average Completion Time (time units)')
        plt.xlabel('Number of Nodes')
        plt.savefig('average_completion_time_by_nodes.png')
        plt.show()

        # �p��귽�Q�βv
        total_time = data['End_Time'].max()  # �`�����ɶ�
        utilization = calculate_resource_utilization(data, total_time, data['Nodes'].nunique())

        # ø�s�귽�Q�βv����u��
        plt.figure(figsize=(8, 6))
        utilization.plot(kind='line', marker='o', color='salmon')
        plt.title('Resource Utilization by Number of Nodes')
        plt.ylabel('Resource Utilization (%)')
        plt.xlabel('Number of Nodes')
        plt.savefig('resource_utilization_by_nodes.png')
        plt.show()

        # �p��O����ϥζq
        memory_usage_avg = data.groupby('Nodes')['Memory_Usage'].mean()

        # ø�s�O����ϥζq����u��
        plt.figure(figsize=(8, 6))
        memory_usage_avg.plot(kind='line', marker='o', color='green')
        plt.title('Average Memory Usage by Number of Nodes')
        plt.ylabel('Memory Usage (%)')
        plt.xlabel('Number of Nodes')
        plt.savefig('memory_usage_by_nodes.png')
        plt.show()

    elif experiment_type == 'strategies':
        # �p��C�ص��������������ɶ�
        completion_time_avg = data.groupby('Strategy')['Completion_Time'].mean()

        # ø�s���������ɶ���������
        plt.figure(figsize=(8, 6))
        completion_time_avg.plot(kind='bar', color=['skyblue', 'lightgreen', 'lightcoral', 'lightyellow'])
        plt.title('Average Task Completion Time by Strategy')
        plt.ylabel('Average Completion Time (time units)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig('average_completion_time_by_strategy.png')
        plt.show()

        # �p��귽�Q�βv
        total_time = data['End_Time'].max()  # �`�����ɶ�
        utilization = calculate_resource_utilization(data, total_time, data['Strategy'].nunique())

        # ø�s�귽�Q�βv��������
        plt.figure(figsize=(8, 6))
        utilization.plot(kind='bar', color=['salmon', 'lightblue', 'lightgreen', 'lightpink'])
        plt.title('Resource Utilization by Strategy')
        plt.ylabel('Resource Utilization (%)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig('resource_utilization_by_strategy.png')
        plt.show()

        # �p��O����ϥζq
        memory_usage_avg = data.groupby('Strategy')['Memory_Usage'].mean()

        # ø�s�O����ϥζq��������
        plt.figure(figsize=(8, 6))
        memory_usage_avg.plot(kind='bar', color=['green', 'lightblue', 'lightgreen', 'lightpink'])
        plt.title('Average Memory Usage by Strategy')
        plt.ylabel('Memory Usage (%)')
        plt.xlabel('Scheduling Strategy')
        plt.savefig('memory_usage_by_strategy.png')
        plt.show()

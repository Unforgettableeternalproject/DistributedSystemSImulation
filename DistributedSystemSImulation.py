# Main entrance of the program
import Core.simulation as sim
import Core.data_analysis as da
import pandas as pd

def experiment_systems():
    strategy = 'SJF'
    num_tasks = 5000  # ���������ȼƶq
    num_nodes = [1, 5, 20, 50, 100] # �`�I�ƶq
    
    # ����������
    for nodes in num_nodes:
        logs = sim.simulate(strategy, num_tasks, nodes)
        # �O�s�������G��CSV�ɮ�
        df = pd.DataFrame(logs, columns=['Task_ID', 'Duration', 'Start_Time', 'End_Time', 'Memory_Usage'])
        df['Completion_Time'] = df['End_Time'] - df['Start_Time']
        df.to_csv(f'Data/simulation_results_node_{nodes}.csv', index=False)

def experiment_strategies():
    strategies = ['SJF', 'LLF', 'FCFS', 'RR']
    num_tasks = 5000  # ���������ȼƶq
    num_nodes = 15  # �`�I�ƶq

    # ����������
    for strategy in strategies:
        logs = sim.simulate(strategy, num_tasks, num_nodes)
        # �O�s�������G��CSV�ɮ�
        df = pd.DataFrame(logs, columns=['Task_ID', 'Duration', 'Start_Time', 'End_Time', 'Memory_Usage'])
        df['Completion_Time'] = df['End_Time'] - df['Start_Time']
        df.to_csv(f'Data/simulation_results_strategy_{strategy}.csv', index=False)

if __name__ == "__main__":
    # �������
    experiment_systems()
    experiment_strategies()

    # �ƾڤ��R������
    data_systems = da.load_data_for_systems()
    da.analyze_data(data_systems, 'systems')

    data_strategies = da.load_data_for_strategies()
    da.analyze_data(data_strategies, 'strategies')

    print("All experiments were successfully completed!")
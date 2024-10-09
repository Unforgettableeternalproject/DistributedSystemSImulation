# Main entrance of the program
import Core.simulation as sim
import Core.data_analysis as da
import pandas as pd

if __name__ == "__main__":
    strategies = ['SJF', 'LLF']
    num_tasks = 100  # ���������ȼƶq
    num_nodes = 5  # �`�I�ƶq

    # ����������
    for strategy in strategies:
        logs = sim.simulate(strategy, num_tasks, num_nodes)
        # �O�s�������G��CSV�ɮ�
        df = pd.DataFrame(logs, columns=['Task_ID', 'Duration', 'Start_Time', 'End_Time'])
        df['Completion_Time'] = df['End_Time'] - df['Start_Time']
        df.to_csv(f'Data/simulation_results_{strategy}.csv', index=False)

    # �ƾڤ��R������
    data = da.load_data(strategies)
    da.analyze_data(data)
import pandas as pd
import matplotlib.pyplot as plt

def load_data(strategies):
    dfs = []
    for strategy in strategies:
        df = pd.read_csv(f'simulation_results_{strategy}.csv')
        df['Strategy'] = strategy
        dfs.append(df)
    return pd.concat(dfs)

def analyze_data(data):
    # �p��C�ص��������������ɶ�
    completion_time_avg = data.groupby('Strategy')['Completion_Time'].mean()

    # ø�s���������ɶ���������
    plt.figure(figsize=(8, 6))
    completion_time_avg.plot(kind='bar', color=['skyblue', 'lightgreen'], edgecolor='black')
    plt.title('Average Task Completion Time by Strategy')
    plt.ylabel('Average Completion Time (time units)')
    plt.xlabel('Scheduling Strategy')
    plt.savefig('average_completion_time.png')
    plt.show()

    # �p��귽�Q�βv�]²�Ƭ��C�Ӹ`�I�������t���ɶ��^
    utilization = data.groupby('Strategy')['Duration'].mean()

    # ø�s�귽�Q�βv��������
    plt.figure(figsize=(8, 6))
    utilization.plot(kind='bar', color=['salmon', 'lightblue'], edgecolor='black')
    plt.title('Average Resource Utilization by Strategy')
    plt.ylabel('Average Duration (time units)')
    plt.xlabel('Scheduling Strategy')
    plt.savefig('resource_utilization.png')
    plt.show()

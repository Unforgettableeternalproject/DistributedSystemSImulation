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
    # 計算每種策略的平均完成時間
    completion_time_avg = data.groupby('Strategy')['Completion_Time'].mean()

    # 繪製平均完成時間的長條圖
    plt.figure(figsize=(8, 6))
    completion_time_avg.plot(kind='bar', color=['skyblue', 'lightgreen'], edgecolor='black')
    plt.title('Average Task Completion Time by Strategy')
    plt.ylabel('Average Completion Time (time units)')
    plt.xlabel('Scheduling Strategy')
    plt.savefig('average_completion_time.png')
    plt.show()

    # 計算資源利用率（簡化為每個節點的平均負載時間）
    utilization = data.groupby('Strategy')['Duration'].mean()

    # 繪製資源利用率的長條圖
    plt.figure(figsize=(8, 6))
    utilization.plot(kind='bar', color=['salmon', 'lightblue'], edgecolor='black')
    plt.title('Average Resource Utilization by Strategy')
    plt.ylabel('Average Duration (time units)')
    plt.xlabel('Scheduling Strategy')
    plt.savefig('resource_utilization.png')
    plt.show()

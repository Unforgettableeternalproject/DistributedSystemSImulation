# Main entrance of the program
import Core.simulation as sim
import Core.data_analysis as da
import pandas as pd

if __name__ == "__main__":
    strategies = ['SJF', 'LLF']
    num_tasks = 100  # 家览ヴ叭计秖
    num_nodes = 5  # 竊翴计秖

    # 家览场だ
    for strategy in strategies:
        logs = sim.simulate(strategy, num_tasks, num_nodes)
        # 玂家览挡狦CSV郎
        df = pd.DataFrame(logs, columns=['Task_ID', 'Duration', 'Start_Time', 'End_Time'])
        df['Completion_Time'] = df['End_Time'] - df['Start_Time']
        df.to_csv(f'Data/simulation_results_{strategy}.csv', index=False)

    # 计沮だ猂场だ
    data = da.load_data(strategies)
    da.analyze_data(data)
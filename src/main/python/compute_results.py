import pandas as pd
import argparse
import numpy as np
import csv
import matplotlib.pyplot as plt

def compute_results(args):
    
    input_folder = args.input
    if args.output: 
        output_folder = args.output
    output_folder = input_folder

    monetdb_df = pd.read_csv(input_folder + "/output_monetdb_bm25_robertson_time.csv", sep=" ", names=['id', 'exec_time'])
    duckdb_df = pd.read_csv(input_folder + "/output_duckdb_bm25_robertson_time.csv", sep=" ", names=['id', 'exec_time'])

    avg_exec_time_duckdb = np.mean(duckdb_df['exec_time'])
    avg_exec_time_monetdb = np.mean(monetdb_df['exec_time'])

    with open(output_folder + '/avg_execution_times.csv', 'w', newline='') as file: 
        writer = csv.writer(file, delimiter=",", 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['monetdb', avg_exec_time_monetdb])
        writer.writerow(['duckdb', avg_exec_time_duckdb])
    
    monetdb_boxplot_avgs = []
    start_index = 0 
    end_index = 250
    for i in range(250): 
        idx = [index for index in range(i, len(monetdb_df.index), 250)]
        monetdb_boxplot_avgs.append(np.mean(monetdb_df['exec_time'].iloc[idx]))
    
    data = [monetdb_boxplot_avgs, duckdb_df['exec_time']]
    fig1, ax1 = plt.subplots()
    ax1.boxplot(data, vert=False)
    ax1.set_yticklabels(['MonetDB', 'DuckDB'])
    ax1.set_xlabel('Execution time (s)')
    ax1.set_title('Distribution of execution times for MonetDB and DuckDB')


    fig2, ax2 = plt.subplots()
    ax2.boxplot(monetdb_boxplot_avgs, vert=False)
    ax2.set_yticklabels(['MonetDB'])
    ax2.set_xlabel('Execution time (s)')
    ax2.set_title('Distribution of execution times for MonetDB')

    fig3, ax3 = plt.subplots()
    ax3.boxplot(duckdb_df['exec_time'], vert=False)
    ax3.set_yticklabels(['DuckDB'])
    ax3.set_xlabel('Execution time (s)')
    ax3.set_title('Distribution of execution times for DuckDB')

    plt.plot()
    plt.show(block=False)
    input('press <ENTER> to continue')

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input path to directory')
    parser.add_argument('--output', required=False, help='Output path to directory')
    args = parser.parse_args()
    compute_results(args)

if __name__ == "__main__":
    main()
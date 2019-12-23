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

    input_files_monetdb = ["/output_monetdb_standard_bm25_robertson_time.csv", "/output_monetdb_surkey_bm25_robertson_time.csv",
                    "/output_monetdb_indexed_bm25_robertson_time.csv", "/output_monetdb_surkey_indexed_bm25_robertson_time.csv"]

    input_files_duckdb = ["/output_duckdb_standard_bm25_robertson_time.csv", "/output_duckdb_surkey_bm25_robertson_time.csv"]

    avgs = {}
    for input_file in input_files_monetdb + input_files_duckdb: 
        df = pd.read_csv(input_folder + input_file, sep=" ", names=['id', 'exec_time'])
        avgs[input_file] = np.mean(df.exec_time)

    with open(output_folder + '/avg_execution_times.csv', 'w', newline='') as file: 
        writer = csv.writer(file, delimiter=",", 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for key, value in avgs.items(): 
            writer.writerow([key, value])

    # Plot MonetDB distributions
    fig1, ax1 = plt.subplots()
    plot_exec_times_distributions(input_files_monetdb, input_folder=input_folder, tick_labels=
                                                        ['MonetDB Standard', 'MonetDB w/ Surrogate Key', 
                                                        'MonetDB w/ Indexes', 'MonetDB w/ Indexes and Surrogate Keys'], 
                                                        title='Distribution of execution times for MonetDB', 
                                                        fig=fig1,
                                                        ax=ax1)

    fig2, ax2 = plt.subplots()
    plot_exec_times_distributions(input_files_duckdb, input_folder=input_folder, tick_labels=
                                                            ['DuckDB Standard', 'DuckDB w/ Surrogate Key'], 
                                                        title='Distribution of execution times for DuckDB', 
                                                        fig=fig2, 
                                                        ax=ax2)
    # fig1, ax1 = plt.subplots()
    # data = []
    # for input_file in input_files_monetdb:
        
    #     start_index = 0 
    #     end_index = 250
    #     df = pd.read_csv(input_folder + input_file, sep=" ", names=['id', 'exec_time'])
    #     avgs = []
    #     for i in range(250): 
    #         idx = [index for index in range(i, len(df.index), 250)]
    #         avgs.append(np.mean(df['exec_time'].iloc[idx]))

    #     data.append(avgs)

    # ax1.boxplot(data, vert=False)
    # ax1.set_yticklabels(['MonetDB Standard', 'MonetDB w/ Surrogate Key', 'MonetDB w/ Indexes', 'MonetDB w/ Indexes and Surrogate Keys'])
    # ax1.set_xlabel('Execution time (s)')
    # ax1.set_title('Distribution of execution times for MonetDB')

    # # Plot MonetDB averages
    # fig2, ax2 = plt.subplots()
    # data = []
    # for input_file in input_files_duckdb:
        
    #     start_index = 0 
    #     end_index = 250
    #     df = pd.read_csv(input_folder + input_file, sep=" ", names=['id', 'exec_time'])
    #     avgs = []
    #     for i in range(250): 
    #         idx = [index for index in range(i, len(df.index), 250)]
    #         avgs.append(np.mean(df['exec_time'].iloc[idx]))

    #     data.append(avgs)

    # ax2.boxplot(data, vert=False)
    # ax2.set_yticklabels(['DuckDB Standard', 'DuckDB w/ Surrogate Key'])
    # ax2.set_xlabel('Execution time (s)')
    # ax2.set_title('Distribution of execution times for DuckDB')

    plt.plot()
    plt.show(block=False)
    input('press <ENTER> to continue')

def plot_exec_times_distributions(input_files, input_folder, tick_labels, title, fig, ax):
    data = []
    
    for input_file in input_files:
        start_index = 0 
        end_index = 250
        df = pd.read_csv(input_folder + input_file, sep=" ", names=['id', 'exec_time'])
        avgs = []

        for i in range(250): 
            idx = [index for index in range(i, len(df.index), 250)]
            avgs.append(np.mean(df['exec_time'].iloc[idx]))

        data.append(avgs)

    ax.boxplot(data, vert=False)
    ax.set_yticklabels(tick_labels)
    ax.set_xlabel('Execution time (s)')
    ax.set_title(title)

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input path to directory')
    parser.add_argument('--output', required=False, help='Output path to directory')
    args = parser.parse_args()
    compute_results(args)

if __name__ == "__main__":
    main()
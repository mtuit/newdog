import pandas as pd
import argparse
import numpy as np
import csv

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
    
def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input path to directory')
    parser.add_argument('--output', required=False, help='Output path to directory')
    args = parser.parse_args()
    compute_results(args)

if __name__ == "__main__":
    main()
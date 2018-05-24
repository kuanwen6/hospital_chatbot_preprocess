import pandas as pd
import psycopg2
from sqlalchemy import create_engine

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='fliter_dr568410605emgcase.csv',
                        help='input file name')
    args = parser.parse_args()
  
    csv = pd.read_csv(args.input, lineterminator='\n')
    print(csv.head())
    print(csv.shape)

    #conn = psycopg2.connect(database="test_1", user="kuanwen", password="", host="127.0.0.1", port="5432")

    
    engine = create_engine('postgresql+psycopg2://kuanwen:@localhost:5432/test_1')
    #csv.to_sql('case', engine)
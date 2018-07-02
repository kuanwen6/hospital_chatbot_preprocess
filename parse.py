import pandas as pd

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='dr568410605emgcase.csv',
                        help='input file name')
    args = parser.parse_args()
  
    csv = pd.read_csv(args.input, encoding="latin1")
    print(csv.head())
    print(csv.shape)

    # if is error here, please check the encode type,  maybe re-store in notepad/vscode will help 
    csv['Kcom'] = csv['Kcom'].map(lambda x: str(x).encode("latin1").decode('big5'))
    csv['Cresult'] = csv['Cresult'].map(lambda x: str(x).encode("latin1").decode('big5'))


    print(csv.head())
    csv[['Pno', 'Caseno','Kcom','Bdate','Edate','Cresult']].to_csv('Kcom_'+args.input, index=False,encoding="utf_8_sig")

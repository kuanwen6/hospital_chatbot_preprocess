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

    #csv = csv[['Pno', 'Caseno','Bdate','Edate','Cresult','Cdis1','Cdis2','Cdis3','Cdis4','Cdis5','Kstatus','Woundchk9','Medchk1','Medchk2','Medchk3','Medchk4','Medchk5','Medchk6','Medchk7','Medchk8','Ke','Km','Kv','Kright','Kleft','Kt','Kp','Kr','Kbp1','Kbp2','Kpos','Kcom','Sex','Creason']]
    
    # if is error there, please check the encode type,  maybe re-store in notepad/vscode will help 
    #for i in ['Kcom','Kstatus','Woundchk9','Medchk8','Creason','Cresult']:\
        #csv[i] = csv[i].map(lambda x: str(x).encode("latin1").decode('big5'))
    csv['Kcom'] = csv['Kcom'].map(lambda x: str(x).encode("latin1").decode('big5'))


    print(csv.head())
    csv[['Pno', 'Caseno','Kcom']].to_csv('Kcom2_'+args.input, index=False,encoding="utf_8_sig")

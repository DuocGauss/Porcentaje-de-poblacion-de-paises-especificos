import csv

def read_csv(path):
    with open(path,'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        lista = []
        for row in reader:
            union = zip(header, row)
            country_dict = {key: value for key, value in union}
            lista.append(country_dict)
        return lista
            
if __name__ == '__main__':
    result = read_csv('./data.csv')
    print(result[0])
    

import read_csv, graficos

def run():
    
    data = read_csv.read_csv('./data.csv')
    
    data = list(filter(lambda x: x['Country/Territory'] in ['Chile', 'Argentina','Mexico','Peru','Brazil'] , data))
    
    paises = list(map(lambda x: x['Country/Territory'], data))
    porcentaje = list(map(lambda x: x['World Population Percentage'], data))
    
    '''
    country = input('Ingresa el nombre del país: ')
    result = mod.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
    labels, values = mod.ob_population(country)
    '''
    graficos.generar_grafico_pie(paises, porcentaje)
    
if __name__ == '__main__':
    run() 



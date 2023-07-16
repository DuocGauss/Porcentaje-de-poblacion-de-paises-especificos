import matplotlib.pyplot as plt


#def generar_grafico(labels, values):
    #plt.bar(labels, values)
    #plt.show()
    
def generar_grafico_pie(labels,valores):
    plt.pie(valores, labels= labels)
    plt.show()
    

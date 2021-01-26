# Devisive-Hierarchical-Clustering
Por ahora sólo aglomera con dataframes de 2 variables, pero sería relativamente fácil hacer que lo haga con n variables.

## Ejemplo de uso que divide en 2 clusters y grafica:

```py
my_data = pd.read_csv('/content/class-grades.csv')
my_data = my_data[['Midterm','Final']]
X = my_data
graficar_labels(X,cluster_divisivo(X,2))
```


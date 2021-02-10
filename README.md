# Devisive-Hierarchical-Clustering
Usa distancia euclideana y la distancia entre clusters es la promedio.     
Por ahora sólo aglomera con dataframes de 2 variables, pero sería relativamente fácil hacer que lo haga con n variables.

## Ejemplo de uso que divide en 3 clusters y grafica:

```py
import seaborn as sns

iris = sns.load_dataset('iris')
iris = iris[['sepal_length','sepal_width']]
graficar_labels(iris,cluster_divisivo(iris,3))
```
![](https://github.com/JavoJavo/Devisive-Hierarchical-Clustering/blob/main/iris_k3.png)



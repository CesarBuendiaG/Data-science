
"""
Pasos:
1 - Importar la data
2 - Limpiar los datos (evitar errores o duplicados, para que el modelo no se entrene mal)
3 - Divir la data entre entrenamieto /(para entrenar el modelo) y pruebas(para comprobar que funcione el modelo)
    se suele dividir 80% -20%
4 - Seleccionar un modelo (algoritmo a utilizar, depende netamente del problema a solucionar)
5 - Entrenar modelo(tomas los datos limpios y se los pasas al modelo)
6 - Pedir al modelo que haga predicciones (va a salir margen de error)
7 - Evaluar y mejorar (tal vez mas datos, otro modelo,  y saber que hacer para resolver el problema)
"""
"""
Herramientas librerias/bibliotecas

- numPy: Para arerglos en multiples dimesiones (listas dentro de listas)
- pandas: dataframe (arreglos de dos dimensiones (filas y columnas))
- matPlotlib: Para generar graficos en dos dimesiones (visualizar data)
- Scikit-learn: contiene algoritmos utiles a trabajar (como redes neurales, arbol de descicion, etc)
- TensorFlow: Especializado en redes neurales (a muy grande escala, mucha especializacion)

"""
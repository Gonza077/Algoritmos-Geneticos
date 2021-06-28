# Trabajo Práctico Nº2

## Enunciado

<h1 align="center">
  <img src="../assets/TP2.png" alt="Enunciado TP2">
</h1>

## Ejercicios

### Ejercicio 1: Resolver el problema de la mochila utilizando una busqueda exhaustiva

Como es una busqueda exhaustiva, primero se deben generar todas las soluciones.
Luego, se evaluaran todas para encontrar la mejor.

El problema contiene 10 elementos que pueden estar en la mochila o no, por lo que las soluciones van
desde la que no tiene ningun elemento hasta la que tienen todos (1024 soluciones).
Luego, habra que evaluarlas todas, descartar las que no cumplen con la restriccion de volumen y
encontrar la que tiene un mayor valor en las que si cumplen con las restriciones de volumen.

Ejemplo posibles soluciones:

 (Objeto 1, Objeto 2, ... , Objeto 10)

    0 0 0 0 0 0 0 0 0 0
    1 0 0 0 0 0 0 0 0 0
    1 1 0 0 0 0 0 0 0 0
    ...
    ...
    ...
    1 1 1 1 1 1 1 1 1 1
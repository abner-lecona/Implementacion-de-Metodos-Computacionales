﻿# Implementacion-de-Metodos-Computacionales

#Descripción de la Evidencia

Con tu equipo de trabajo:

Extiende el programa realizado en la █ Etapa 1 - Situación Problema 1: Resaltador de sintaxis para que aplique, de manera secuencial, el resaltado de léxico a múltiples archivos fuente contenidos en uno o varios directorios anidados.
Desarrolla una nueva versión de tu programa para que realice el proceso de resaltado de léxico de manera paralela con el fin de aprovechar los múltiples núcleos disponibles en los CPUs modernos.
Asegúrate de utilizar en tu código fuente las convenciones de codificación del lenguaje en el que está implementado tu programa.
Diseña experimentos para medir y comparar los desempeños de ambas versiones de tu solución (secuencial y paralela). Se recomienda realizar diversas pruebas con diferentes configuraciones (threads vs procesos, número de trabajadores, número de archivos de entrada, etc.) Calcula el speed-up obtenido usando la siguiente fórmula:
  

En donde:

 es el número de procesadores (o núcleos).
 es el tiempo que tarda en ejecutarse la versión secuencial del programa.
 es el tiempo que tarda en ejecutarse la versión paralela del programa utilizando 
 procesadores.
 es el speed-up obtenido usando  procesadores.

Analiza los experimentos realizados y emite una conclusión sobre los mejores resultados obtenidos. ¿Bajo qué condiciones se recomedaría el uso de una u otra implementación?
Plasma en un reporte los resultados de tus pruebas y conclusiones de los puntos 4 y 5. 
Crea un video breve (5 minutos) demostrando el correcto funcionamiento de tu solución. Asegúrate de demostrar los siguientes puntos:
Ejecución secuencial
Ejecución paralela
Generación y contenido de archivos "resaltados" (incluyendo identificación de errores sintácticos)

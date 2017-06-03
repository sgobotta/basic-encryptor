## Universidad Nacional de Quilmes - Seguridad Informática - 2017

### Laboratorio de Seguridad Informática: Encriptación

### Alumno: Botta Santiago

#### Necesidad:
Se necesita encriptar un archivo de texto dado utilizando el algoritmo AES256. De la misma manera se necesita poder desencriptarlo utilizando una clave.

#### Problemas y Motivación
Se ha realizado una breve investigación sobre los requisitos básicos que cualquier implementación de un AES256 debería tener y se recopilaron los siguientes requerimientos, en particular para el modo CBC:

	Un programa de encriptación debería:
		- definir un tamaño de bloque para la extracción del vector de inicialización
		- aceptar una clave

		- encriptación:
			- debe realizar un relleno (padding) al texto plano que llega externamente
			- debe generar un vector de inicialización teniendo en cuenta el tamaño del bloque del modo utilizado
			- debe retornar el vector de inicialización junto con el contenido ya encriptado 

		- desencriptación:
			- debe reconocer y extraer los caracteres que representan el vector de inicialización utilizado
			- debe utilizar la misma clave y vector de inicialización al desencriptar el contenido
			- debe retornar el contenido desencriptado sin el relleno (padding) dado durante la encriptación


#### Solución propuesta:
Realizar un programa que que a partir de un archivo de texto y una clave sea capaz de devolver otro archivo con el contenido encriptado. El archivo original no será eliminado. También podrá tomar un archivo encriptado en un formato específico y utilizando la misma clave con la que se encriptó, se obtendrá el archivo original en un formato de texto.

#### Tecnologías utilizadas:

Lenguaje: Python3

Librerías: Crypto

#### Alcance:
El programa acepta archivos en formato .txt y .cyrpt
Consta de dos comandos principales encrypt, decrypt.
Acepta claves con números y/o letras
Se ha utilizado el programa con archivos de texto de hasta 5400 caracteres

#### Requisitos:
python3

#### Modo de uso:

```
python3 encryptor.py help
```

Encriptar:
```
	python3 encryptor.py encrypt <archivo.txt>
```
	
Desencriptar:
```
	python3 encryptor.py decrypt <archivo.crypt>
```

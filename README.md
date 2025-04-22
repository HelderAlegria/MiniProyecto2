¿Cómo funciona?
Primero, utilizo Python con las librerías OpenCV y MediaPipe para procesar la imagen de la cámara en tiempo real. El sistema detecta la mano y cuenta los dedos levantados. Cada vez que el número de dedos cambia, envío ese número al Arduino a través del puerto serial (USB).
En el Arduino, tengo un código que recibe ese número y enciende los segmentos correspondientes del display de 7 segmentos para mostrar el número. El display que estoy utilizando es de 7 segmentos de ánodo común (modelo 5161BS).

Materiales que usé:
Display de 7 segmentos modelo 5161BS (ánodo común)

* Arduino Uno
* Protoboard y cables jumper
* Computadora con cámara
* Python con MediaPipe y OpenCV
* Conexión USB entre Python y Arduino

¿Qué sucede cuando lo uso?
Cuando levanto entre 0 y 5 dedos frente a la cámara, el sistema detecta el número de dedos y lo muestra en el display de 7 segmentos. Esto se logra mediante la comunicación entre Python y Arduino.


LINK DEL VIDEO:
https://drive.google.com/file/d/1iEokrX3J-CvwvK7LTUwtI-Wr9r10Jeg-/view?usp=sharing

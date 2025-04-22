int segmentos[] = {2, 3, 4, 5, 6, 7, 8}; 

byte digitos[6][7] = {
  {0,0,0,0,0,0,1}, // 0
  {1,0,0,1,1,1,1}, // 1
  {0,0,1,0,0,1,0}, // 2
  {0,0,0,0,1,1,0}, // 3
  {1,0,0,1,1,0,0}, // 4
  {0,1,0,0,1,0,0}, // 5
};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    int numero = c - '0';
    if (numero >= 0 && numero <= 5) {
      for (int i = 0; i < 7; i++) {
        digitalWrite(segmentos[i], digitos[numero][i]);
      }
    }
  }
}

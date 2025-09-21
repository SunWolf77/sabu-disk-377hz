// Teensy/Arduino MEMS mic logger
// Captures amplitude/phase at hub & rim

const int micPins[] = {A0, A1, A2, A3};
const int numMics = 4;

void setup() {
  Serial.begin(115200);
}

void loop() {
  for (int i = 0; i < numMics; i++) {
    int val = analogRead(micPins[i]);
    Serial.print(val);
    if (i < numMics - 1) Serial.print(",");
  }
  Serial.println();
  delay(10);
}
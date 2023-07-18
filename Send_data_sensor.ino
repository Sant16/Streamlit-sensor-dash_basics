#include <DHT.h>
#define DHTTYPE DHT22
const int DHTPin = 6;
DHT dht(DHTPin, DHTTYPE);


void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}
void loop() {
  delay(90);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println("No se pudo leer el sensor DHT!");
    return;
  }
  Serial.print(h);
  Serial.print("|");
  Serial.print(t);
  Serial.print("\n"); 
}

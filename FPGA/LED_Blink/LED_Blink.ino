void setup () {
  pinMode (0, OUTPUT);
  Serial.begin (9600);
}

void loop () {
  digitalWrite (0, HIGH);
  delay (100);
  digitalWrite (0, LOW);
  delay (100);
  
  Serial.println ("AAA");
}

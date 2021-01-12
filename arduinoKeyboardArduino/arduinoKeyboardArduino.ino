int input = 2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(input, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(input) == LOW)
  {
    Serial.println("on");
  }
  else
  {
    Serial.println("off");
  }
}

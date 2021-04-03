int inputTypes = 12;
int input[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, A0};
bool pressedKey[] = {false, false, false, false, false, false, false, false, false, false, false, false};
int led = 13;
bool ledState;

void setup() 
{
  Serial.begin(9600);
  /*
  for(int i = 0; i < inputTypes; i++)
  {
    pinMode(input[i], INPUT_PULLUP);
  }*/
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(A0, INPUT_PULLUP);
  
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  ledState = true;
}

void loop() 
{
  // Checking if button is pressed
  
  if(digitalRead(input[0]) == LOW)
  {
    if(!pressedKey[0])
    {
      Serial.println("key20");
      pressedKey[0] = true;
    }
  }
  else 
  {
    pressedKey[0] = false;
  }
  
  if(digitalRead(input[1]) == LOW)
  {
    if(!pressedKey[1])
    {
      Serial.println("key21");
      pressedKey[1] = true;
    }
  }
  else 
  {
    pressedKey[1] = false;
  }
  
  if(digitalRead(input[2]) == LOW)
  {
    if(!pressedKey[2])
    {
      Serial.println("key22");
      pressedKey[2] = true;
    }
  }
  else 
  {
    pressedKey[2] = false;
  }
  
  if(digitalRead(input[3]) == LOW)
  {
    if(!pressedKey[3])
    {
      Serial.println("key13");
      pressedKey[3] = true;
    }
  }
  else 
  {
    pressedKey[3] = false;
  }
  
  if(digitalRead(input[4]) == LOW)
  {
    if(!pressedKey[4])
    {
      Serial.println("key12");
      pressedKey[4] = true;
    }
  }
  else 
  {
    pressedKey[4] = false;
  }
  
  if(digitalRead(input[5]) == LOW)
  {
    if(!pressedKey[5])
    {
      Serial.println("key11");
      pressedKey[5] = true;
    }
  }
  else 
  {
    pressedKey[5] = false;
  }
  
  if(digitalRead(input[6]) == LOW)
  {
    if(!pressedKey[6])
    {
      Serial.println("key10");
      pressedKey[6] = true;
    }
  }
  else 
  {
    pressedKey[6] = false;
  }
  
  if(digitalRead(input[7]) == LOW)
  {
    if(!pressedKey[7])
    {
      Serial.println("key01");
      pressedKey[7] = true;
    }
  }
  else 
  {
    pressedKey[7] = false;
  }
  
  if(digitalRead(input[8]) == LOW)
  {
    if(!pressedKey[8])
    {
      Serial.println("key02");
      pressedKey[8] = true;
    }
  }
  else 
  {
    pressedKey[8] = false;
  }
  
  if(digitalRead(input[9]) == LOW)
  {
    if(!pressedKey[9])
    {
      Serial.println("key03");
      pressedKey[9] = true;
    }
  }
  else 
  {
    pressedKey[9] = false;
  }
  
  if(digitalRead(input[10]) == LOW)
  {
    // Used repeating code because if's don't nest further than two layers.
    if(!pressedKey[10] && ledState)
    {
      Serial.println("key00");
      pressedKey[10] = true;
      digitalWrite(led, LOW);
      ledState = false;
    }
    else if(!pressedKey[10] && !ledState)
    {
      Serial.println("key00");
      pressedKey[10] = true;
      digitalWrite(led, HIGH);
      ledState = true;
    }
  }
  else 
  {
    pressedKey[10] = false;
  }
  
  if(digitalRead(input[11]) == LOW)
  {
    if(!pressedKey[11])
    {
      Serial.println("key23");
      pressedKey[11] = true;
    }
  }
  else 
  {
    pressedKey[11] = false;
  }
}

void handleLed()
{
  
}

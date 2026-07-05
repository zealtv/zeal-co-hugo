# Wailers

solar panel -> dc motor -> dc motor -> speaker

use dc motor as generator to produce AC signal to drive speaker

alternatively an encoder can do this.... https://www.instructables.com/Motor-Sound-generator/
![[Pasted image 20251225203747.png]]
print the encoder!

... could spin this with a motor


# [[vane - musical weather station]]



# Sun Bugs

## Solar Striker
![[solar striker]]


## piezo blippers and blippers

![[sun bug v2]]
- instruments that require no external power, instead drawing from light, wind, heat, motion
- play as an ensemble
- Richness of composition comes from shifts in power availability
- Each instrument needs to do not much





![[sun bug]]



# Sunbugs - consider a pic microcontroller
https://youtube.com/shorts/Mrvp41q170s?si=6bskaiFpjQKoHSzQ

# Sunbugs ATTiny Code

``` C++
// UNDERTONES

#define BUZZER1PIN 0
#define POT1PIN 1
#define BUZZER2PIN 3
#define POT2PIN 2
//uint_16_t clock;
int clock1 = 0;
bool tone1 = false;
int clock2 = 0;
bool tone2 = false;


//| arduino |   tiny      |    pin |
//|---------|-------------|--------|
//|    4    |  RESET      |   1    | // an-in turns ATTiny of below 50% of VCC
//|    3    |             |   2    | // d-out / an-in
//|    2    |             |   3    | // d-out / an-in
//|         |  (-)        |   4    |
//|    0    |             |   5    | // d-out
//|    1    |             |   7    | // an-in* 
//|         |  (+)        |   8    |

//* disconnect pin 7 when programming


void setup() {
  pinMode(BUZZER1PIN, OUTPUT);
  pinMode(BUZZER2PIN, OUTPUT);
  pinMode(POT1PIN, INPUT);
  pinMode(POT2PIN, INPUT);
}



void loop() {
  // analog in read as 0 - 1024
  float position1 = map(analogRead(POT1PIN), 0, 1024, 2, 20);
  float position2 = map(analogRead(POT2PIN), 0, 1024, 2, 20);
  
  if(clock1 >= position1){
    tone1 = !tone1;
    clock1 = 0;
  }

  if(clock2 >= position2){
    tone2 = !tone2;
    clock2 = 0;
  }


  digitalWrite(BUZZER1PIN, tone1);
  digitalWrite(BUZZER2PIN, tone2);

  // digitalWrite(BUZZER1PIN, HIGH);
  // digitalWrite(BUZZER2PIN, HIGH);
  // delay(position);

  // digitalWrite(BUZZER1PIN, LOW);
  // digitalWrite(BUZZER2PIN, LOW);
  
  
  delay(1);
  clock1++;
  clock2++;

}
```

```
  
  
  

void setup() {

pinMode(0, OUTPUT); // BUZZER ATTiny PB0 / pin 5

pinMode(3, INPUT); // In 1 ATTiny PB3 / pin 2

pinMode(4, INPUT); // In 2 ATTiny PB4 / pin 3

}

  

void loop() {

int position = analogRead(3) < analogRead(4);

  
  

digitalWrite(0, HIGH);

if(position > 0){

delay(2);

}

else{

delay(4);

}

  

digitalWrite(0, LOW);

  

if(position > 0){

delay(2);

}

else{

delay(4);

} // wait for a second

}
```

# Simple Oscillator Circuits
![# Beginner Electronics Project: Simple Oscillator with 555 Timer and Speaker in Astable Mode EVLOG #7](https://www.youtube.com/watch?v=ADifSQv3nY8)

![# Oskitone POLY555 - 3D Printed 555 Timer Analog Synth!](https://www.youtube.com/watch?v=YcFjmL8s72Y)

![ Casper Electronics DIY synth building. Part 1: Oscillators ](https://www.youtube.com/watch?v=FaoJaLmZaL4)

# Harvesting power from piezos?
![](https://www.youtube.com/shorts/GwnAhHjQAKw)

# Components
42 ohms Passive Buzzer AC 12MMx8.5MM 12085 42R Resistance
TSSERND

# Setting up an ATTiny13 
https://www.instructables.com/Updated-Guide-on-How-to-Program-an-Attiny13-or-13a/

![[Pasted image 20250529152615.png]]


# piezo chorus - sun singers
![[piezo chorus]]

# Playing a tone on the ATtiny85
http://www.technoblogy.com/show?20MO

```
const int Output = 1;                                   // Can be 1 or 4

// Cater for 16MHz, 8MHz, or 1MHz clock:
const int Clock = ((F_CPU/1000000UL) == 16) ? 4 : ((F_CPU/1000000UL) == 8) ? 3 : 0;
const uint8_t scale[] PROGMEM = {239,226,213,201,190,179,169,160,151,142,134,127};

void note (int n, int octave) {
  int prescaler = 8 + Clock - (octave + n/12);
  if (prescaler<1 || prescaler>15 || octave==0) prescaler = 0;
  DDRB = (DDRB & ~(1<<Output)) | (prescaler != 0)<<Output;
  OCR1C = pgm_read_byte(&scale[n % 12]) - 1;
  GTCCR = (Output == 4)<<COM1B0;
  TCCR1 = 1<<CTC1 | (Output == 1)<<COM1A0 | prescaler<<CS10;
}

void loop() {
  for (int n=0; n<=12; n++) {
    note(n, 4);
    if (n!=4 && n!=11) n++;
    delay(500);
  }
  note(0, 0);
  delay(10000);
}
```

Earlier version... http://www.technoblogy.com/show?KVO
```
/* TinyTone for ATtiny85 */

// Notes
const int Note_C  = 239;
const int Note_CS = 225;
const int Note_D  = 213;
const int Note_DS = 201;
const int Note_E  = 190;
const int Note_F  = 179;
const int Note_FS = 169;
const int Note_G  = 159;
const int Note_GS = 150;
const int Note_A  = 142;
const int Note_AS = 134;
const int Note_B  = 127;

int Speaker = 1;

void setup()
{
  pinMode(Speaker, OUTPUT);
}

void loop()
{
  playTune();
  delay(10000);
}

void TinyTone(unsigned char divisor, unsigned char octave, unsigned long duration)
{
  TCCR1 = 0x90 | (8-octave); // for 1MHz clock
  // TCCR1 = 0x90 | (11-octave); // for 8MHz clock
  OCR1C = divisor-1;         // set the OCR
  delay(duration);
  TCCR1 = 0x90;              // stop the counter
}

// Play a scale
void playTune(void)
{
 TinyTone(Note_C, 4, 500);
 TinyTone(Note_D, 4, 500);
 TinyTone(Note_E, 4, 500);
 TinyTone(Note_F, 4, 500);
 TinyTone(Note_G, 4, 500);
 TinyTone(Note_A, 4, 500);
 TinyTone(Note_B, 4, 500);
 TinyTone(Note_C, 5, 500);
}
```


Or MIDI to Arduino:
https://www.instructables.com/Musical-Card-ATtiny85/
# PUSH PULL CIRCUIT
https://electronics.stackexchange.com/questions/299998/how-to-make-a-piezoelectric-transducer-buzz-louder 

![[Pasted image 20250603170727.png]]

# Speaker Enclosure
![[Pasted image 20250603170806.png]]

![[Pasted image 20250603170820.png]]



# [[The Miller Solar Engine]]


# Mendocino Motor
![](https://www.youtube.com/watch?v=sB5hf5N5akg)

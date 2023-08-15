#define NUM_LEDS 78
#define LED_PIN 13
#define LIMIT 1000
#define POT_PIN 4
#define BUT_PIN 6


#include "FastLED.h"

struct CRGB leds[NUM_LEDS];

unsigned short int LED_COUNT = NUM_LEDS;

int ihue = 0;
unsigned short int fade_delay = 150;
String alph_l = "0123456789abcdef";
byte alph_n[16] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
byte pix_num;
byte brightness = 100;

byte idex;




void one_color_all(int cred, int cgrn, int cblu) {       //-SET ALL LEDS TO ONE COLOR
  for (int i = 0 ; i < LED_COUNT; i++ ) {
    leds[i].setRGB( cred, cgrn, cblu);
  }
  LEDS.show();
  //one_color_all(255, 255, 255);
}

void rainbow_fade() {                         //-m2-FADE ALL LEDS THROUGH HSV RAINBOW
  ihue++;
  if (ihue > 255) {
    ihue = 0;
  }
  for (int idex = 0 ; idex < NUM_LEDS; idex++ ) {
    leds[idex] = CHSV(ihue, 255, 255);

  }
  LEDS.show();
  delay(fade_delay);
}



void better()
{
  ihue -= 1;
  fill_rainbow( leds, LED_COUNT, ihue );
  LEDS.show();
  delay(fade_delay);
}

void rainbow_self()
{

  for (int idex = 0 ; idex < NUM_LEDS; idex++ ) {
    leds[idex] = CHSV(ihue, 255, 255);

    ihue++;
    if (ihue > 255) {
      ihue = 0;
    }
  }

  LEDS.show();
  delay(10);
}


void rainbow_loop() {                        //-m3-LOOP HSV RAINBOW

  ihue = ihue + 10;
  if (idex >= LED_COUNT) {
    idex = 0;
  }
  if (ihue > 255) {
    ihue = 0;
  }
  leds[idex] = CHSV(ihue, 255, 255);
  LEDS.show();
  idex++;
  delay(fade_delay);
}

void pulse_one_color_all_rev() {           //-m11-PULSE SATURATION ON ALL LEDS TO ONE COLOR
  byte isat;

  bool bouncedirection = 0;
  if (bouncedirection == 0) {
    isat++;
    if (isat >= 255) {
      bouncedirection = 1;
    }
  }
  if (bouncedirection == 1) {
    isat = isat - 1;
    if (isat <= 1) {
      bouncedirection = 0;
    }
  }
  for (int idex = 0 ; idex < LED_COUNT; idex++ ) {
    leds[idex] = CHSV(255, isat, 255);
  }
  LEDS.show();
}



void setup() {
  // put your setup code here, to run once:



  LEDS.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);  // настройки для нашей ленты (ленты на WS2811, WS2812, WS2812B)
  one_color_all(0, 0, 0);
  LEDS.setBrightness(brightness);
  pinMode(POT_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUT_PIN, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  //rainbow_fade();
  better();
  //rainbow_loop();
  //pulse_one_color_all_rev();
  //rainbow_self();
}

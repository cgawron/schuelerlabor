/*
ursprüngliches Programm: Standalone Arduino StopWatch
By Conor M - 11/05/15, Modified by Elac - 12/05/15
*/

// call the necessary libraries
#include <SPI.h>
#include <LiquidCrystal.h>
// these are the pins used on the shield for this sketch
LiquidCrystal lcd(8, 13, 9, 4, 5, 6, 7);
// variables used on more than 1 function need to be declared here
unsigned long start, finished, elapsed;
boolean r = false;
// Variables for button debounce time
long lastButtonPressTime = 0; // the last time the button was pressed
long debounceDelay = 50; // the debounce time; keep this as low as possible

void setup()
{
lcd.begin(16, 2); // initialize the lcd (16 chars, 2 lines)

// a little introduction :)
lcd.setCursor(0, 0); // set the cursor to first character on line 1 
lcd.print("Selbstbauprojekt");
lcd.setCursor(0, 1); // set the cursor to first character on line 2
lcd.print("2017 - DARC G01");
delay(4000); // wait 4 seconds
lcd.clear(); // clear the display
lcd.print("Stoppuhr            ");
delay (3000);
lcd.clear(); 
lcd.print("Druecke SELECT");
lcd.setCursor(0, 1); // set the cursor to first character on line 2
lcd.print("fuer Start/Stopp");
}

void loop()
{
CheckStartStop();
DisplayResult();
}

void CheckStartStop()
{
int x = analogRead (0); // assign 'x' to the Arduino's AnalogueInputs (Shield's buttons)
if (x < 800 && x > 600 ) // if the button is SELECT
{
if ((millis() - lastButtonPressTime) > debounceDelay)
{

if (r == false)
{
lcd.clear();
lcd.setCursor(0, 0); // needed
lcd.print("Zeit laeuft");
start = millis(); // saves start time to calculate the elapsed time
}
else if (r == true)
{
lcd.setCursor(0, 0); // needed
lcd.print("Stopp                ");
}
r = !r;
}
lastButtonPressTime = millis();
}
}

void DisplayResult()
{
if (r == true)
{
finished = millis(); // saves stop time to calculate the elapsed time
// declare variables
float h, m, s, ms;
unsigned long over;

// MATH time!!!
elapsed = finished - start;

h = int(elapsed / 3600000);
over = elapsed % 3600000;
m = int(over / 60000);
over = over % 60000;
s = int(over / 1000);
ms = over % 1000;
// display the results
lcd.setCursor(0, 1);
lcd.print(h, 0); // display variable 'h' - the 0 after it is the number of algorithms after a comma (ex: lcd.print(h, 2); would print 0,00
lcd.print("h "); // and the letter 'h' after it
lcd.print(m, 0);
lcd.print("m ");
lcd.print(s, 0);
lcd.print("s ");
if (h < 10)
{
lcd.print(ms, 0);
lcd.print("ms ");
}
}
}

# Arduino Smart Cane

An open-source, affordable assistive technology project that enables obstacle detection for visually impaired individuals. This device enhances a standard white cane by adding ultrasonic obstacle detection with vibration feedback, helping to identify obstacles beyond the range of traditional canes, this project aims to reduce the price of smart canes, such as the WeWalk Smart Cane 2, which can price up to $1000 USD.

This project creates a smart cane using an Arduino Uno that uses an HC-SR04 ultrasonic sensor to detect obstacles and provides vibration feedback. The device functions as follows:

* **Ultrasonic Sensor**: Detects obstacles up to 4 meters away
* **Feedback Actions**:
  * No obstacle detected → No vibration
  * Obstacle within threshold (30cm) → Vibration activated
  * Button pressed → Temporarily disable detection

## Features

* Low-cost alternative to commercial smart cane devices
* Customizable detection threshold
* Arduino Uno implementation
* Open-source hardware and software
* Modular design for easy customization

## Hardware Requirements

### Essential Components

1. **Arduino Uno** (~$25 USD)
   * Core controller for the project

2. **HC-SR04 Ultrasonic Sensor** (~$2-6 USD)
   * Detects obstacles up to 4m away
   * Accuracy of ±0.3cm

3. **Vibration Motor** (~$2-8 USD)
   * Provides tactile feedback when obstacles are detected
   * Small coin type recommended for easy mounting

4. **Push Button** (~$1-3 USD)
   * For temporarily disabling detection
   * Useful when talking to someone standing close

5. **Additional Components**:
   * Breadboard for prototyping (~$5 USD)
   * Jumper wires (~$3-5 USD)
   * 9V Battery with holder and ON/OFF switch (~$3-5 USD)
   * LED Indicator (optional) (~$0.50-1 USD)
   * Mounting materials (~$3-5 USD)

**Estimated Total Cost:** Approximately $11.50-24 USD (excluding Arduino Uno)

### Tools Needed

* Soldering iron and solder (optional for final assembly)
* Wire cutters/strippers
* Hot glue gun
* Small screwdriver set
* Scissors

## Circuit Connections

### Basic Circuit Connections

1. **HC-SR04 Ultrasonic Sensor Connections**:
   * VCC pin → Arduino 5V
   * GND pin → Arduino GND
   * Trig pin → Arduino D2
   * Echo pin → Arduino D3

2. **Vibration Motor Connections**:
   * Positive (+) lead → Arduino D4 (through transistor)
   * Negative (-) lead → Arduino GND
   * Note: Use a 2N2222 transistor and 1N4001 diode for protection

3. **Push Button Connections**:
   * One terminal → Arduino D5
   * Other terminal → Arduino GND
   * Note: Uses Arduino's internal pull-up resistor

4. **Power Supply**:
   * 9V Battery positive → Arduino Vin
   * 9V Battery negative → Arduino GND

## Software

### Arduino Code

```cpp
/*
 * Smart Cane - Obstacle Detection System
 * 
 * This Arduino sketch implements an obstacle detection system for a smart cane
 * using an HC-SR04 ultrasonic sensor and a vibration motor for feedback.
 * 
 * Components:
 * - Arduino Uno
 * - HC-SR04 Ultrasonic Sensor
 * - Vibration Motor
 * - Push Button (for temporarily disabling detection)
 * - 9V Battery (for power)
 * 
 * Created for Arduino beginners
 */

// Pin Definitions
const int trigPin = 2;      // HC-SR04 Trigger pin connected to Arduino D2
const int echoPin = 3;      // HC-SR04 Echo pin connected to Arduino D3
const int motorPin = 4;     // Vibration motor connected to Arduino D4
const int buttonPin = 5;    // Push button connected to Arduino D5

// Constants
const int detectionThreshold = 30;  // Distance threshold in centimeters (adjust as needed)
const int buttonDebounceTime = 50;  // Debounce time for button in milliseconds

// Variables
long duration;              // Time taken for ultrasonic pulse to return
int distance;               // Calculated distance to obstacle
boolean detectionEnabled = true;    // Flag to enable/disable detection
boolean buttonPressed = false;      // Flag to track button state
unsigned long lastButtonPress = 0;  // Time of last button press for debouncing

void setup() {
  // Initialize Serial communication for debugging
  Serial.begin(9600);
  Serial.println("Smart Cane - Obstacle Detection System");
  
  // Configure pin modes
  pinMode(trigPin, OUTPUT);   // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);    // Sets the echoPin as an Input
  pinMode(motorPin, OUTPUT);  // Sets the motorPin as an Output
  pinMode(buttonPin, INPUT_PULLUP); // Sets the buttonPin as an Input with internal pull-up resistor
  
  // Initialize all outputs to LOW
  digitalWrite(trigPin, LOW);
  digitalWrite(motorPin, LOW);
  
  // Wait for system to stabilize
  delay(1000);
  
  Serial.println("System initialized and ready!");
}

void loop() {
  // Check button state for enabling/disabling detection
  checkButton();
  
  // Measure distance to obstacle
  measureDistance();
  
  // Print distance to Serial Monitor for debugging
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Activate vibration motor if obstacle is detected and detection is enabled
  if (detectionEnabled && distance <= detectionThreshold && distance > 0) {
    // Obstacle detected within threshold - activate motor
    digitalWrite(motorPin, HIGH);
    Serial.println("OBSTACLE DETECTED! Motor activated.");
  } else {
    // No obstacle detected or detection disabled - deactivate motor
    digitalWrite(motorPin, LOW);
  }
  
  // Small delay before next reading
  delay(100);
}

/*
 * Function: measureDistance
 * Description: Measures the distance to an obstacle using the HC-SR04 ultrasonic sensor
 * Returns: Updates the global 'distance' variable with the measured distance in centimeters
 */
void measureDistance() {
  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Set the trigPin HIGH for 10 microseconds to send ultrasonic pulse
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the echoPin to get the time it takes for the pulse to return
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance in centimeters
  // Speed of sound is 343 meters/second = 0.0343 cm/microsecond
  // Distance = (Time × Speed) / 2 (divide by 2 because sound travels to object and back)
  distance = duration * 0.0343 / 2;
}

/*
 * Function: checkButton
 * Description: Checks if the button is pressed and toggles detection mode
 * Returns: Updates the global 'detectionEnabled' variable
 */
void checkButton() {
  // Read the button state (LOW when pressed due to INPUT_PULLUP)
  boolean currentButtonState = digitalRead(buttonPin);
  
  // Check if button is pressed (LOW) and was not pressed before
  if (currentButtonState == LOW && !buttonPressed) {
    // Debounce the button
    if (millis() - lastButtonPress > buttonDebounceTime) {
      // Toggle detection state
      detectionEnabled = !detectionEnabled;
      
      // Print status message
      if (detectionEnabled) {
        Serial.println("Detection ENABLED");
      } else {
        Serial.println("Detection DISABLED");
      }
      
      // Update button state and time
      buttonPressed = true;
      lastButtonPress = millis();
    }
  } 
  // Button is released
  else if (currentButtonState == HIGH && buttonPressed) {
    buttonPressed = false;
  }
}
```

## Getting Started

1. Gather all the components listed in the Hardware Requirements section
2. Connect the components according to the Circuit Connections section
3. Upload the Arduino code to your Arduino Uno
4. Test the system by moving your hand in front of the ultrasonic sensor
5. Mount the system to a standard white cane
6. Adjust the detection threshold in the code if needed

## Future Enhancements

* Multiple sensors for wider detection coverage
* Variable feedback based on distance
* Audio feedback options
* Power optimization for extended battery life
* Smartphone integration for configuration

## Acknowledgments

This project was inspired by research on existing smart cane technologies, particularly the WeWalk Smart Cane and various Arduino-based DIY implementations.

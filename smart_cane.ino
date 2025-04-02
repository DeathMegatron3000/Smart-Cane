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

/*
 * Advanced Features (Uncomment to use):
 * 
 * 1. Variable vibration intensity based on distance:
 *    Instead of simple ON/OFF for the motor, you can use PWM to vary
 *    the intensity of vibration based on how close the obstacle is.
 *    
 *    Replace the motor activation code with:
 *    
 *    if (detectionEnabled && distance <= detectionThreshold && distance > 0) {
 *      // Calculate intensity (closer = stronger vibration)
 *      int intensity = map(distance, 0, detectionThreshold, 255, 50);
 *      analogWrite(motorPin, intensity);
 *    } else {
 *      analogWrite(motorPin, 0);
 *    }
 *    
 * 2. Double-press detection for permanent disable/enable:
 *    This would require tracking the timing between button presses
 *    and implementing a state machine for detection modes.
 */

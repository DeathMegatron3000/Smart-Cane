import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Set title and labels
ax.set_title('Smart Cane - Arduino Circuit Diagram', fontsize=16)
ax.text(0.5, 0.02, 'Created for Arduino Uno - Beginner Friendly', 
        horizontalalignment='center', fontsize=10, transform=ax.transAxes)

# Turn off axis
ax.axis('off')

# Define components
# Arduino Uno
arduino_x, arduino_y = 3, 3
arduino_width, arduino_height = 4, 2.5
arduino = patches.Rectangle((arduino_x, arduino_y), arduino_width, arduino_height, 
                           fill=True, color='#429ef5', alpha=0.7)
ax.add_patch(arduino)
ax.text(arduino_x + arduino_width/2, arduino_y + arduino_height/2, 'Arduino Uno', 
        horizontalalignment='center', verticalalignment='center', fontsize=12)

# Arduino pins
pin_labels = ['5V', 'GND', 'D2', 'D3', 'D4', 'D5']
pin_positions = [(arduino_x, arduino_y + arduino_height - 0.3 - i*0.4) for i in range(len(pin_labels))]

for i, (x, y) in enumerate(pin_positions):
    ax.plot(x, y, 'ko', markersize=5)
    ax.text(x - 0.3, y, pin_labels[i], horizontalalignment='right', verticalalignment='center', fontsize=8)

# HC-SR04 Ultrasonic Sensor
sensor_x, sensor_y = 9, 6
sensor_width, sensor_height = 2, 1
sensor = patches.Rectangle((sensor_x, sensor_y), sensor_width, sensor_height, 
                          fill=True, color='#66c56c', alpha=0.7)
ax.add_patch(sensor)
ax.text(sensor_x + sensor_width/2, sensor_y + sensor_height/2, 'HC-SR04', 
        horizontalalignment='center', verticalalignment='center', fontsize=10)

# Sensor pins
sensor_pin_labels = ['VCC', 'Trig', 'Echo', 'GND']
sensor_pin_positions = [(sensor_x + 0.2 + i*0.5, sensor_y) for i in range(len(sensor_pin_labels))]

for i, (x, y) in enumerate(sensor_pin_positions):
    ax.plot(x, y, 'ko', markersize=4)
    ax.text(x, y - 0.2, sensor_pin_labels[i], horizontalalignment='center', verticalalignment='top', fontsize=7, rotation=90)

# Vibration Motor
motor_x, motor_y = 9, 3
motor_width, motor_height = 1.5, 1
motor = patches.Ellipse((motor_x + motor_width/2, motor_y + motor_height/2), motor_width, motor_height, 
                       fill=True, color='#f54263', alpha=0.7)
ax.add_patch(motor)
ax.text(motor_x + motor_width/2, motor_y + motor_height/2, 'Vibration\nMotor', 
        horizontalalignment='center', verticalalignment='center', fontsize=8)

# Motor pins
motor_pin_positions = [(motor_x + 0.3, motor_y), (motor_x + motor_width - 0.3, motor_y)]
motor_pin_labels = ['+', '-']

for i, (x, y) in enumerate(motor_pin_positions):
    ax.plot(x, y, 'ko', markersize=4)
    ax.text(x, y - 0.2, motor_pin_labels[i], horizontalalignment='center', verticalalignment='top', fontsize=8)

# Push Button
button_x, button_y = 9, 1.5
button_width, button_height = 1, 0.8
button = patches.Rectangle((button_x, button_y), button_width, button_height, 
                          fill=True, color='#f5d742', alpha=0.7)
ax.add_patch(button)
ax.text(button_x + button_width/2, button_y + button_height/2, 'Button', 
        horizontalalignment='center', verticalalignment='center', fontsize=8)

# Button pins
button_pin_positions = [(button_x, button_y + button_height/2), (button_x + button_width, button_y + button_height/2)]

for x, y in button_pin_positions:
    ax.plot(x, y, 'ko', markersize=4)

# Battery
battery_x, battery_y = 1, 1
battery_width, battery_height = 1.5, 0.8
battery = patches.Rectangle((battery_x, battery_y), battery_width, battery_height, 
                           fill=True, color='#a3a3a3', alpha=0.7)
ax.add_patch(battery)
ax.text(battery_x + battery_width/2, battery_y + battery_height/2, '9V Battery', 
        horizontalalignment='center', verticalalignment='center', fontsize=8)

# Battery pins
battery_pin_positions = [(battery_x + battery_width, battery_y + 0.2), (battery_x + battery_width, battery_y + 0.6)]
battery_pin_labels = ['-', '+']

for i, (x, y) in enumerate(battery_pin_positions):
    ax.plot(x, y, 'ko', markersize=4)
    ax.text(x + 0.2, y, battery_pin_labels[i], horizontalalignment='left', verticalalignment='center', fontsize=8)

# Draw connections
# VCC connections (5V)
ax.plot([pin_positions[0][0], 1.5, 1.5, sensor_pin_positions[0][0]], 
        [pin_positions[0][1], pin_positions[0][1], sensor_pin_positions[0][1], sensor_pin_positions[0][1]], 
        'r-', linewidth=1.5)

# GND connections
ax.plot([pin_positions[1][0], 1.3, 1.3, sensor_pin_positions[3][0]], 
        [pin_positions[1][1], pin_positions[1][1], sensor_pin_positions[3][1], sensor_pin_positions[3][1]], 
        'k-', linewidth=1.5)

# Trig pin to D2
ax.plot([pin_positions[2][0], 1.1, 1.1, sensor_pin_positions[1][0]], 
        [pin_positions[2][1], pin_positions[2][1], sensor_pin_positions[1][1], sensor_pin_positions[1][1]], 
        'b-', linewidth=1.5)

# Echo pin to D3
ax.plot([pin_positions[3][0], 0.9, 0.9, sensor_pin_positions[2][0]], 
        [pin_positions[3][1], pin_positions[3][1], sensor_pin_positions[2][1], sensor_pin_positions[2][1]], 
        'g-', linewidth=1.5)

# Vibration motor to D4
ax.plot([pin_positions[4][0], 0.7, 0.7, motor_pin_positions[0][0]], 
        [pin_positions[4][1], pin_positions[4][1], motor_pin_positions[0][1], motor_pin_positions[0][1]], 
        'y-', linewidth=1.5)

# Vibration motor GND
ax.plot([motor_pin_positions[1][0], motor_pin_positions[1][0], 1.3, 1.3], 
        [motor_pin_positions[1][1], motor_pin_positions[1][1] - 0.5, motor_pin_positions[1][1] - 0.5, pin_positions[1][1]], 
        'k-', linewidth=1.5)

# Button to D5
ax.plot([pin_positions[5][0], 0.5, 0.5, button_pin_positions[0][0]], 
        [pin_positions[5][1], pin_positions[5][1], button_pin_positions[0][1], button_pin_positions[0][1]], 
        'm-', linewidth=1.5)

# Button to GND
ax.plot([button_pin_positions[1][0], button_pin_positions[1][0] + 0.5, button_pin_positions[1][0] + 0.5, 1.3, 1.3], 
        [button_pin_positions[1][1], button_pin_positions[1][1], button_pin_positions[1][1] - 0.7, button_pin_positions[1][1] - 0.7, pin_positions[1][1]], 
        'k-', linewidth=1.5)

# Battery to Arduino
ax.plot([battery_pin_positions[1][0], battery_pin_positions[1][0] + 0.5, battery_pin_positions[1][0] + 0.5, pin_positions[0][0]], 
        [battery_pin_positions[1][1], battery_pin_positions[1][1], pin_positions[0][1], pin_positions[0][1]], 
        'r-', linewidth=1.5)

ax.plot([battery_pin_positions[0][0], battery_pin_positions[0][0] + 0.7, battery_pin_positions[0][0] + 0.7, pin_positions[1][0]], 
        [battery_pin_positions[0][1], battery_pin_positions[0][1], pin_positions[1][1], pin_positions[1][1]], 
        'k-', linewidth=1.5)

# Add connection labels
ax.text(1.5, sensor_pin_positions[0][1] + 0.2, '5V', fontsize=7, color='red')
ax.text(1.3, sensor_pin_positions[3][1] + 0.2, 'GND', fontsize=7, color='black')
ax.text(1.1, sensor_pin_positions[1][1] + 0.2, 'Trig', fontsize=7, color='blue')
ax.text(0.9, sensor_pin_positions[2][1] + 0.2, 'Echo', fontsize=7, color='green')
ax.text(0.7, motor_pin_positions[0][1] + 0.2, 'D4', fontsize=7, color='orange')
ax.text(0.5, button_pin_positions[0][1] + 0.2, 'D5', fontsize=7, color='purple')

# Add legend/notes
notes = [
    "CONNECTIONS:",
    "1. HC-SR04 VCC → Arduino 5V",
    "2. HC-SR04 GND → Arduino GND",
    "3. HC-SR04 Trig → Arduino D2",
    "4. HC-SR04 Echo → Arduino D3",
    "5. Vibration Motor + → Arduino D4",
    "6. Vibration Motor - → Arduino GND",
    "7. Button → Arduino D5 & GND",
    "8. 9V Battery → Arduino power"
]

for i, note in enumerate(notes):
    ax.text(0.5, 8.5 - i*0.3, note, fontsize=8)

# Add beginner tips
tips = [
    "BEGINNER TIPS:",
    "• Use a breadboard for easier connections",
    "• Double-check all connections before powering on",
    "• The button needs a pull-up resistor (10kΩ) in actual circuit",
    "• For the vibration motor, add a transistor (e.g., 2N2222) and",
    "  a diode (e.g., 1N4001) for protection in actual circuit"
]

for i, tip in enumerate(tips):
    ax.text(7, 8.5 - i*0.3, tip, fontsize=8)

# Save the figure
plt.savefig('/home/ubuntu/smart_cane_project/circuit_diagram.png', dpi=300, bbox_inches='tight')
print("Circuit diagram created and saved as 'circuit_diagram.png'")

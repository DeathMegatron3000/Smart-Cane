# Smart Cane Project

An Arduino-based smart cane with obstacle detection for visually impaired individuals.

## Overview

This project enhances a standard white cane by adding ultrasonic obstacle detection with vibration feedback. The smart cane helps identify obstacles beyond the range of traditional canes, providing additional safety and independence for users.

## Features

- **Obstacle Detection**: Detects obstacles up to 4 meters away using HC-SR04 ultrasonic sensor
- **Tactile Feedback**: Provides vibration alerts when obstacles are detected within 30cm
- **User Control**: Button to temporarily disable detection when needed
- **Low Cost**: Uses affordable, widely available components (~$11.50-$24 excluding Arduino)
- **Beginner-Friendly**: Detailed documentation for easy assembly and use

## Components

- Arduino Uno microcontroller
- HC-SR04 ultrasonic sensor
- Vibration motor
- Push button
- 9V battery with holder and switch
- Breadboard and jumper wires
- Mounting materials

## Repository Contents

- `smart_cane_architecture.md` - System design and functional blocks
- `component_selection.md` - List of cost-effective components with pricing
- `circuit_diagram.png` - Visual representation of component connections
- `smart_cane.ino` - Arduino code for obstacle detection
- `assembly_instructions.md` - Step-by-step guide to building the smart cane
- `user_manual.md` - Guide for using and maintaining the smart cane
- `final_documentation.md` - Comprehensive overview of the entire project

## Getting Started

1. Review the `component_selection.md` file to gather all necessary components
2. Follow the `assembly_instructions.md` to build the circuit according to `circuit_diagram.png`
3. Upload the `smart_cane.ino` code to your Arduino Uno
4. Test the system following the instructions in the assembly guide
5. Mount the system to a standard white cane
6. Refer to `user_manual.md` for operation and maintenance

## Future Enhancements

- Multiple sensors for wider detection coverage
- Variable feedback based on distance
- Audio feedback options
- Power optimization for extended battery life
- Smartphone integration for configuration

## License

This project is open source and available for personal and educational use.

## Acknowledgments

This project was inspired by research on existing smart cane technologies, particularly the WeWalk Smart Cane and various Arduino-based DIY implementations.

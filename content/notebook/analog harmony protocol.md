---
title: "An Analog Harmony Protocol - AKA Intermals"
publish: y
date: 2023-01-10
abstract: "A simple protocol for defining harmony as a signal."
---

# Analog Harmony Protocol
Also called "Intermals".
This is an idea for encoding a chord and/or harmonic information in a single floating point value.

- The number to the left of the decimal defines the root in semitones equivalent. 
- The numbers to the right of the floating point defines rising semitone steps for each subsequent voice.

# Examples of Analog Harmony Protocol

```
Relative to C:

Cmaj7
0.434 //root, major 3rd, minor 3rd, major 3rd

Cmaj
0.43 //root, major 3rd, minor 3rd

Dmin
2.34 //root, minor 3rd, major 3rd

F stacked 5ths
5.777 f c d a  

B half-diminished
11.334 //b d f a    
		//root, minor 3rd, minor 3rd, major 3rd

Bmaj
-1.43  //root, major3rd, minor3rd

```


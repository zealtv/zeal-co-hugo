---
title: "Intermals - A Signal-Based Harmony Protocol"
publish: y
date: 2023-01-10
abstract: "A simple protocol for describing chord voicings as a signal."
---

# Intermals
This is an idea for encoding a chord and/or harmonic information in a single floating point value.

- The number to the left of the decimal defines the root in semitones. 
- The numbers to the right of the floating point defines rising semitone steps for each subsequent voice.
- useful for shooting harmonic information around as signals in rnbo.
- You can do weird *chord maths* maybe.

The possible chord voicings are both limited and limitless.

```
-- THE.INTERMAL --------------- 
	  .
   -12.074   <---- Signal    
	  .  
     / \ _To the right_
    /   |> Three additional 
   /    |> voices 0, 7,
  /     |> and 11 semitones 
 /      |> above the root.
|
|< Root twelve semitones below 
|< whatever reference pitch.

```


# Example Intermals

```
Relative to C:

Cmaj
0.43 //root, major 3rd, minor 3rd

Cmaj7
0.434 //root, major 3rd, minor 3rd, major 3rd

Cmin
0.34 //root, minor 3rd, major 3rd

Dmin
2.34 //root, minor 3rd, major 3rd

F stacked 5ths
5.777 // f c d a  

B half-diminished
11.334 //root, minor 3rd, minor 3rd, major 3rd

Bmaj
-1.43  //root, major3rd, minor3rd

```


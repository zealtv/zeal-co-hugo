---
title: "the concept formally known as intermals"
publish: y
date: 2023-01-10
abstract: "A simple protocol for describing chord voicings as a signal."
---

#  decimal + interval = decival 

A decival (or intermal) is a way of encoding a chord voicing and relative root pitch as a floating point value.

- The number to the left of the decimal defines the root in semitones. 
- The numbers to the right of the floating point defines rising semitone steps for each subsequent voice.

```
-- THE INTERMAL --
   -12.074   <---- Signal    
  
     / \ 
    /   |> Three additional 
   /    |> voices 0, 7,
  /     |> and 11 semitones 
 /      |> above the root.
|
|< Root twelve semitones below 
|< whatever reference pitch.

```

It might be useful for shooting harmonic information around as signals in rnbo.  You can do weird *chord maths* maybe. The possible chord voicings are simultaneously limited and limitless.



# Example decivals/intermals

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


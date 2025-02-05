---
title: semisteps (the concept formally known as intermals)
publish: y
date: 2024-01-10
abstract: "A simple protocol for describing chord voicings as a floating point number."
---
{{< youtube E_wUjTwJ_i8 >}}

#  semisteps
Semisteps are a way of encoding a chord voicing and relative root pitch as a floating point value.  Semisteps are currently implemented in [bop](https://github.com/zealtv).

- The number to the left of the decimal defines the root in semitones. 
- Each digit to the right of the floating point defines a new voice that many semitone above the previous voice.

```
-- THE SEMISTEP --
   -12.074   
     / \ 
    /   Three additional 
   /    voices 0, 7,
  /     and 11 semitones 
 /      above the root.
|
Root twelve semitones below 
whatever reference pitch.

```

The possible chord voicings are simultaneously limited and limitless. 



# Example semisteps
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


## Variations on a theme

# Strings and Frets
```
Tuning strings using semisteps:
0.555 // four strings tuned in fourths from a reference pitch

E.ADG // the above tuned to E

Fretting applied:
0.221 // Emaj E B E G#

```

# Bitplucking
```
//velocity coded as integer digit array

7965 // envelope values 0 to 9 across four voices
	
	// 0 mutes voice, 
	// 1 lets voice ring
	// 2 to 9 trigger voice

```


# As a speculative text-based language...

{{< youtube 57_gENjvj0g >}}

```
## CHEAT SHEET

[DIGITS] ($)ymbol

@ set root frequency
= sets string tuning 
> fret string
. convert to intermal

` set duration of bar
/ set subdivision
# ID tag 

[FLOAT] (l)owercase

  // set instrument (instruments configured externally)
s // set sampler bank and sample
a // set analog synth bank and sample
f // set FM synth bank and sample
g // set granular synth bank and sample

  // play settings
r // set retriggering
k // set attack (rising)
y // set decay (falling)
  
  // play and convert to [SIGNAL]
p // pluck intermal using attack decay envelope  
b // bow (interpolate) intermal using attack decay envelope

[SIGNAL] (U)ppercase

G // gain to 1.5
L // limiter to 0.99
O // Output

```

```
//EXAMPLE USING STRINGS AND FRETS
42@10 // set root frequency to E1
=0555 // string tuning e1 a2 d2 g3 
>1024 // applying frets f1 a2 e2 b3
1s001 // sampler bank 1 sample 001 
p7506 // bitplucking
1G500 // (G)ain
0L990 // (L)imiter
1O001 // (O)utput to dac 1 channel 1

//EXAMPLE USING INTERMALS
164@8 // set root frequency to E3
1.434 // intermal f2 a3 e3 b4 
2a051 // analog synth bank 2 preset 51 
k1000 // set attack 1000ms
d5000 // set decay 5000ms
i7506 // interpolate intermal and velociters
1G500 // (G)ain to 1.5
0L990 // (L)imiter to 0.99
1O001 // (O)utput to dac 1 channel 1

//EXAMPLES SETTING TIME INTERVAL
1?001 // one whole bar
2?001 // two whole bars
1?002 // one half-note
1?003 // one quater-note triplet
1?004 // one quater-note
03?16 // three 16th notes
040?2 // fourty bars
1?006 // one eighth note triplet
1?012 // one 16th note triplet

//EXAMPLE SETTONG ID
1#001 // could be read as bank one pattern 1


```
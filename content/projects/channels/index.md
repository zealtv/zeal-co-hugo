---
title: "Channels"
when: 
  - "2014"
heroImage: "./hero.jpg"
what: "Technical demonstration, installation, and single channel audio-visual work"
tags: ["av", "interactive", "software"]
with: ["Oliver Elmers"]
where: ["Melbourne Media Lab"]
tier: 2
---

{{< vimeo 93701429 >}}

A technical Demonstration of the [Spout](http://spout.zeal.co) realtime video sharing framework. 

Teaming up with Kiwi media artist Oliver Ellmers, we’ve started up a new experiential design company Blunk.  Our goal with Blunk is to use emerging technologies to create previously impossible experiences and one of our first pieces is a technical demonstration of the new Spout video sharing framework for windows.  Channels is a made-for-vimeo interactive installation built around a lovely old TV I found on the side of the road.  Six “channels” are created, each having a video output produced in a different realtime graphics framework as well as a colour palette.  The user is able to select different channels using a USB remote control which will then switch the TV to a new source as well as control the projections rotating around the TV.

![System diagram of Channels](./assets/arch_diagram.jpg)

Resolume served as the hub for the system.  Five sources were spouted in to Resolume: Processing, Max, OpenFrameworks, VVVV and VIZZable.  A video file was used to represent Resolume.

Max was used to interpret keystrokes from a wireless USB remote which were then converted to OSC and forwarded to both TouchDesigner and Resolume.  In Resolume, the OSC messages were used to switch between Spout senders and in TouchDesigner the same OSC messages were used to control the graphics being projected on to the ground around the TV and to apply transition effects to the source video.  As there is currently no native Spout support for TouchDesigner, we used SpoutCam to bring the source video in from Resolume using the video in TOP.  Finally, two video streams were sent from TouchDesigner,  one to the projector and one to the TV via a scan converter and RF modulator.

![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-11-09-232.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-34-09-523.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-34-38-803.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-35-11-664.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-35-37-154.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-36-08-546.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-36-10-858.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-37-48-675.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-38-31-742.jpg)
![Documentation of Channels installation](./assets/bandicam-2014-05-03-14-39-03-873.jpg)
![Documentation of Channels installation](./assets/IMG_7828.jpg)
![Documentation of Channels installation](./assets/IMG_7830.jpg)
![Documentation of Channels installation](./assets/IMG_7842.jpg)
![Documentation of Channels installation](./assets/IMG_7844.jpg)
![Documentation of Channels installation](./assets/IMG_7849.jpg)
![Documentation of Channels installation](./assets/IMG_7853.jpg)
![Documentation of Channels installation](./assets/IMG_7867.jpg)
![Documentation of Channels installation](./assets/IMG_7869.jpg)

We shot the video at Melbourne Medialab and the shoot ran for about 5 hours.  Happily, there were no crashes, no stumbles and everything purred happily with all 8 applications passing video between themselves and with Windows deciding to update unannounced in the background.  Many thanks to [Melbourne Medialab](http://www.medialabmelbourne.com.au) and [Super Team](http://www.superteam.net.au/) for their support.
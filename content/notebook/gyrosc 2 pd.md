
---
title: gyrosc 2 pd
date: 2022-01-31T20:07
lastmod: 2022-03-21T16:45:58+11:00
publish: y
---
![screenshot of PD patch](../files/Pastedimage20220129134527.png)

[Download gyrosc2pd.pd](../files/gyrosc2pd.pd)

This patch receives OSC data from [gyrosc](https://www.bitshapesoftware.com/instruments/gyrosc/) , and tags them with a dynamic send object to be accessed globally via named receive objects.   Available receives are shown on the right, and useful code snippets are provided for easy patching.

The default port is 9999.

Gyrosc is a very capable iOS application and can be [configured using a .CSV file](http://www.bitshapesoftware.com/instruments/gyrosc/configuration.html).  I use the application in tandem with an [PacketPunk - OSC logging on the DSTIKE ESP32 watch](PacketPunk%20-%20OSC%20logging%20on%20the%20DSTIKE%20ESP32%20watch.md) for logging data in the field. 

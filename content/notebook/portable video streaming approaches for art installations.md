---
title: "portable video streaming approaches for art installations"
date: 2022-05-31
publish: y
---

I am surveying small, locally streaming cameras for applications in art installations.   The focus is on affordable, hackable, wearable cameras for performance or interaction applications.

![](../files/nextech.png)

# NEXTECH QC3868
Recently I tested the [Nextech mini wifi camera](NEXTECH%20QC3868.md) - a handy device for portable realtime video streaming where latency is not a major factor.  Battery powered, good IR illumination at night, small and light.

# UV4L
[This is a good example of a Raspberry pi approach](https://www.reddit.com/r/raspberry_pi/comments/ppu00m/prototype_low_latency_wireless_streaming_camera/) that focusses on low latency - particularly helpful when using for tracking gestures, sonifying, or video piloting.   The system above uses [UV4L](https://www.linux-projects.org/uv4l/)  that allows you to capture and stream an HDMI output.  So you could, for example, build an [openframeworks](http://openframeworks.cc) app displaying a fullscreen video feed and then forward the fullscreen output of that application as a low latency MJPG stream.

# NDI
Another pi-based approach would be to send video via NDI with [Dicaffeinate](https://dicaffeine.com/). NDI is very easy to receive in frameworks and video tools - TouchDesigner, OpenFrameworks etc.  making a simple set up.  Latency and quality are hardware dependant and an rPi might not be up to the job if latency is primary concern
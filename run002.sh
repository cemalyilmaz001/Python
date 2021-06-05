#!/bin/bash
xfce4-terminal -x htop	|
xfce4-terminal -H -x sudo iftop -i wlan0

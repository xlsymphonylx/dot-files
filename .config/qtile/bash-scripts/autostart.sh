#!/bin/bash

# Start feh (wallpaper)
~/Scripts/set_random_wallpaper.sh &

# Start notification daemon
dunst &

# Start power manager
#xfce4-power-manager &

# Start picom for compositing effects
picom &

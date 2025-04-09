# Minecraft Map

A super quick & dirty approach to viewing a set of Minecraft coordinates
as an X-Y graph.

## Features

- Displays North/South/East/West correctly (flips the horizontal axis)
- Shows gridlines on multiples of 512 to align with in-game maps
- Overrides matplotlib's tendency to stretch the map to make it look better
- MIT licensed, use it however you like.

## To run:

- Install matplotlib.
  - Fedora: `sudo dnf install python3-matplotlib-gtk4`
- Clone this repo.
- Delete the example coordiantes and enter yours.
- Run `python Minecraft\ Map.py`

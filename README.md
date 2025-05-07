# Minecraft Map

Quickly view Minecraft coordinates as an X-Y graph.

## Features

- Displays North/South/East/West correctly (flips the vertical axis)
- Shows gridlines on multiples of 512 to align with in-game maps
- Overrides matplotlib's desire to stretch the map to make it look better

<img src="minecraft-map.png" alt="Example Map" width="400">

## Usage

- Install matplotlib.
  - Fedora: `sudo dnf install python3-matplotlib-gtk4`
- Clone this repo.
- Copy an example file and name it whatever you like: `cp example.py MyWorld.py`
- Add your coordinates to MyWorld.py.
- Generate your map: `./MyWorld.py`

Consider submitting any improvements you make as a pull request.

#!/usr/bin/env python3

MAP_TITLE = "Searanch"

# Village locations
VILLAGES = {
    # X, Y, Z, has_portal
    # if has_portal is True, that means the location has a nether portal
    # and will be displayed in red, False means the location will be blue.
    # X is left-right with negative to the west, Z is up-down with negative to the north.
    'Sea Ranch': (-2335, '?', 1338, True),
    'Hill Village': (-1200, 120, 600, True),
    'Home Base': (-200, '?', 80, True),
    'Snowy Village': (-1854, 63, -289, True),
    'The Harbor': (298, 63, -430, True),
    'Lumberjack Lair': (-428, 64, 206, False),
    'Boat House': (-754, 105, 30, False),
    'Many Ores': (492, 63, -857, False),
    'Beehive': (1093, 65, -460, False),
    'Zombie Village': (-2336, 105, 8, True),
    'Redstone Platform': (-2342, 105, 672, True)
}

# paths between locations
SKYWAYS = {
    # - points: List of coordinate tuples (required)
    # - is_tunnel: Boolean flag for tunnel style (defaults to False if not specified)
    # - show_label: Boolean flag to display name on map (defaults to False if not specified)
    # - label_offset: Optional (x, y) offset in pixels for label placement (defaults to (0, 6))
    # - label_fontsize: Relative font size adjustment (e.g., '+2' makes text larger, '-2' makes it smaller)
    # - label_rotation: Rotation angle in degrees (defaults to 0 for horizontal, try 90 for vertical)

    'harbor onramp': {
        'points': [(288, 63, -477), (288, 105, -520)]
    },
    'beehive onramp': {
        'points': [(1028, 79, -544), (1028, 105, -520)]
    },
    'Harbor Rd': {
        'points': [(0, 105, -520), (1028, 105, -520)],
        'show_label': True,
        'label_offset': (30, 6.5)
    },

    'Snowy Rd': {
        'points': [(-2544, 105, -350), (0, 105, -350)],
        'show_label': True,
        'label_fontsize': '+3',
        'label_offset': (0, 8)
    },
    'snowy village onramp': {
        'points': [(-1854, 63, -289), (-1854, 105, -350)],
    },
    'snowy tunnel 1': {
        'points': [(-1392, 105, -350), (-836, 105, -350)],
        'is_tunnel': True
    },
    'snowy tunnel 2': {
        'points': [(-1657, 105, -350), (-1578, 105, -350)],
        'is_tunnel': True,
    },
    'snowy tunnel 3': {
        'points': [(-2177, 105, -350), (-1991, 105, -350)],
        'is_tunnel': True,
    },

    'Homeshack Rd': {
        'points': [(0, 105, -520), (0, 105, 100), (-74, 105, 100)],
        'show_label': True,
        'label_fontsize': '-2',
        'label_offset': (8, 20),
        'label_rotation': 90
    },
    'Homeshack Rd Close': {
        'points': [(-88, 106, 87), (-223, 106, 87)],
    },

    'Boathouse Rd': {
        'points': [(-749, 105, -350), (-749, 105, 252)],
        'show_label': True,
        'label_offset': (0, 15),
        'label_fontsize': '-2'
    },
    'homeboat': {  # unnamed random road between home base and the boathouse
        'points': [(-224, 105, 0), (-949, 105, 0)],
    },

    'Lumberjack Ln': {
        'points': [(-229, 113, 208), (-355, 113, 208)],
        'show_label': True,
        'label_fontsize': '-2',
        'label_offset': (-10, -10)
    },
    'lumberjack onramp': {
        'points': [(-355, 113, 208), (-407, 63, 208)],
        'show_label': False
    },

    'Hill Village Rd': {
        'points': [(-228, 110, 94), (-228, 113, 595), (-1200, 113, 595)],
        'show_label': True,
        'label_offset': (-35, 7)
    },
    'Hill\nVillage\nRoad\nNorth': {
        'points': [(-224, 105, 96), (-224, 105, -350)],
        'show_label': True,
        'label_fontsize': '-3.5',
        'label_offset': (6, 2)
    },
    'hill tunnel 1': {
        'points': [(-927, 113, 595), (-970, 113, 595)],
        'is_tunnel': True,
    },
    'hill tunnel 2': {
        'points': [(-987, 113, 595), (-1200, 113, 595)],
        'is_tunnel': True,
    },

    'Sea Ranch Rd': {
        'points': [(-2331, 63, 1334), (-2331, 105, 1292), (-2331, 105, 1200), (-2000, 105, 1200), (-2000, 105, 600), (-1192, 105, 600)],
        'show_label': True,
        'label_offset': (40, 70)
    },
    'sea ranch tunnel 1': {
        'points': [(-1192, 105, 600), (-1248, 105, 600)],
        'is_tunnel': True,
    },
    'sea ranch tunnel 2': {
        'points': [(-1614, 105, 600), (-1799, 105, 600)],
        'is_tunnel': True,
    },

    'Zombie Rd': {
        'points': [(-2336, 105, 1229), (-2336, 105, -350)],
        'show_label': True,
        'label_rotation': 90,
        'label_offset': (9, 0)
    },
}

# this section should not be needed because they should all be defaults
OUTPUT_FILENAME = "Searanch Map.png"
GRID_SIZE = 512
FIGURE_SIZE = (10, 8)  # Width, height in inches
VILLAGE_MARKER_SIZE = 100
TUNNEL_LINE_WIDTH = 3
SKYWAY_LINE_WIDTH = 2

__import__('Minecraft Map').run()

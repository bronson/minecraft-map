#!/usr/bin/env python3

MAP_TITLE = "Searanch Nether"

# Village locations
VILLAGES = {
    # X, Y, Z, has_portal
    # if has_portal is True, that means the location has a nether portal
    # and will be displayed in red, False means the location will be blue.
    # X is left-right with negative to the west, Z is up-down with negative to the north.
    'The Harbor': (62, 40, -52, True),
    'Oslo': (-435, 74, -276, True),
    'Alpine Village': (-281, 100, -90, True),
    'Snowy Village': (-228, 102, -44, True),
    'Zombie Village': (-295, 99, 2, True),
    'Hill Village': (-162, 70, 75, True),
    'Sea Ranch': (-294, 61, 166, True),
    'Mushroom': (-369, 70, 117, True),
    'Four Seasons': (-526, 63, 120, True),
    'El Pueblo': (-738, 82, 189, True),
    'Redstone Platform': (-287, 99, 87, True),
    'Spawn': (-18, 53, 0, True),
    'Many Ores': (52, 39, -122, True),
    'Hidey Hole': (150, 61, -182, True),
    'Beehive': (114, 40, -81, True),
    'Pandora': (-471, 98, -53, True),
    'Woodland': (-531, 74, -90, True),
    'Mansion': (-593, 73, -144, True),
    'Wuwey': (-749, 77, -192, True),
    'Pitchfork': (-261, 61, 216, True),
}

# paths between locations
SKYWAYS = {
    # - points: List of coordinate tuples (required)
    # - is_tunnel: Boolean flag for tunnel style (defaults to False if not specified)
    # - show_label: Boolean flag to display name on map (defaults to False if not specified)
    # - label_offset: Optional (x, y) offset in pixels for label placement (defaults to (0, 6))
    # - label_fontsize: Relative font size adjustment (e.g., '+2' makes text larger, '-2' makes it smaller)
    # - label_rotation: Rotation angle in degrees (defaults to 0 for horizontal, try 90 for vertical)

    'hidey_hole_to_many_ores': {
        'points': [(150, 61, -182), (52, 39, -122)],
        'is_tunnel': True
    },
    'many_ores_to_harbor': {
        'points': [(52, 39, -122), (62, 40, -52)],
        'is_tunnel': True
    },
    'harbor_to_spawn': {
        'points': [(62, 40, -52), (-18, 53, 0)],
        'is_tunnel': True
    },
    'spawn_to_hill_village': {
        'points': [(-18, 53, 0), (-162, 70, 75)],
        'is_tunnel': True
    },
    'hill_village_to_sea_ranch': {
        'points': [(-162, 70, 75), (-294, 61, 166)],
        'is_tunnel': True
    },
    'sea_ranch_to_mushroom': {
        'points': [(-294, 61, 166), (-369, 70, 117)],
        'is_tunnel': True
    },
    'mushroom_to_four_seasons': {
        'points': [(-369, 70, 117), (-526, 63, 120)],
        'is_tunnel': True
    },
    'four_seasons_to_el_pueblo': {
        'points': [(-526, 63, 120), (-738, 82, 189)],
        'is_tunnel': True
    },
    'four_seasons_to_pandora': {
        'points': [(-526, 63, 120), (-471, 98, -53)],
    },
    'pandora_to_woodland': {
        'points': [(-471, 98, -53), (-531, 74, -90)],
    },
    'woodland_to_mansion': {
        'points': [(-531, 74, -90), (-593, 73, -144)],
    },
    'mansion_to_wuwey': {
        'points': [(-593, 73, -144), (-749, 77, -192)],
    },

    'sea_ranch_to_redstone_platform': {
        'points': [(-294, 61, 166), (-287, 99, 87)],
    },
    'redstone_platform_to_zombie': {
        'points': [(-287, 99, 87), (-295, 99, 2)],
    },
    'zombie_to_snowy': {
        'points': [(-295, 99, 2), (-228, 102, -44)],
    },
    'snowy_to_alpine': {
        'points': [(-228, 102, -44), (-281, 100, -90)],
    },
    'alpine_to_oslo': {
        'points': [(-281, 100, -90), (-435, 74, -276)],
    },
    'snowy_to_hill_spawn_midpoint': {
        'points': [(-228, 102, -44), (-90, 62, 38)],
    },
    'harbor_to_beehive': {
        'points': [(62, 40, -52), (114, 40, -81)],
    },
    'searanch_to_pitchfork': {
        'points': [(-294, 61, 166), (-261, 61, 216)],
    },



    # 'harbor onramp': {
    #     'points': [(288, 63, -477), (288, 105, -520)]
    # },
    # 'beehive onramp': {
    #     'points': [(1028, 79, -544), (1028, 105, -520)]
    # },
    # 'Harbor Rd': {
    #     'points': [(0, 105, -520), (1028, 105, -520)],
    #     'show_label': True,
    #     'label_offset': (30, 6.5)
    # },

    # 'Snowy Rd': {
    #     'points': [(-2544, 105, -350), (0, 105, -350)],
    #     'show_label': True,
    #     'label_fontsize': '+3',
    #     'label_offset': (0, 8)
    # },
    # 'snowy village onramp': {
    #     'points': [(-1854, 63, -289), (-1854, 105, -350)],
    # },
    # 'snowy tunnel 1': {
    #     'points': [(-1392, 105, -350), (-836, 105, -350)],
    #     'is_tunnel': True
    # },
    # 'snowy tunnel 2': {
    #     'points': [(-1657, 105, -350), (-1578, 105, -350)],
    #     'is_tunnel': True,
    # },
    # 'snowy tunnel 3': {
    #     'points': [(-2177, 105, -350), (-1991, 105, -350)],
    #     'is_tunnel': True,
    # },

    # 'Homeshack Rd': {
    #     'points': [(0, 105, -520), (0, 105, 100), (-74, 105, 100)],
    #     'show_label': True,
    #     'label_fontsize': '-2',
    #     'label_offset': (8, 20),
    #     'label_rotation': 90
    # },
    # 'Homeshack Rd Close': {
    #     'points': [(-88, 106, 87), (-223, 106, 87)],
    # },

    # 'Boathouse Rd': {
    #     'points': [(-749, 105, -350), (-749, 105, 252)],
    #     'show_label': True,
    #     'label_offset': (0, 15),
    #     'label_fontsize': '-2'
    # },
    # 'homeboat': {  # unnamed random road between home base and the boathouse
    #     'points': [(-224, 105, 0), (-949, 105, 0)],
    # },

    # 'Lumberjack Ln': {
    #     'points': [(-229, 113, 208), (-355, 113, 208)],
    #     'show_label': True,
    #     'label_fontsize': '-2',
    #     'label_offset': (-10, -10)
    # },
    # 'lumberjack onramp': {
    #     'points': [(-355, 113, 208), (-407, 63, 208)],
    #     'show_label': False
    # },

    # 'Hill Village Rd': {
    #     'points': [(-228, 110, 94), (-228, 113, 595), (-1200, 113, 595)],
    #     'show_label': True,
    #     'label_offset': (-35, 7)
    # },
    # 'Hill\nVillage\nRoad\nNorth': {
    #     'points': [(-224, 105, 96), (-224, 105, -350)],
    #     'show_label': True,
    #     'label_fontsize': '-3.5',
    #     'label_offset': (6, 2)
    # },
    # 'hill tunnel 1': {
    #     'points': [(-927, 113, 595), (-970, 113, 595)],
    #     'is_tunnel': True,
    # },
    # 'hill tunnel 2': {
    #     'points': [(-987, 113, 595), (-1200, 113, 595)],
    #     'is_tunnel': True,
    # },

    # 'Sea Ranch Rd': {
    #     'points': [(-2331, 63, 1334), (-2331, 105, 1292), (-2331, 105, 1200), (-2000, 105, 1200), (-2000, 105, 600), (-1192, 105, 600)],
    #     'show_label': True,
    #     'label_offset': (40, 70)
    # },
    # 'sea ranch tunnel 1': {
    #     'points': [(-1192, 105, 600), (-1248, 105, 600)],
    #     'is_tunnel': True,
    # },
    # 'sea ranch tunnel 2': {
    #     'points': [(-1614, 105, 600), (-1799, 105, 600)],
    #     'is_tunnel': True,
    # },

    # 'Zombie Rd': {
    #     'points': [(-2336, 105, 1229), (-2336, 105, -350)],
    #     'show_label': True,
    #     'label_rotation': 90,
    #     'label_offset': (9, 0)
    # },
}

# this section should not be needed because they should all be defaults
OUTPUT_FILENAME = "Searanch Map.png"
GRID_SIZE = 512
FIGURE_SIZE = (10, 8)  # Width, height in inches
VILLAGE_MARKER_SIZE = 100
TUNNEL_LINE_WIDTH = 3
SKYWAY_LINE_WIDTH = 2

__import__('Minecraft Map').run()

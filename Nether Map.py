#!/usr/bin/env python3

MAP_TITLE = "Searanch Nether"

# Village locations
VILLAGES = {
    # X, Y, Z, has_portal
    # if has_portal is True, that means the location has a nether portal
    # and will be displayed in red, False means the location will be blue.
    # X is left-right with negative to the west, Z is up-down with negative to the north.
    'The Harbor': (62, 40, -52, True),
    'The Armory': (39, 52, 31, True),
    'Oslo': (-435, 74, -276, True),
    'Alpine Village': (-281, 100, -90, True),
    'Sculk': (-337, 33, -105, True),
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
    'Coarsegold': (102, 60, 11, True),
    'Pillville': (83, 66, 114, True),
    'Twin Cities': (316, 78, 549, True),
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
    'coarsegold_to_harbor_beehive_midpoint': {
        'points': [(102, 60, 11), (88, 40, -66)],
    },
    'corsegold_to_pillville': {
        'points': [(102, 60, 11), (83, 66, 114)],
    },
    'pillville_to_twin_cities_junction': {
        'points': [(83, 66, 114), (83, 67, 261)],
    },
    'hill_village_to_twin_cities_1':  {
        'points': [(-162, 70, 75), (83, 67, 261)],
    },
    'hill_village_to_twin_cities_2':  {
        'points': [(83, 67, 261), (316, 78, 549)],
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

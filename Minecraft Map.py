# Minecraft Map, April 2025
# A quick way to plot Minecraft coordinates.

villages = {
    # X, Y, Z, has_portal
    # if has_portal is True, that means the location has a nether portal
    # and will be displayed in red, False means the location will be blue.
    # In Minecraft coordinates, X is left-right with negative to the West,
    # and Z is up-down with negative going to the North.
    'Sea Ranch': (-2335, '?', 1338, True),
    'Hill Village': (-1200, 120, 600, True),
    'Home Base': (-200, '?', 80, True),
    'Snowy Village': (-1854, 63, -289, False),
    'The Harbor': (298, 63, -430, True),
    'Lumberjack Lair': (-428, 64, 206, False),
    'Boat House': (-754, 105, 30, False),
    'Many Ores': (492, 63, -857, False),
    'Beehive': (1093, 65, -460, False),
    'Zombie Village': (-2336, 105, 8, False)
}

skyways = {
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
    'homeboat': {
        'points': [(-224, 105, 0), (-949, 105, 0)],
    },

    'Lumberjack Rd': {
        'points': [(-229, 113, 208), (-355, 113, 208)],
        'show_label': True,
        'label_fontsize': '-2',
        'label_offset': (-10, -10)
    },
    'lumberjack onramp': {
        'points': [(-355, 113, 208), (-407, 63, 208)],
        'show_label': False
    },

    'Hill\nVillage\nRoad\nNorth': {
        'points': [(-224, 105, 96), (-224, 105, -350)],
        'show_label': True,
        'label_fontsize': '-3.5',
        'label_offset': (6, 2)
    },
    'Hill Village Rd': {
        'points': [(-228, 110, 94), (-228, 113, 595), (-1200, 113, 595)],
        'show_label': True
    },
    'hill tunnel 1': {
        'points': [(-927, 113, 595), (-970, 113, 595)],
        'is_tunnel': True,
    },
    'hill tunnel 2': {
        'points': [(-987, 113, 595), (-1200, 113, 595)],
        'is_tunnel': True,
    }
}


#
#     ok let's go
#

import matplotlib.pyplot as plt

x_coords = [coord[0] for coord in villages.values()]
z_coords = [coord[2] for coord in villages.values()]
portals = [coord[3] for coord in villages.values()]
colors = ['red' if s else 'blue' for s in portals]
names = list(villages.keys())

# Create scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(x_coords, z_coords, s=100, color=colors)

# Draw skyway lines
for name, skyway in skyways.items():
    # Get properties from the skyway dictionary with defaults
    points = skyway['points']
    is_tunnel = skyway.get('is_tunnel', False)  # Default to False if not specified
    show_label = skyway.get('show_label', False)  # Default to False if not specified
    
    # Extract X and Z coordinates for all points
    x_values = [point[0] for point in points]
    z_values = [point[2] for point in points]
    
    # Plot the line
    if is_tunnel:
        line = plt.plot(x_values, z_values, 'darkgreen', alpha=0.9, linewidth=3)[0]
    else:
        line = plt.plot(x_values, z_values, 'g-', alpha=0.7, linewidth=2)[0]
    
    # Add a label to the line if requested
    if show_label:
        # Find middle point of the path for label placement
        middle_idx = len(x_values) // 2
        
        # For paths with multiple points, place label at midpoint
        if len(x_values) > 2:
            # Place at the middle segment
            mid_x = x_values[middle_idx]
            mid_z = z_values[middle_idx]
        else:
            # For simple two-point paths, place label at midpoint of the line
            mid_x = (x_values[0] + x_values[-1]) / 2
            mid_z = (z_values[0] + z_values[-1]) / 2
        
        # Get label customization options with defaults
        label_offset = skyway.get('label_offset', (0, 6))
        
        # Handle relative font sizes
        default_fontsize = 8
        label_fontsize_adjustment = skyway.get('label_fontsize', '0')  # Default to no adjustment
        
        # Apply the relative adjustment to the default font size
        if label_fontsize_adjustment.startswith('+') or label_fontsize_adjustment.startswith('-'):
            label_fontsize = default_fontsize + float(label_fontsize_adjustment)
        else:
            # If just a number is provided, treat it as a relative adjustment
            try:
                label_fontsize = default_fontsize + float(label_fontsize_adjustment)
            except ValueError:
                # If conversion fails, use default
                label_fontsize = default_fontsize
            
        label_rotation = skyway.get('label_rotation', 0)

        # Add the label with appropriate styling
        plt.annotate(name, (mid_x, mid_z), 
                    textcoords="offset points",
                    xytext=label_offset,
                    ha='center',
                    color='darkgreen',
                    fontsize=label_fontsize,
                    rotation=label_rotation,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", alpha=0.7))

# Add village labels with coordinates
for i, name in enumerate(names):
    # Add village name
    plt.annotate(name, (x_coords[i], z_coords[i]),
                 textcoords="offset points",
                 xytext=(0,12),
                 ha='center')

    # Add coordinates in smaller font right below name
    coord_text = f"({villages[name][0]}, {villages[name][1]}, {villages[name][2]})"
    plt.annotate(coord_text, (x_coords[i], z_coords[i]),
                 textcoords="offset points",
                 xytext=(0,6),
                 ha='center',
                 fontsize=5)

# Add coordinate grid and labels
plt.grid(False)  # Turn off default grid

# Find min and max of our data for setting fixed grid boundaries
min_x, max_x = min(x_coords), max(x_coords)
min_z, max_z = min(z_coords), max(z_coords)

# Add padding to ensure all points are visible (10% on each side)
x_padding = (max_x - min_x) * 0.1
z_padding = (max_z - min_z) * 0.1

# Set axis limits with padding
x_min, x_max = min_x - x_padding, max_x + x_padding
z_min, z_max = min_z - z_padding, max_z + z_padding

grid_size = 512

# Calculate grid line positions as multiples of 512
x_grid_min = (int(x_min) // grid_size) * grid_size
x_grid_max = (int(x_max) // grid_size + 1) * grid_size
z_grid_min = (int(z_min) // grid_size) * grid_size
z_grid_max = (int(z_max) // grid_size + 1) * grid_size

# Create X grid lines (vertical lines)
x_grid_points = list(range(x_grid_min, x_grid_max + 1, grid_size))
for x in x_grid_points:
    plt.axvline(x=x, color='gray', linestyle='-', alpha=0.3)

# Create Z grid lines (horizontal lines)
z_grid_points = list(range(z_grid_min, z_grid_max + 1, grid_size))
for z in z_grid_points:
    plt.axhline(y=z, color='gray', linestyle='-', alpha=0.3)

# Set up the axis lines, limits, and tick positions
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.xlim(x_min, x_max)
plt.ylim(z_min, z_max)
plt.xticks(x_grid_points)
plt.yticks(z_grid_points)

# Invert the y-axis since in Minecraft negative Z is North
plt.gca().invert_yaxis()

plt.title('Village Locations')
plt.xlabel('X Coordinate')
plt.ylabel('Z Coordinate')

# Make the plot square so that grid cells appear as squares
plt.gca().set_aspect('equal')

plt.tight_layout()
plt.savefig('minecraft_map.png')
print("Map saved as minecraft_map.png")
plt.show()

# Minecraft Map, April 2025
# A quick way to plot Minecraft coordinates.

# The coordinates:
# True means a location has a nether portal and will be displayed in red,
# False means the location will be blue.
# In Minecraft, X is left-right with negative to the West, and
# Z is up-down with negative going to the North.
villages = {         # X, Y, Z, has_portal
    'Sea Ranch': (-2335, '?', 1338, True),
    'Hill Village': (-1200, 120, 600, True),
    'Home Base': (-200, '?', 80, True),
    'Snowy Village': (-1854, 63, -289, False),
    'The Harbor': (298, 63, -430, True),
    'Lumberjack Lair': (-428, 64, 206, False),
    'Many Ores': (492, 63, -857, False),
    'Beehive': (1093, 65, -460, False)
}

skyways = {
    'harbor onramp': ((288, 63, -477), (288, 105, -520)),
    'harbor': ((0, 105, -520), (288, 105, -520)),
    'snowy village onramp': ((-1854, 63, -289), (-1854, 105, -349)),
    'snowy tunnel 1': ((-1392, 105, -349), (-836, 105, -349)),
    'snowy tunnel 2': ((-1657, 105, -349), (-1578, 105, -349)),
    'snowy village': ((-1854, 105, -349), (0, 105, -349)),
    'snowy harbor': ((0, 105, -520), (0, 105, -349))
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
for name, (start, end) in skyways.items():
    plt.plot([start[0], end[0]], [start[2], end[2]], 'g-', alpha=0.7, linewidth=2)

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
plt.show()

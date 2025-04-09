import matplotlib.pyplot as plt

# Minecraft coordinates. True means a location has a nether portal
# and will be displayed in red, False means the location will be blue.
villages = {
    'Sea Ranch': (-2335, '?', 1338, True),
    'Hill Village': (-1200, 120, 600, True),
    'Home Base': (-200, '?', 80, True),
    'Snowy Village': (-1800, '?', -360, False),
    'The Harbor': (298, 63, -430, True),
    'Lumberjack Lair': (-428, 64, 206, False),
    'Many Ores': (492, 63, -857, False)
}


#
#     ok let's go
#

# Extract x and y coordinates and status
x_coords = [coord[2] for coord in villages.values()]
y_coords = [coord[0] for coord in villages.values()]
portals = [coord[3] for coord in villages.values()]
colors = ['red' if s else 'blue' for s in portals]
names = list(villages.keys())

# Create scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(x_coords, y_coords, s=100, color=colors)
plt.gca().invert_xaxis()

# Add village labels with coordinates
for i, name in enumerate(names):
    # Add village name
    plt.annotate(name, (x_coords[i], y_coords[i]),
                 textcoords="offset points",
                 xytext=(0,12),
                 ha='center')

    # Add coordinates in smaller font right below name
    coord_text = f"({villages[name][0]}, {villages[name][1]}, {villages[name][2]})"
    plt.annotate(coord_text, (x_coords[i], y_coords[i]),
                 textcoords="offset points",
                 xytext=(0,6),
                 ha='center',
                 fontsize=5)

# Add coordinate grid and labels
plt.grid(False)  # Turn off default grid

# Get current axis limits to maintain the same view
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()

# Calculate grid line positions as multiples of 512
# Handle the inverted x-axis differently by using the original min/max values
x_grid_min = (int(x_min) // 512) * 512
x_grid_max = (int(x_max) // 512 + 1) * 512
y_grid_min = (int(y_min) // 512) * 512
y_grid_max = (int(y_max) // 512 + 1) * 512

# Create custom grid lines on multiples of 512
for i in range(y_grid_min, y_grid_max + 1, 512):
    plt.axhline(y=i, color='gray', linestyle='-', alpha=0.3)

# For X (Z-coordinates), be careful with the range direction
# When x_grid_min > x_grid_max (due to inversion), we need to reverse the range
x_range = range(x_grid_min, x_grid_max + 1, 512) if x_grid_min <= x_grid_max else range(x_grid_min, x_grid_max - 1, -512)
for i in x_range:
    plt.axvline(x=i, color='gray', linestyle='-', alpha=0.3)

# Set tick positions at multiples of 512
plt.xticks(x_range)
plt.yticks(range(y_grid_min, y_grid_max + 1, 512))

# Add axis lines
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Restore original view limits with the original min/max (inverted)
orig_x_min, orig_x_max = plt.xlim()
plt.xlim(orig_x_min, orig_x_max)
plt.ylim(y_min, y_max)

plt.title('Village Locations')
plt.xlabel('Z Coordinate')
plt.ylabel('X Coordinate')

# Make the plot square so that grid cells appear as squares
plt.gca().set_aspect('equal')

plt.tight_layout()
plt.show()

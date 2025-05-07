#!/usr/bin/env python3

# Minecraft Map Generator
# quickly plot Minecraft coordinates

import matplotlib.pyplot as plt

def generate_map(config):
    """Generate a Minecraft map from the provided configuration"""
    villages = getattr(config, "VILLAGES", {})
    skyways = getattr(config, "SKYWAYS", {})

    # Extract village coordinates
    x_coords = [coord[0] for coord in villages.values()]
    z_coords = [coord[2] for coord in villages.values()]
    portals = [coord[3] for coord in villages.values()]
    colors = ['red' if s else 'blue' for s in portals]
    names = list(villages.keys())

    # Create scatter plot
    figure_size = getattr(config, "FIGURE_SIZE", (10, 8))
    plt.figure(figsize=figure_size)

    village_marker_size = getattr(config, "VILLAGE_MARKER_SIZE", 100)
    plt.scatter(x_coords, z_coords, s=village_marker_size, color=colors)

    # Draw skyway lines
    tunnel_line_width = getattr(config, "TUNNEL_LINE_WIDTH", 3)
    skyway_line_width = getattr(config, "SKYWAY_LINE_WIDTH", 2)

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
            line = plt.plot(x_values, z_values, 'darkgreen', alpha=0.9, linewidth=tunnel_line_width)[0]
        else:
            line = plt.plot(x_values, z_values, 'g-', alpha=0.7, linewidth=skyway_line_width)[0]

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
    if x_coords and z_coords:  # Check for non-empty lists
        min_x, max_x = min(x_coords), max(x_coords)
        min_z, max_z = min(z_coords), max(z_coords)

        # Add padding to ensure all points are visible (10% on each side)
        x_padding = (max_x - min_x) * 0.1
        z_padding = (max_z - min_z) * 0.1

        # Set axis limits with padding
        x_min, x_max = min_x - x_padding, max_x + x_padding
        z_min, z_max = min_z - z_padding, max_z + z_padding

        grid_size = getattr(config, "GRID_SIZE", 512)

        # Calculate grid line positions as multiples of the grid size
        x_grid_min = (int(x_min) // grid_size) * grid_size
        x_grid_max = (int(x_max) // grid_size + 1) * grid_size
        z_grid_min = (int(z_min) // grid_size) * grid_size
        z_grid_max = (int(z_max) // grid_size + 1) * grid_size

        # Create X grid lines (vertical lines)
        x_grid_points = list(range(x_grid_min, x_grid_max + 1, grid_size))
        for x in x_grid_points:
            plt.axvline(x=x, color='gray', linestyle='-', linewidth=0.5, alpha=0.25)

        # Create Z grid lines (horizontal lines)
        z_grid_points = list(range(z_grid_min, z_grid_max + 1, grid_size))
        for z in z_grid_points:
            plt.axhline(y=z, color='gray', linestyle='-', linewidth=0.5, alpha=0.25)

        # Set up the axis lines, limits, and tick positions
        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.25)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.25)
        plt.xlim(x_min, x_max)
        plt.ylim(z_min, z_max)
        plt.xticks(x_grid_points)
        plt.yticks(z_grid_points)

        # Invert the y-axis since in Minecraft negative Z is North
        plt.gca().invert_yaxis()

    map_title = getattr(config, "MAP_TITLE", "Minecraft Map")
    plt.title(map_title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Z Coordinate')

    # Make the plot square so that grid cells appear as squares
    plt.gca().set_aspect('equal')

    plt.tight_layout()

    output_filename = getattr(config, "OUTPUT_FILENAME", "minecraft-map.png")
    plt.savefig(output_filename)
    print(f"Map saved as {output_filename}")
    plt.show()

def run():
    import inspect
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    generate_map(caller_module)

if __name__ == "__main__":
    print("This file must be run from a configuration file.")

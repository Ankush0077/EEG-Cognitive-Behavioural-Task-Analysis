import matplotlib.pyplot as plt
import numpy as np

def generate_colored_jars(color1, color2, ratio1, ratio2, image_number, num_circles=700, jar_size=(0.6, 0.8)):
    """
    Generate an image with two jars filled with circles of two different colors in a given ratio,
    with labeled jars and enclosing structures. The image is saved with a transparent background.
    
    Parameters:
    color1 (str): Color of the first set of circles.
    color2 (str): Color of the second set of circles.
    ratio1 (float): Percentage of color1 circles (0 to 1).
    ratio2 (float): Percentage of color2 circles (0 to 1).
    image_number (int): Number appended to the filename.
    num_circles (int): Total number of circles in each jar.
    jar_size (tuple): Size of the jar (width, height).
    """
    if ratio1 + ratio2 != 1:
        raise ValueError("Ratios must sum to 1.")
    
    fig, ax = plt.subplots(1, 2, figsize=(432/100, 244/100), dpi=100)
    fig.patch.set_alpha(0)  # Make background transparent
    
    map = {0: color1, 1: color2}
    for i, label in enumerate(['A', 'B']):  # Two jars labeled A and B
        x_positions = np.random.uniform(0.05, jar_size[0] - 0.05, num_circles)
        y_positions = np.random.uniform(0.05, jar_size[1] - 0.05, num_circles)
        
        for j in range(num_circles):
            color = np.random.choice([map[i], map[1-i]], p=[ratio1, ratio2])
            circle = plt.Circle((x_positions[j], y_positions[j]), 0.03, color=color, ec='black')
            
            # Clip circles extending beyond jar boundaries
            if 0.03 <= x_positions[j] <= jar_size[0] - 0.03 and 0.03 <= y_positions[j] <= jar_size[1] - 0.03:
                ax[i].add_patch(circle)
        
        # Draw jar structure (without top line)
        ax[i].plot([0, 0, jar_size[0], jar_size[0]], [0, jar_size[1], jar_size[1], 0], color='black', lw=2)
        ax[i].plot([0, jar_size[0]], [0, 0], color='black', lw=3)  # Bottom line of the jar
        
        ax[i].set_xlim(-0.1, jar_size[0] + 0.1)
        ax[i].set_ylim(-0.2, jar_size[1] + 0.1)
        ax[i].set_aspect('equal')
        ax[i].axis('off')
        
        # Add label below the jar
        ax[i].text(jar_size[0] / 2, -0.1, label, fontsize=14, ha='center', color='black')
    
    # Generate filename from color initials and image number
    filename = f"{color1[0].upper()}{color2[0].upper()}{image_number}.png"
    plt.savefig(filename, transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

# Example usage
generate_colored_jars(color1='blue', color2='red', ratio1=0.85, ratio2=0.15, image_number=1)
generate_colored_jars(color1='blue', color2='red', ratio1=0.85, ratio2=0.15, image_number=2)
generate_colored_jars(color1='blue', color2='red', ratio1=0.6, ratio2=0.4, image_number=3)
generate_colored_jars(color1='blue', color2='red', ratio1=0.6, ratio2=0.4, image_number=4)




# 
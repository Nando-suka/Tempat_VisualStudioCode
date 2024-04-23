import matplotlib.pyplot as plt
import numpy as np
from aquarel import load_theme

def apply_theme(theme_name):
   
    # Menambahkan atau mengatur tema
    theme = (
        load_theme(theme_name)
        .set_title(location="center",size="medium",weight="bold") 
        .set_color(text_color="#153448",)
        .set_font(sans_serif="Roboto")
        .set_axis_labels()
        .set_lines("--")
        )
    # Apply the theme to the current plot
    theme.apply()

def plot_trigonometric(x, y_sin, y_cos, y_tan, theme_name = "arctic_light", save_path=None, show_plot=False):
   
    # Create a figure object
    fig, ax = plt.subplots()

    # Plot the trigonometric functions
    ax.plot(x, y_sin, label="sin(x)")
    ax.plot(x, y_cos, label="cos(x)")
    ax.plot(x, y_tan, label="tan(x)")

    # Apply the specified theme
    apply_theme(theme_name)

    # Add legend
    ax.legend()

    # Add title
    plt.title("Trigonometri")

    # Save the plot to a file if save_path is provided
    if save_path:
        fig.savefig(save_path)

    # Show the plot if requested
    if show_plot:
        plt.show()

# Generate example data
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Plot each trigonometric function separately
plot_trigonometric(x, y_sin, np.zeros_like(x), np.zeros_like(x), theme_name="arctic_light",save_path="sinus_plot.png", show_plot=False)
plot_trigonometric(x, np.zeros_like(x), y_cos, np.zeros_like(x), theme_name="arctic_light",save_path="cosinus_plot.png", show_plot=False)
plot_trigonometric(x, np.zeros_like(x), np.zeros_like(x), y_tan, theme_name="arctic_light",save_path="tangen_plot.png", show_plot=False)


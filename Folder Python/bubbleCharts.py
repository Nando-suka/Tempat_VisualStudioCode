import matplotlib.pyplot as plt
import numpy as np
from aquarel import load_theme

# Menambahkan stle yang ada pada aquarel
tema = load_theme("boxy_light").set_overrides({
    "ytick.minor.visible": False,
    "xtick.minor.visible": True
})
tema.apply()

# Data sample
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50) * 1000  # Data untuk ukuran bubble

# Membuat plot
fig, ax = plt.subplots()

# Scatter plot dengan variabel 'z' sebagai ukuran bubble
bubble = ax.scatter(x, y, s=z, alpha=0.5)

# Menambahkan title dan labels
ax.set_title('Bubble Chart Example')
ax.set_xlabel('X Axis Value')
ax.set_ylabel('Y Axis Value')

# Menunjukkan color bar sebagai legenda untuk ukuran bubbles
cbar = fig.colorbar(bubble)
cbar.set_label('Bubble Size')

# Menampilkan plot
plt.show()

tema.apply_transforms()
# Membuat program berguna dan bermanfaat dengan menggunakan library aquarel

import matplotlib.pyplot as plt
from aquarel import load_theme
import numpy as np

# Memasukkan theme dari Aquarel
theme = load_theme("scientific")
theme.apply()

# Data untuk box plot
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Membuat box plot
plt.boxplot(data, patch_artist=True)

# Menambahkan label sumbu x
plt.xlabel('Data')

# Menambahkan label sumbu y
plt.ylabel('Nilai')

# Menambahkan judul
plt.title('Contoh Box Plot')

# Menampilkan grid
plt.grid(True)

# Menampilkan plot
plt.show()

# Menampilkan theme
theme.apply_transforms()    
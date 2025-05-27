# This is based on the following sample:
# https://matplotlib.org/stable/users/getting_started/
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# デフォルトのファイル名を Untitled に設定
c = fig.canvas
ext = c.get_default_filetype()
c.get_default_filename = lambda: f"Untitled.{ext}"

plt.show()

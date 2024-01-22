import geopandas as gpd
import matplotlib.pyplot as plt

# Download the dataset
world = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

# Explore Data
print(world.head())

# Create a Simple Map
world.plot(marker='o', color='red', markersize=5)
plt.title('City Distribution Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Customize the Map
ax = world.plot(marker='o', color='blue', markersize=10, alpha=0.5)
ax.set_title('City Distribution Map')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.show()

# Save the Map as an Image File
plt.savefig('city_distribution_map.png', format='png', dpi=300, bbox_inches='tight')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Create a new map
m = Basemap(llcrnrlon=46, llcrnrlat=39, urcrnrlon=88, urcrnrlat=55, resolution='i', projection='merc')

# Read in the shapefile
m.readshapefile('path/to/shapefile', 'kazakhstan')

# Extract the region names and values
region_names = []
region_values = []
for shape_dict in m.kazakhstan_info:
    region_names.append(shape_dict['NAME_1'])
    region_values.append(shape_dict['POPULATION'])

# Color the regions based on their values
colors = plt.cm.OrRd(region_values)

# Draw the map
for i, shape in enumerate(m.kazakhstan):
    # Get the name of the region
    name = region_names[i]

    # Get the color of the region
    color = colors[i]

    # Draw the region
    patches = [plt.Polygon(xy, True, fc=color, ec='k', lw=.2, alpha=.8) for xy in shape]
    ax.add_collection(PatchCollection(patches, match_original=True))

# Add a title
plt.title('Population Density in Kazakhstan')

plt.show()

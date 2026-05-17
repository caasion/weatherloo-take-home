import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import gcsfs
import xarray as xr

# Pick a start date
start = '2020-01-01T00:00'
end   = '2020-01-06T00:00'

# Connect to Google Cloud Storage (no account needed for public data)
fs = gcsfs.GCSFileSystem(token='anon')

# Open the Zarr store
store = fs.get_mapper('gcp-public-data-arco-era5/ar/1959-2022-6h-1440x721.zarr')
ds = xr.open_zarr(store, consolidated=True)

# Select just that time window, and only the two wind variables
wind_speed = ds['10m_wind_speed'].sel(time=slice(start, end))

# Load into memory (this triggers the actual download of chunks — it may take 30s–2min)
print("Loading data...")
wind_speed = wind_speed.compute()
# print("Done! Shape:", wind_speed.shape)
# Expected: (20, 721, 1440)

# matplotlib graph
fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

ax.add_feature(cfeature.COASTLINE, linewidth=0.5, color='white')
ax.add_feature(cfeature.BORDERS, linewidth=0.3, color='white', alpha=0.5)

# Draw the first frame
frame = wind_speed.isel(time=0)
im = ax.pcolormesh(
    wind_speed.longitude,
    wind_speed.latitude,
    frame,
    transform=ccrs.PlateCarree(),
    cmap='viridis',
    vmin=0,
    vmax=25
)
plt.colorbar(im, ax=ax, label='Wind speed (m/s)', shrink=0.6)
title = ax.set_title('')

def update(i):
    frame = wind_speed.isel(time=i)
    im.set_array(frame.values.ravel())
    title.set_text(f"Wind Speed at 10 meters — {str(wind_speed.time[i].values)[:16]}")
    return im, title

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(wind_speed.time),
    interval=600,
    blit=False
)

# Save as GIF
ani.save('wind_animation.gif', writer='pillow', fps=2.5, dpi=100)
print("Saved wind_animation.gif")
plt.show()
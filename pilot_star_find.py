from astropy.io import fits
from astropy.stats import mad_std
from photutils.detection import DAOStarFinder
import matplotlib.pyplot as plt

# 🔍 Kép betöltése
hdul = fits.open('ngc4414_fits/mastDownload/HST/u2en1001t/u2en1001t_c0f.fits')
image_data = hdul[0].data[0]  # WFPC2 chip 1 (pl. WF2)
hdul.close()

# 📈 Háttér zaj becslése
bkg_sigma = mad_std(image_data)

# 🌟 Csillagdetektálás
daofind = DAOStarFinder(fwhm=3.0, threshold=5.*bkg_sigma)
sources = daofind(image_data)

# 📋 Eredmények
print(sources[:5])  # első 5 detektált csillag

# 🖼️ Vizualizáció
plt.imshow(image_data, cmap='gray', origin='lower', vmin=0, vmax=500)
plt.scatter(sources['xcentroid'], sources['ycentroid'], s=30, edgecolor='red', facecolor='none')
plt.title("Detektált csillagok")
plt.show()

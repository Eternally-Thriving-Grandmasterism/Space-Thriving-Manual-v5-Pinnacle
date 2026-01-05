from astropy.coordinates import get_body, EarthLocation, AltAz
from astropy.time import Time

time = Time('2026-01-04T00:00:00')
loc = EarthLocation.of_site('greenwich')

jupiter = get_body('jupiter', time)
jupiter_altaz = jupiter.transform_to(AltAz(obstime=time, location=loc))
print(f"Jupiter visibility: alt {jupiter_altaz.alt.deg:.2f}°, az {jupiter_altaz.az.deg:.2f}° — orbital habitat alignment locked.")

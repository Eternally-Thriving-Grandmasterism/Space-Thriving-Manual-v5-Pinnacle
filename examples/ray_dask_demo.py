from space_thriving_manual import SpaceThrivingEngine

engine = SpaceThrivingEngine()
times = ["2026-01-04", "2026-07-04", "2027-01-04", "2027-07-04"]
orbits = engine.hybrid_ray_dask_orbits(times)
print(orbits)

batch = engine.hybrid_mega_habitat_array(num_habitats=200)
print(f"Hybrid batch shape: {batch.shape} — thriving distributed eternal!")

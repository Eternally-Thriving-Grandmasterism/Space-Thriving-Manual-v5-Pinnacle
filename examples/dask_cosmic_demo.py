from space_thriving_manual import SpaceThrivingEngine

engine = SpaceThrivingEngine()
times = ["2026-01-04", "2026-07-04", "2027-01-04", "2027-07-04"]
orbits = engine.distributed_dask_orbits(times)
print(orbits)

batch = engine.mega_habitat_batch(num_habitats=200)
print(f"Mega batch shape: {batch.compute().shape} — thriving distributed eternal!")

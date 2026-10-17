# finitevolume-python

> **Calendar reconstruction:** The historical records in [`docs/reconstructed-calendar-2026.csv`](docs/reconstructed-calendar-2026.csv) were generated on 2026-10-18. Their historical author dates are synthetic; they do not mean this project, its improvements, or work on them existed on those dates. The actual software improvements were completed on 2026-10-18. Original upstream authorship and history are preserved. Calendar coverage is not a measure of engineering quality or historical working time.

Development edition based on [Philip Mocz's original project](https://github.com/pmocz/finitevolume-python).
Original authorship, Git history, and the GPL-3.0 license are retained.

## Local improvement and verification

Primitive velocity recovery divides cell momentum directly by cell mass, removing
two full-array divisions per recovery without changing the finite-volume method.
Three numerical tests cover primitive/conserved round trips, periodic conservation,
and the physical Euler flux for a uniform state.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -v
```

Verified on 2026-10-18 with Python 3.13.5 and NumPy 2.1.3. A short 32x32
simulation matched the original conserved fields within floating-point tolerance.
A local 512x512 kernel benchmark measured median recovery times of 35.69 ms before
and 16.26 ms after (seven repeats of ten calls). These are kernel measurements,
not whole-simulation speedups; timings depend on the machine and load.

---

Finite Volume simulation of the Kelvin-Helmholtz Instability

## Create Your Own Finite Volume Fluid Simulation (With Python)

### Philip Mocz (2020) Princeton University, [@PMocz](https://twitter.com/PMocz)

### [📝 Read the Algorithm Write-up on Medium](https://levelup.gitconnected.com/create-your-own-finite-volume-fluid-simulation-with-python-8f9eab0b8305)

Simulate the Kelvin-Helmholtz Instability with Finite Volume


```
python finitevolume.py
```

![Simulation](./finitevolume.png)

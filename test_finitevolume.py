"""Numerical invariants for the finite-volume kernels."""
import unittest

import matplotlib
matplotlib.use("Agg")
import numpy as np

from finitevolume import applyFluxes, getConserved, getFlux, getPrimitive


class FiniteVolumeTests(unittest.TestCase):
    def test_primitive_conserved_round_trip(self):
        rng = np.random.default_rng(17)
        rho = rng.uniform(0.1, 5.0, (17, 23))
        vx = rng.uniform(-2.0, 2.0, rho.shape)
        vy = rng.uniform(-2.0, 2.0, rho.shape)
        pressure = rng.uniform(0.5, 4.0, rho.shape)
        gamma = 5 / 3
        for volume in (1e-6, 0.25, 100.0):
            conserved = getConserved(rho, vx, vy, pressure, gamma, volume)
            recovered = getPrimitive(*conserved, gamma, volume)
            for actual, expected in zip(recovered, (rho, vx, vy, pressure)):
                np.testing.assert_allclose(actual, expected, rtol=2e-13, atol=2e-13)

    def test_periodic_flux_update_conserves_total(self):
        rng = np.random.default_rng(21)
        field = rng.uniform(1.0, 2.0, (17, 23))
        total = field.sum()
        flux_x = rng.normal(size=field.shape)
        flux_y = rng.normal(size=field.shape)
        updated = applyFluxes(field, flux_x, flux_y, dx=0.1, dt=0.01)
        self.assertAlmostEqual(updated.sum(), total, places=11)

    def test_uniform_state_flux_matches_euler_equations(self):
        rho, vx, vy, pressure, gamma = 2.0, 0.3, -0.4, 1.5, 5 / 3
        actual = getFlux(rho, rho, vx, vx, vy, vy, pressure, pressure, gamma)
        energy = pressure / (gamma - 1) + 0.5 * rho * (vx * vx + vy * vy)
        expected = (rho * vx, rho * vx * vx + pressure,
                    rho * vx * vy, (energy + pressure) * vx)
        np.testing.assert_allclose(actual, expected, rtol=1e-14)


if __name__ == "__main__":
    unittest.main()

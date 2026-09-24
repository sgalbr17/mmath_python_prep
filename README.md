# Numerical Methods & Mathematical Modelling Portfolio

A collection of small, self-contained numerical simulations spanning
ODE solvers and PDEs, applied to problems in mathematical biology and
physics. Written while studying for an MMath in Mathematics at
Queen's University Belfast (differential equations, dynamical systems,
numerical analysis, PDEs) in pursuit of developing coding skills.

Each project is a single Python script with no dependencies beyond
NumPy and Matplotlib, a docstring explaining the maths, and a
generated output plot.

## Projects

| # | Project | Topic | Method |
|---|---------|-------|--------|
| 1 | [Euler ODE Solver](01-euler-ode-solver/) | Linear decay ODE, numerical stability | Forward Euler |
| 2 | [Predator-Prey Model](02-predator-prey-rk4/) | Lotka-Volterra nonlinear ODE system | RK4 |
| 3 | [1D Heat Equation](03-heat-equation-1d/) | Linear diffusion, Neumann BCs | Explicit FD (FTCS) |
| 4 | [2D Diffusion](04-diffusion-2d/) | Linear diffusion in 2D, periodic BCs | Explicit FD, 5-point Laplacian |
| 5 | [Fisher-KPP Equation](05-fisher-kpp-reaction-diffusion/) | Nonlinear reaction-diffusion, travelling waves | Explicit FD |

## Preview

<table>
<tr>
<td><img src="01-euler-ode-solver/output.png" width="260"></td>
<td><img src="02-predator-prey-rk4/output.png" width="260"></td>
<td><img src="03-heat-equation-1d/output.png" width="260"></td>
</tr>
<tr>
<td><img src="04-diffusion-2d/output.png" width="260"></td>
<td><img src="05-fisher-kpp-reaction-diffusion/output.png" width="260"></td>
<td></td>
</tr>
</table>

## What's covered

- **Numerical ODE methods:** forward Euler (and its stability limits) and fourth-order Runge-Kutta (RK4)
- **Numerical PDE methods:** explicit finite differences in 1D and 2D, von Neumann stability analysis
- **Boundary conditions:** Neumann (insulated/zero-flux) and periodic
- **Applied modelling:** predator-prey population dynamics, heat/mass diffusion, biological invasion (travelling waves)

## Requirements

```bash
pip install -r requirements.txt
```

Each script can then be run directly, e.g.:

```bash
cd 02-predator-prey-rk4
python predator_prey_rk4.py
```

Every script saves its plot to `output.png` in its own folder.


## About

Written by Sophie Galbraith, MMath Mathematics, Queen's University
Belfast.

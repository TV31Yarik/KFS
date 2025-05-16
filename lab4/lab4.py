import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lorenz(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

def simulate_lorenz(initial_state, t_max=30, dt=0.01):
    t_span = (0, t_max)
    t_eval = np.arange(0, t_max, dt)
    sol = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval)
    return sol.t, sol.y

def show_sensitivity():
    state_1 = [1.0, 1.0, 1.0]
    state_2 = [1.001, 1.0, 1.0]  

    t1, sol1 = simulate_lorenz(state_1)
    t2, sol2 = simulate_lorenz(state_2)

    plt.figure(figsize=(10, 5))
    plt.plot(t1, sol1[0], label="x (початкове значення)")
    plt.plot(t2, sol2[0], label="x (з похибкою)", linestyle="--")
    plt.title("Вплив малої похибки на Lorenz Attractor")
    plt.xlabel("Час")
    plt.ylabel("x координата")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

show_sensitivity()

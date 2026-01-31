# Quantum Battleship Environment Setup

This folder contains environment configuration files for the Quantum Battleship project.

## Quick Setup

### Option 1: Using Conda (Recommended)

Create the environment from the YAML file:
```bash
conda env create -f env/environment.yml
conda activate quantum_battleship
```

### Option 2: Using pip

Create a new conda environment and install packages:
```bash
conda create -n quantum_battleship python=3.11 -y
conda activate quantum_battleship
pip install -r env/requirements.txt
```

## Register Jupyter Kernel

After creating the environment, register it as a Jupyter kernel:
```bash
conda activate quantum_battleship
python -m ipykernel install --user --name=quantum_battleship --display-name="Python (Quantum Battleship)"
```

## Key Dependencies

- **qiskit** - Quantum computing framework
- **qiskit-aer** - Quantum circuit simulator
- **qiskit-ibm-runtime** - IBM Quantum runtime support
- **numpy** - Numerical computing
- **matplotlib** - Visualization
- **jupyter** - Notebook environment

## Updating the Environment

If you install new packages, update the environment files:
```bash
# Update environment.yml
conda env export > env/environment.yml

# Update requirements.txt
pip freeze > env/requirements.txt
```

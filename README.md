# RSA & Shor's Algorithm — Practical Quantum Computing Experiment

A practical experimental project exploring the relationship between **RSA cryptography, integer factorization, and Shor's Algorithm** using Python and Qiskit.

The main purpose of this project is to understand how Shor's Algorithm can theoretically factor an RSA modulus and why sufficiently powerful quantum computers could pose a threat to traditional RSA cryptography.

> **⚠️ Disclaimer:** This project is created **strictly for educational, experimental, and research purposes**. It uses very small toy numbers such as `15`, `21`, and `33` because a normal laptop cannot efficiently simulate large-scale quantum computers. This project is **not intended to break real-world RSA encryption, attack systems, bypass security mechanisms, or provide production cryptographic software.**

---

## 📌 Project Overview

RSA security relies on the difficulty of factoring a large integer into its prime factors.

For example:

```text
N = 15

15 = 3 × 5
```

For small numbers, classical computers can factor `N` easily.

Shor's Algorithm provides a quantum approach to integer factorization. The important part of the algorithm is finding the **period/order** of a modular exponentiation function.

This project explores that process step by step.

---

## 🎯 Objectives

The main objectives of this experiment are:

* Understand the basic mathematics behind RSA.
* Generate a small toy RSA key pair.
* Understand integer factorization.
* Implement the classical mathematical steps used after period finding.
* Explore the core idea behind Shor's Algorithm.
* Experiment with small RSA moduli such as `15`.
* Implement quantum circuits using Qiskit.
* Explore quantum period finding and the Quantum Fourier Transform (QFT).
* Compare classical and quantum-simulation approaches.
* Understand the limitations of simulating quantum algorithms on a normal laptop.

---

## 🧩 Experiment Architecture

The project follows this general workflow:

```text
                    RSA
                     │
                     ▼
             Choose p and q
                     │
                     ▼
              Calculate N
                     │
                     ▼
              RSA Modulus
                     │
                     ▼
             N = p × q
                     │
                     ▼
        ┌────────────────────────┐
        │  Shor's Algorithm      │
        └────────────────────────┘
                     │
                     ▼
              Choose a
                     │
                     ▼
       Find the period/order r
                     │
                     ▼
          Quantum Period Finding
                     │
                     ▼
        Quantum Fourier Transform
                     │
                     ▼
                Measurement
                     │
                     ▼
             Estimate period r
                     │
                     ▼
            Classical GCD
                     │
              ┌──────┴──────┐
              ▼             ▼
             p              q
              └──────┬──────┘
                     ▼
                  N = p × q
```

---

## 🔐 Part 1 — RSA Demonstration

The first experiment demonstrates a very small RSA system.

Example:

```text
p = 3
q = 5

N = p × q

N = 15
```

Euler's totient:

```text
φ(N) = (p - 1)(q - 1)

φ(15) = 2 × 4
       = 8
```

A small public exponent is selected:

```text
e = 3
```

The private exponent is calculated as:

```text
d = e⁻¹ mod φ(N)

d = 3
```

The resulting toy keys are:

```text
Public Key  = (3, 15)
Private Key = (3, 15)
```

A small message can then be encrypted and decrypted to demonstrate the basic RSA process.

> This RSA implementation is intentionally tiny and **must not be used for real security**.

---

# ⚛️ Part 2 — Shor's Algorithm

The second part demonstrates the mathematical structure of Shor's Algorithm.

Suppose:

```text
N = 15
```

We select:

```text
a = 2
```

We calculate:

```text
2¹ mod 15 = 2
2² mod 15 = 4
2³ mod 15 = 8
2⁴ mod 15 = 1
```

Therefore, the period is:

```text
r = 4
```

Because `r` is even, we calculate:

```text
a^(r/2)

= 2²

= 4
```

The factors can then be obtained using the greatest common divisor:

```text
gcd(4 - 1, 15)

= gcd(3, 15)

= 3
```

and:

```text
gcd(4 + 1, 15)

= gcd(5, 15)

= 5
```

Therefore:

```text
15 = 3 × 5
```

---

# 🧮 Classical Period-Finding Demonstration

The initial version of this project includes a classical implementation of period finding.

This allows the complete mathematical workflow to be tested on a normal computer.

However, this is **not a demonstration of quantum speedup**.

The classical implementation directly calculates:

```text
a^r mod N
```

until the result returns to `1`.

In a real implementation of Shor's Algorithm, the period-finding process is performed using a quantum circuit.

---

# ⚛️ Quantum Version

The next stage of the experiment uses **Qiskit** to construct and simulate quantum circuits.

The quantum workflow can be represented as:

```text
Quantum Register
       │
       ▼
Superposition
       │
       ▼
Modular Exponentiation
       │
       ▼
Quantum Period Finding
       │
       ▼
Quantum Fourier Transform
       │
       ▼
Measurement
       │
       ▼
Classical Post-Processing
       │
       ▼
Period r
       │
       ▼
GCD Calculation
       │
       ▼
Factors
```

The experiment focuses on understanding this process rather than attempting to factor large RSA keys.

---

# 💻 Technologies

* **Python**
* **Qiskit**
* **Quantum Circuit Simulation**
* **NumPy**
* **Mathematical Number Theory**
* **RSA Mathematics**
* **Quantum Fourier Transform**

---

# 📂 Project Structure

The project is organized approximately as follows:

```text
rsa-shor-experiment/
│
├── rsa_demo.py
│
├── shor_demo.py
│
├── quantum/
│   ├── period_finding.py
│   ├── qft.py
│   └── shor_quantum.py
│
├── experiments/
│   ├── experiment_15.py
│   ├── experiment_21.py
│   └── experiment_33.py
│
├── results/
│   └── README.md
│
├── requirements.txt
│
└── README.md
```

The structure may evolve as the experiment develops.

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rsa-shor-experiment.git
```

```bash
cd rsa-shor-experiment
```

## 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the RSA experiment

```bash
python rsa_demo.py
```

## 5. Run the classical Shor demonstration

```bash
python shor_demo.py
```

The quantum experiments can then be executed from the corresponding files in the `quantum/` directory.

---

# 🧪 Planned Experiments

### Experiment 1 — Toy RSA

Factor:

```text
N = 15
```

Demonstrate:

```text
RSA key generation
        ↓
Encryption
        ↓
Decryption
```

---

### Experiment 2 — Classical Factorization

Measure the time required to factor small integers using classical approaches.

---

### Experiment 3 — Classical Shor Workflow

Demonstrate:

```text
Choose a
   ↓
Find period r
   ↓
Calculate a^(r/2)
   ↓
GCD
   ↓
Factors
```

---

### Experiment 4 — Quantum Circuit Simulation

Build the quantum components required for Shor's Algorithm:

```text
Superposition
      +
Modular Arithmetic
      +
QFT
      +
Measurement
```

---

### Experiment 5 — Resource Analysis

Investigate:

* Number of qubits
* Circuit depth
* Number of gates
* Simulation time
* CPU utilization
* Memory usage
* Scaling with input size

---

# 📊 Future Research Direction

A major goal of the experiment is to investigate the computational cost of quantum algorithm simulation on classical hardware.

Possible measurements include:

```text
Input Size
     │
     ├── Execution Time
     ├── Memory Usage
     ├── CPU Usage
     ├── Number of Qubits
     ├── Circuit Depth
     └── Gate Count
```

These measurements can be used to understand the practical limitations of simulating quantum algorithms on conventional computers.

---

# ⚠️ Limitations

This project has several important limitations.

### 1. Small Numbers

The experiments use very small numbers such as:

```text
15
21
33
```

These numbers are deliberately chosen because quantum circuit simulation becomes increasingly expensive as the number of qubits grows.

### 2. Classical Simulation

Running a quantum circuit simulator on a laptop is **not equivalent to running the algorithm on a real quantum computer**.

The simulator uses classical computational resources to reproduce quantum behavior.

### 3. No Real RSA Breaking

This project does not demonstrate the factorization of real-world RSA keys.

Modern RSA uses extremely large key sizes, while this project uses toy values specifically for experimentation.

### 4. No Quantum Advantage Demonstration

The experiment does not claim to demonstrate a practical quantum speedup.

Its primary purpose is to understand the algorithm and its underlying mathematical and quantum concepts.

---

# 🔒 Security Disclaimer

**This repository is strictly for educational, experimental, and academic research purposes.**

The RSA implementations use intentionally small and insecure parameters. They are provided only to demonstrate cryptographic concepts and the theoretical relationship between RSA and quantum factorization.

Do **not** use the code in this repository for:

* Production cryptography
* Protecting sensitive information
* Real-world RSA key generation
* Attacking systems
* Unauthorized security testing
* Bypassing authentication or encryption
* Any activity without proper authorization

The project is intended for **learning, experimentation, quantum computing research, and academic study only**.

---

# 📚 Learning Topics

This project provides practical exposure to:

* RSA Cryptography
* Prime Factorization
* Modular Arithmetic
* Euler's Totient Function
* Greatest Common Divisor
* Period Finding
* Quantum Computing
* Qubits
* Quantum Superposition
* Quantum Measurement
* Quantum Fourier Transform
* Quantum Circuit Simulation
* Qiskit
* Post-Quantum Cryptography concepts

---

# 🔬 Research Question

A possible research question inspired by this experiment is:

> **How does the computational cost of simulating Shor's Algorithm on classical hardware change as the size of the integer being factored increases?**

Possible future extensions can investigate:

```text
Classical computation
        vs
Quantum circuit simulation
        vs
Real quantum hardware
```

with measurements based on computational resources and energy efficiency.

---

# 📜 License

This project is intended for educational and research use.

See the repository license for the applicable terms.

---

## 👨‍💻 Author

**Jeyarakavan Jeyakandan**

Computer Science Undergraduate
Sri Lanka

---

⭐ This repository is a practical learning experiment exploring the intersection of **cryptography, quantum computing, and computational efficiency**.

# ⛏️ Mining Production & Haulage Calculator

**A Python project applying programming to mining engineering and operational productivity analysis.**

## 📌 About the Project

The **Mining Production & Haulage Calculator** is a Python application designed to estimate truck haulage productivity based on payload capacity, fleet size, cycle time, operating hours, and utilization.

The project combines my interest in **Mining Engineering, Software Development, and Data Analysis** to explore how operational parameters influence estimated mine production.

This is an educational project developed to strengthen my programming skills and apply them to practical mining scenarios.

## 🎯 Objectives

- Calculate truck cycle time from its individual components.
- Estimate hourly and daily material production.
- Analyze the relationship between fleet size and productivity.
- Explore how operational utilization affects production estimates.
- Build a foundation for more advanced mining data analysis tools.

## ⚙️ Features — Version 1.0

- 🚛 Configurable truck payload capacity and fleet size.
- ⏱️ Calculation of total haulage cycle time.
- 📊 Estimation of cycles per hour per truck.
- 🏗️ Calculation of theoretical and effective hourly production.
- 📅 Estimation of daily production.
- ✅ Input validation for numerical parameters and percentages.
- 📋 Structured productivity report in the terminal.

## 🧮 Methodology

### 1. Truck Cycle Time

The total cycle time is calculated as:

`Cycle Time = Loading + Loaded Haul + Dumping + Empty Return + Waiting`

All times are measured in minutes.

### 2. Cycles per Hour

`Cycles per Hour = 60 / Cycle Time`

This estimates the number of complete cycles per hour for one truck.

### 3. Theoretical Hourly Production

`Theoretical Production = Payload × Cycles per Hour × Number of Trucks`

### 4. Effective Hourly Production

`Effective Production = Theoretical Production × Utilization`

Utilization is expressed as a decimal between 0 and 1.

### 5. Daily Production

`Daily Production = Effective Hourly Production × Operating Hours per Day`

These calculations assume identical trucks and cycle times across the fleet.

## 💻 Technologies

- **Python 3**
- Functions and modular programming
- Input validation and exception handling
- Mathematical modeling and productivity calculations

## 🚀 Getting Started

### Requirements

- Python 3 installed on your computer.
- A code editor or terminal.

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mining-production-calculator.git
```

Navigate to the project directory:

```bash
cd mining-production-calculator
```

Run the application:

```bash
python main.py
```

Follow the prompts to enter the operating parameters and generate the productivity report.

## 📈 Example Scenario

Consider a hypothetical haulage operation with the following parameters:

| Parameter | Value |
|---|---:|
| Truck payload capacity | 40 tonnes |
| Number of trucks | 3 |
| Loading time | 4 min |
| Loaded haul time | 12 min |
| Dumping time | 2 min |
| Empty return time | 8 min |
| Waiting time | 2 min |
| Operating hours | 8 h/day |
| Utilization | 85% |

**Estimated results:**

| Metric | Result |
|---|---:|
| Total cycle time | 28 min |
| Cycles per hour per truck | 2.14 |
| Theoretical hourly production | 257.14 t/h |
| Effective hourly production | 218.57 t/h |
| Estimated daily production | 1,748.57 t/day |

These figures are illustrative calculations, not actual production data from a mine.

## ⚠️ Model Assumptions and Limitations

The current version uses a simplified deterministic model.

- All trucks have the same payload capacity and cycle time.
- Waiting time is entered as a fixed value per cycle.
- Utilization is applied as a multiplier to theoretical production.
- Truck queues, interactions between loading and dumping equipment, road conditions, payload variability, and stochastic breakdowns are not simulated.
- The model does not account for all operational constraints that may limit actual production.

Consequently, the results should be interpreted as preliminary productivity estimates rather than operational forecasts.

## 🛠️ Development Roadmap

- [x] **V1.0 — Basic Productivity Calculator**
- [ ] **V2.0 — Scenario Analysis and Fleet Comparison**
- [ ] **V3.0 — Data Analysis with Pandas**
- [ ] **V4.0 — Productivity Visualizations with Matplotlib**
- [ ] **V5.0 — Improved Operational Modeling**
- [ ] **V6.0 — Documentation and Portfolio Presentation**

Future versions will explore how changes in cycle time, utilization, and fleet size affect estimated production, with increasingly detailed analytical tools.

## 👨‍💻 About Me

I am a Mining and Energy Engineering student at the University of Castilla-La Mancha (UCLM), with previous academic experience in Computer Systems Engineering.

I am interested in applying programming and data analysis to mining operations, productivity optimization, and engineering decision-making.

This project is part of my effort to develop a profile that combines **mining knowledge, software development, and data-driven problem-solving**.

## 💬 Final Note

*The goal is not just to calculate tonnes per hour, but to understand which operational variables influence productivity and how data can support better engineering decisions.*

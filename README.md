# ARI711S-Assignment-Coders

This repository contains the solution for the **ARI711S Artificial Intelligence Assignment** (Informed Search section) completed by the group *Assignment Coders*.

---

# ARI711S: Artificial Intelligence Assignment

**Group Name:** ARI711S Assignment Coders
**Institution:** Namibia University of Science and Technology (NUST)
**Qualification:** Bachelor of Computer Science (Software Development)
**Course Coordinator:** Naftali Indongo (GitHub: naftalindeapo)

---

## 📌 Project Overview

This project focuses on **Informed Search Algorithms**, specifically solving a **warehouse navigation problem**.

The goal is to move an agent from a starting position (**A**) to a goal position (**B**) while avoiding obstacles in a grid-based environment.

The following algorithms were implemented:

* **Greedy Best-First Search**
* **A* Search (A-Star)**

Both algorithms are compared in terms of:

* Path efficiency
* Optimality
* Behavior in grid navigation

---

## ⚙️ Key Features

* Grid-based warehouse simulation
* Pathfinding using informed search
* Heuristic function (Euclidean Distance)
* Path reconstruction
* Visual representation of paths in the notebook
* Comparison between Greedy and A*

---

## 👥 Group Members & Contributions

1. **Fiauana Denilson**
   Student Number: 223078263
   GitHub Username: FabiO20000

2. **Namolo Wilhelm**
   Student Number: 223106143
   GitHub Username: Focusrn

---

## 📂 Repository Structure

* `ARI711S_Assignment_Notebook.ipynb` → Main notebook with explanations and results
* `algorithms.py` → Implementation of Greedy and A* search algorithms
* `warehouse.py` → Warehouse environment and grid handling
* `node.py` → Node structure for search tree
* `main.py` → Script to test algorithms via terminal
* `maps/warehouse1.txt` → Input grid for the warehouse problem
* `ARI711S_Report_Final.pdf` → Final report document
* `README.md` → Project documentation

---

## 🚀 How to Run the Project

### ▶ Option 1: Notebook (Recommended)

1. Open `ARI711S_Assignment_Notebook.ipynb`
2. Run all cells
3. View:

   * Paths generated
   * Visual grid output
   * Explanation of results

---

### ▶ Option 2: Python Script

Run the following in terminal:

```bash
python main.py
```

---

## 🧠 Algorithm Details

### Greedy Best-First Search

* Uses only the heuristic function
* Faster but does not guarantee optimal solutions

### A* Search

* Uses:
  f(n) = g(n) + h(n)
* Guarantees optimal path when heuristic is admissible

---

## 📊 Conclusion

The results show that:

* **Greedy Search** is faster but may produce suboptimal paths
* **A* Search** provides optimal and more reliable solutions

---

## 📄 Notes

* The notebook contains full explanations and outputs as required by the assignment
* All code is modular and well-documented
* Visualization of paths is included for clarity

---

## 📜 License

This project is submitted for academic purposes as part of ARI711S coursework.

---

**Note to Marker:** As requested, **naftalindeapo** has been added as a contributor to this repository.

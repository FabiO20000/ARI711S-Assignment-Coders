# ARI711S Warehouse Search Assignment

## 📌 Overview

This project implements **Greedy Best-First Search** and **A*** algorithms to solve a warehouse navigation problem.

The objective is to find the most efficient path from a starting point (A) to a goal (B) in a grid-based warehouse while avoiding obstacles.

---

## 📂 Project Structure

* `main.py` → Runs the program
* `warehouse.py` → Handles the grid environment
* `algorithms.py` → Contains Greedy and A* search
* `node.py` → Defines the Node structure
* `maps/` → Contains warehouse layouts

---

## ⚙️ How to Run

1. Make sure Python is installed
2. Open terminal in project folder
3. Run:

```
python main.py
```

---

## 🤖 Algorithms Used

* Greedy Best-First Search
* A* Search

---

## 👥 Group Members

* Fiauana Denilson (223078263)
* Namolo Wilhelm (223106143)
* 

---

## 📄 Notes

* A* guarantees optimal path using:
  f(n) = g(n) + h(n)
* Heuristic used: Euclidean Distance

---

## 📌 Conclusion

A* provided optimal results, while Greedy was faster but may not always produce the shortest path.

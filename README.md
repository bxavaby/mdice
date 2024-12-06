# 🎲 MDICE: THE MAGIC DICE GAMBLE

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey?style=flat-square)](#)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square)](CONTRIBUTING.md)
[![GitHub issues](https://img.shields.io/github/issues/bxavaby/mdice?style=flat-square)](https://github.com/bxavaby/mdice/issues)
[![GitHub forks](https://img.shields.io/github/forks/bxavaby/mdice?style=flat-square)](https://github.com/bxavaby/mdice/network)
[![GitHub stars](https://img.shields.io/github/stars/bxavaby/mdice?style=flat-square)](https://github.com/bxavaby/mdice/stargazers)

**Mdice** is inspired by *Kakegurui Twin*. In this game, players face off a dealer in a strategic battle of dice rolls, however.. **THE DEALER ALWAYS HAS THE UPPER HAND**. 

---

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Game Rules](#game-rules)
- [Dice Probabilities](#dice-probabilities)
- [Project Structure](#project-structure)
- [How to Play](#how-to-play)
- [License](#license)

---

## Demo
![Mdice Demo](assets/magic.gif)  
*✨ A walkthrough ✨*

---

## Features
- **🎮 Optional loading screen**: The `-nl` flag skips the loading screen.
- **💰 Balance status**: Persistent tracking across sessions.
- **🎯 Probability**: The dealer picks second.

---

## Game Rules
1. Starting balance of **¥100 million**.
2. Each turn, the player:
   - 💸 Places a bet in **¥** (`100k`, `3M`, `9B`).
   - Picks their dice before the dealer.
3. Both the player and dealer roll their dice.
4. If the player's roll is higher, they ✅ **double their bet**; otherwise, they ❌ lose the bet amount.

---

## Dice Probabilities

#### **Each die has unique numbers, creating strategic advantages and disadvantages**
- **⚫**: `3, 3, 4, 4, 8, 8`
- **⚪**: `1, 1, 5, 5, 9, 9`
- **🔴**: `2, 2, 6, 6, 7, 7`

#### **Statistical advantages**
- **⚫ > 🔴** (66.7%)
- **⚪ > ⚫** (66.7%)
- **🔴 > ⚪** (66.7%)

---

## **Project Structure**
```plaintext
.
├── balance.json      # balance track
├── kolo.py           # utilities
└── mdice.py          # game logic
```

---

## **Installation and Usage**

#### **Prerequisites**
- Python 3.8 or later
- Virtual environment (recommended)

#### **Steps to Run**
1. **Clone the repository**:

   ```bash
   git clone https://github.com/bxavaby/mdice.git
   cd mdice
   ```
   
2. **Run the Game**:

   ```bash
   python mdice.py
   ```
   
---

## License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

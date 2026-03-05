# Tic-Tac-Toe AI using Minimax Algorithm 🎮🤖

## Overview

This project implements an intelligent **Tic-Tac-Toe game** where a human player competes against an AI agent.
The AI uses the **Minimax algorithm with Alpha-Beta Pruning** to make optimal decisions, making it extremely difficult for the human player to win.

The project demonstrates the application of **game theory and search algorithms** in artificial intelligence.

## Features

* Human vs AI gameplay
* Intelligent AI opponent using **Minimax Algorithm**
* **Alpha-Beta Pruning** for improved efficiency
* Graphical user interface built using **Python Tkinter**
* Scoreboard tracking **Human Wins, AI Wins, and Draws**
* Restart button to reset the game board

## Technologies Used

* Python
* Tkinter (for graphical interface)
* Minimax Algorithm
* Alpha-Beta Pruning

## How the AI Works

The AI evaluates all possible moves using the **Minimax algorithm**.
It simulates every possible game state and chooses the move that maximizes its chances of winning while minimizing the player's chances.

Alpha-Beta pruning is used to improve performance by eliminating branches in the search tree that do not affect the final decision.

## Game Rules

* The human player uses **X**
* The AI uses **O**
* Players take turns placing their symbols on the board
* The first player to align three symbols horizontally, vertically, or diagonally wins
* If all spaces are filled and no player wins, the game ends in a draw

## How to Run the Project

1. Install Python on your system.
2. Clone or download this repository.
3. Navigate to the project directory.
4. Run the following command:

python tic_tac_toe_ai_gui.py

5. The game window will open and you can start playing against the AI.

## Project Objective

The goal of this project is to understand:

* Artificial Intelligence in games
* The Minimax search algorithm
* Alpha-Beta pruning optimization
* GUI development using Python

## Future Improvements

* Add difficulty levels (Easy, Medium, Hard)
* Add sound effects and animations
* Improve the graphical interface
* Add multiplayer mode

## Author

Developed as part of an **AI Internship Task**.

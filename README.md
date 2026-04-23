# IntroToComputation Final Project

A Python desktop GUI application that simulates a fast-food self-ordering kiosk experience ("MCMC DRIVE") using Tkinter and Pillow.

> **Important:** This is **not** a vibe coding app. It is a structured GUI programming project built around explicit user interface flows, state handling, and checkout logic.

## Project Overview

This project demonstrates an interactive ordering system with three main flows:

1. **Landing screen** where users choose order mode (Dine In / Take Away)
2. **Menu navigation** across food and drink categories with item quantity selectors
3. **Payment screen** that summarizes selected items, computes totals, applies discount codes, and captures payment method

The app is implemented as a single Python script (`tubess.py`) and relies on Tkinter for UI components plus Pillow for image handling.

## Key Features

- Desktop GUI built with **Tkinter**
- Multi-screen ordering workflow with menu tabs:
  - Food
  - Drinks
  - Payment
- Quantity selection per product using `Spinbox`
- Order summary generation from selected quantities
- Price calculation for all selected products
- Discount code support (predefined valid codes)
- Payment method selection:
  - Cash
  - Credit card input
- Interactive widgets: `Frame`, `Label`, `Button`, `Checkbutton`, `Entry`, `Spinbox`, and menus

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Imaging:** Pillow (`PIL.Image`, `PIL.ImageTk`)

## Repository Structure

- `tubess.py` — Main application file containing all UI flow, menu handling, and payment logic

## Prerequisites

- Python 3.x
- Pillow library installed

Install Pillow:

```bash
pip install pillow
```

## How to Run

From the repository root:

```bash
python tubess.py
```

## How the App Works

### 1. Start Screen
- Displays branding and two ordering choices (`DINE IN` / `TAKE AWAY`)
- Both options open the same ordering window flow

### 2. Food and Drinks Selection
- Menu bar allows switching between `Food`, `Drinks`, and `Payment`
- Users set quantities for products 1–12 via spinboxes
- The app keeps selected values in dictionaries and restores them when switching categories

### 3. Payment and Checkout
- Selected items with quantity > 0 are displayed in order list sections
- Total is computed from quantity × unit price
- Optional discount code can reduce total (30% for valid codes)
- User chooses payment method (cash or credit)

## Current Limitations

- Uses hard-coded local Windows paths for icon/image assets (e.g., `c:\Users\...`)
- Implemented in a single large script with many global variables
- Product names are generic placeholders (`product1`, `product2`, etc.)
- No automated tests in the repository
- No packaging or dependency lock file

## Suggested Improvements

- Replace hard-coded absolute asset paths with relative project paths
- Split code into modules/classes for maintainability
- Add product metadata (real names, categories, images) via config/data files
- Add unit tests for pricing and discount logic
- Add input validation for payment fields
- Add a `requirements.txt` and optional virtual environment instructions

## Educational Value

This project is a solid introductory computation/software project for practicing:

- Event-driven programming
- GUI state management
- Data structures for UI-backed logic
- Basic transaction flow design

## License

No license file is currently included in this repository.

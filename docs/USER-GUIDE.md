# CONS Job User Guide

Welcome to CONS Job, a beginner-friendly Integrated Development Environment (IDE) for Scheme programming. This guide will help you install, configure, and use the key features of the application.

## 1. Installation and Running

### Prerequisites
- **Python 3.10+**: Ensure Python is installed on your system.
- **A Scheme Interpreter**: The IDE works with various Scheme implementations. Install at least one:
  - **MIT/GNU Scheme**: `sudo apt install mit-scheme` or `brew install mit-scheme`
  - **GNU Guile**: `sudo apt install guile-3.0` or `brew install guile`
  - **Chez Scheme**: `sudo apt install chezscheme` or `brew install chezscheme`
  - **Chibi-Scheme**: Available via package managers or from source
  - **CHICKEN Scheme**: `sudo apt install chicken-bin` or `brew install chicken`

### Starting CONS Job
CONS Job comes with automated scripts for easy setup and launching:

1.  **Open a terminal** in the CONS Job project directory.
2.  **Run the launch script**:
    ```bash
    ./run.sh
    ```
    - The script will automatically create a virtual environment (`venv`) if it doesn't exist.
    - It will install all necessary dependencies (`PyQt6`, etc.).
    - It will launch the application.

## 2. Interface Overview

The main window is divided into three sections:

1.  **File Browser (Left)**: Navigate your project directories.
2.  **Code Editor (Center)**: The main area for writing Scheme code. Supports multiple tabs.
3.  **Terminal (Bottom)**: Integrated Scheme REPL (MIT Scheme by default) for immediate code execution.

### Menu Bar
- **File**: Create New files, Open existing ones, Save, or Exit.
- **Edit**: Access Preferences and Find/Replace.
- **Terminal**: Control the REPL (Restart, Clear, Interrupt) and send code to it.
- **View**: Toggle File Browser and Terminal visibility.
- **Help**: About information.

## 3. Key Features

### Code Editor
- **Syntax Highlighting**: Keywords, numbers, strings, and comments are colored for readability.
- **Parenthesis Matching**: Placing the cursor next to a parenthesis highlights its matching partner. Mismatched parentheses are highlighted in red.
- **Line Numbers**: Displayed in the left gutter.
- **Tabbed Editing**: Work on multiple files simultaneously.

### Integrated Terminal (REPL)
The bottom panel runs your chosen Scheme interpreter (MIT Scheme by default). You can type Scheme expressions directly here.
- **Interactive**: Type `(+ 1 2)` and press Enter to see `3`.
- **History**: Use Up/Down arrows to cycle through command history.
- **Integration**:
    - **Ctrl+Enter**: Sends the currently selected text (or the current line) from the Editor to the REPL.
    - **Ctrl+L**: Loads the current file into the REPL using `(load "filename")`.
    - **Ctrl+C**: Interrupts the current computation.
- **Restart**: Use **Terminal → Restart REPL** to restart with current settings.

### File Browser
- **Navigation**: Double-click folders to expand/collapse.
- **Opening Files**: Double-click a file (`.scm`, `.ss`, `.sld`, `.sls`) to open it in the editor.
- **Context Menu**: Right-click to Create New File/Folder, Rename, or Delete items.

## 4. Configuration

Access the settings via **Edit -> Preferences**.

### Editor Settings
- **Font**: Change the font family (e.g., "Monospace", "Courier New") and size.
- **Tab Width**: Set the indentation space count (default: 2).
- **Line Numbers**: Toggle visibility.

### Terminal Settings
- **Interpreter Selection**: Choose from automatically detected Scheme interpreters:
  - The dropdown shows all installed interpreters (MIT Scheme, Guile, Chez, Chibi, etc.) with version info.
  - Click **Refresh** to re-scan for newly installed interpreters.
  - Check **Use custom path** to specify a custom interpreter location.
  - Use **Browse** to locate an interpreter executable.
- **Scrollback**: Limit the number of lines retained in the terminal history.
- **Restart Prompt**: When you change the interpreter and click OK, you'll be asked if you want to restart the REPL immediately with the new interpreter.

### Appearance
- **Theme**: Switch between **Dark** and **Light** themes to suit your preference.

## 5. Scheme Quick Reference

Here's a quick reference for common Scheme constructs:

```scheme
;; Define a function
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

;; Define a variable
(define greeting "Hello, Scheme!")

;; Lambda expressions
(define square (lambda (x) (* x x)))

;; List operations
(car '(1 2 3))      ; => 1
(cdr '(1 2 3))      ; => (2 3)
(cons 0 '(1 2 3))   ; => (0 1 2 3)

;; Higher-order functions
(map square '(1 2 3 4 5))  ; => (1 4 9 16 25)

;; Conditionals
(cond
  ((< x 0) 'negative)
  ((= x 0) 'zero)
  (else 'positive))
```

## 6. Troubleshooting

- **"No interpreters found"**: Ensure a Scheme interpreter is installed and in your PATH.
  - Ubuntu/Debian: `sudo apt install mit-scheme` or `sudo apt install guile-3.0`
  - macOS: `brew install mit-scheme` or `brew install guile`
  - If installed in a custom location, use the **Custom path** option in Preferences.
- **REPL not responding**: Try **Terminal → Restart REPL** or use **Ctrl+C** to interrupt.
- **PyQt6 Errors**: If you encounter display issues, ensure your graphics drivers are up to date.
- **File extension filtering**: The file browser filters for `.scm`, `.ss`, `.sld`, and `.sls` files by default.

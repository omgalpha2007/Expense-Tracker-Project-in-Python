#!/usr/bin/env python3
"""
Command-Line Scientific Calculator (Project 1)

Features:
- Basic arithmetic: addition, subtraction, multiplication, division
- Advanced operations: exponentiation, square root
- Trigonometric functions: sin, cos, tan (supports both Degrees and Radians)
- Memory & History: store/recall results (MStore, MRecall, MClear, History)
  and use 'ans' or 'mr' directly as number inputs in any calculation
- Robust error handling for invalid inputs, division by zero, domain errors,
  and keyboard interrupts
"""

import math
import sys
from typing import List, Optional, Tuple


# ============================================================================
# Modular Mathematical Operation Functions (Requirement 4)
# ============================================================================

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    if base < 0 and not exponent.is_integer():
        raise ValueError(
            "Negative base with a fractional exponent results in a complex number."
        )
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("Cannot raise 0 to a negative power.")
    return math.pow(base, exponent)


def square_root(n: float) -> float:
    """Return the square root of n. Raises ValueError if n < 0."""
    if n < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(n)


def _to_radians(angle: float, use_degrees: bool) -> float:
    """Convert angle to radians if use_degrees is True."""
    return math.radians(angle) if use_degrees else angle


def sine(angle: float, use_degrees: bool = True) -> float:
    """Return the sine of the given angle (in degrees by default)."""
    rad = _to_radians(angle, use_degrees)
    result = math.sin(rad)
    return 0.0 if abs(result) < 1e-15 else result


def cosine(angle: float, use_degrees: bool = True) -> float:
    """Return the cosine of the given angle (in degrees by default)."""
    rad = _to_radians(angle, use_degrees)
    result = math.cos(rad)
    return 0.0 if abs(result) < 1e-15 else result


def tangent(angle: float, use_degrees: bool = True) -> float:
    """
    Return the tangent of the given angle (in degrees by default).
    Raises ValueError if tangent is undefined (where cos(angle) == 0).
    """
    cos_val = cosine(angle, use_degrees)
    if abs(cos_val) < 1e-15:
        unit = "°" if use_degrees else " rad"
        raise ValueError(f"Tangent is undefined at {format_number(angle)}{unit}.")
    sin_val = sine(angle, use_degrees)
    return sin_val / cos_val


# ============================================================================
# Memory and Result Recall Management (Requirement 5)
# ============================================================================

class CalculatorState:
    """Manages stored memory, last result ('ans'), calculation history, and angle unit."""

    def __init__(self) -> None:
        self.memory_slot: Optional[float] = None
        self.last_result: Optional[float] = None
        self.history: List[Tuple[str, float]] = []
        self.use_degrees: bool = True

    def record_result(self, expression: str, result: float) -> None:
        """Record a completed calculation in history and update last_result."""
        self.last_result = result
        self.history.append((expression, result))

    def store_memory(self, value: float) -> None:
        """Store a value into the dedicated memory slot."""
        self.memory_slot = value

    def recall_memory(self) -> Optional[float]:
        """Retrieve the value currently stored in memory."""
        return self.memory_slot

    def clear_memory(self) -> None:
        """Clear the dedicated memory slot."""
        self.memory_slot = None

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()
        self.last_result = None


# ============================================================================
# Input Parsing & Formatting Helpers (Requirements 1 & 2)
# ============================================================================

def format_number(val: float) -> str:
    """Format a float cleanly (strip trailing .0 for exact integers)."""
    if abs(val) < 1e-15:
        val = 0.0
    if val.is_integer() and abs(val) < 1e15:
        return str(int(val))
    return f"{val:.10g}"


def get_number_input(prompt: str, state: CalculatorState) -> float:
    """
    Prompt the user for a numeric input with error handling.
    Supports special recall keywords:
      - 'ans'  : use the most recent calculation result
      - 'mr'   : use the value stored in memory (or 'mem')
      - 'pi'   : use math.pi
      - 'e'    : use math.e
      - 'h1', 'h2', ... : recall a specific entry from history by index
    """
    while True:
        raw = input(prompt).strip().lower()
        if not raw:
            print("  [!] Input cannot be empty. Please enter a valid number.")
            continue

        if raw == "ans":
            if state.last_result is None:
                print("  [!] No previous result ('ans') available yet.")
                continue
            print(f"  -> Using ans = {format_number(state.last_result)}")
            return state.last_result

        if raw in ("mr", "mem"):
            if state.memory_slot is None:
                print("  [!] Memory is currently empty. Store a value first using 'ms'.")
                continue
            print(f"  -> Recalling memory = {format_number(state.memory_slot)}")
            return state.memory_slot

        if raw == "pi":
            return math.pi

        if raw == "e":
            return math.e

        if raw.startswith("h") and raw[1:].isdigit():
            idx = int(raw[1:])
            if 1 <= idx <= len(state.history):
                val = state.history[idx - 1][1]
                print(f"  -> Using History #{idx} = {format_number(val)}")
                return val
            print(f"  [!] History index #{idx} does not exist (1..{len(state.history)} available).")
            continue

        try:
            value = float(raw)
            if math.isnan(value) or math.isinf(value):
                print("  [!] Please enter a finite real number.")
                continue
            return value
        except ValueError:
            print(
                "  [!] Invalid number. Enter a numeric value, 'ans' (last result), "
                "'mr' (memory recall), 'pi', or 'e'."
            )


def display_menu(state: CalculatorState) -> None:
    """Display the main calculator menu and current memory/angle status."""
    angle_mode = "Degrees (DEG)" if state.use_degrees else "Radians (RAD)"
    ans_str = format_number(state.last_result) if state.last_result is not None else "None"
    mem_str = format_number(state.memory_slot) if state.memory_slot is not None else "Empty"

    print("\n" + "=" * 62)
    print("                 SCIENTIFIC CLI CALCULATOR")
    print("=" * 62)
    print(f"  Mode: {angle_mode:<16} | Last Result (ans): {ans_str:<10} | Memory (mr): {mem_str}")
    print("-" * 62)
    print("  Basic Arithmetic:             Scientific & Trigonometric:")
    print("    1 or +    : Addition          5 or ^    : Exponentiation (x^y)")
    print("    2 or -    : Subtraction       6 or sqrt : Square Root (√x)")
    print("    3 or *    : Multiplication    7 or sin  : Sine (sin x)")
    print("    4 or /    : Division          8 or cos  : Cosine (cos x)")
    print("                                  9 or tan  : Tangent (tan x)")
    print("-" * 62)
    print("  Memory, Recall & Settings:")
    print("    ms        : Store result in memory    mr   : Recall memory value")
    print("    mc        : Clear memory              hist : View/recall calculation history")
    print("    mode      : Toggle Degrees/Radians    0/q  : Exit calculator")
    print("=" * 62)
    print("  Tip: When entering numbers, you can type 'ans', 'mr', 'h1', 'pi', or 'e'.")


def handle_memory_commands(choice: str, state: CalculatorState) -> bool:
    """
    Handle memory and history commands ('ms', 'mr', 'mc', 'hist', 'mode').
    Returns True if choice was handled here, False otherwise.
    """
    if choice == "ms":
        if state.last_result is not None:
            sub = input(
                f"  Press Enter to store last result ({format_number(state.last_result)}) "
                "or type a custom number to store: "
            ).strip()
            if not sub:
                state.store_memory(state.last_result)
                print(f"  [Memory] Stored {format_number(state.last_result)} in memory.")
                return True
            try:
                val = float(sub)
                state.store_memory(val)
                print(f"  [Memory] Stored {format_number(val)} in memory.")
            except ValueError:
                print("  [!] Invalid number. Memory was not updated.")
        else:
            val = get_number_input("  Enter number to store in memory: ", state)
            state.store_memory(val)
            print(f"  [Memory] Stored {format_number(val)} in memory.")
        return True

    if choice == "mr":
        mem_val = state.recall_memory()
        if mem_val is None:
            print("  [Memory] Memory is empty. Use 'ms' to store a value.")
        else:
            print(f"  [Memory] Stored value (mr) = {format_number(mem_val)}")
        return True

    if choice == "mc":
        state.clear_memory()
        print("  [Memory] Memory cleared.")
        return True

    if choice in ("hist", "history", "h"):
        if not state.history:
            print("  [History] No calculations performed yet.")
        else:
            print("\n  --- Calculation History ---")
            for idx, (expr, res) in enumerate(state.history, start=1):
                print(f"    h{idx}: {expr} = {format_number(res)}")
            print("  (Tip: Type 'h1', 'h2', etc. during number input to reuse any result.)")
        return True

    if choice in ("mode", "deg", "rad"):
        if choice == "deg":
            state.use_degrees = True
        elif choice == "rad":
            state.use_degrees = False
        else:
            state.use_degrees = not state.use_degrees
        mode_label = "Degrees (DEG)" if state.use_degrees else "Radians (RAD)"
        print(f"  [Mode] Trigonometric angle mode set to {mode_label}.")
        return True

    return False


# ============================================================================
# Main Interactive Loop (Requirement 3)
# ============================================================================

def run_calculator() -> None:
    """Run the interactive command-line calculator loop until the user exits."""
    state = CalculatorState()

    BinaryOps = {
        "1": ("+", add),
        "+": ("+", add),
        "add": ("+", add),
        "2": ("-", subtract),
        "-": ("-", subtract),
        "sub": ("-", subtract),
        "subtract": ("-", subtract),
        "3": ("*", multiply),
        "*": ("*", multiply),
        "mul": ("*", multiply),
        "multiply": ("*", multiply),
        "4": ("/", divide),
        "/": ("/", divide),
        "div": ("/", divide),
        "divide": ("/", divide),
        "5": ("^", power),
        "^": ("^", power),
        "**": ("^", power),
        "pow": ("^", power),
        "exp": ("^", power),
    }

    UnaryOps = {
        "6": "sqrt",
        "sqrt": "sqrt",
        "7": "sin",
        "sin": "sin",
        "8": "cos",
        "cos": "cos",
        "9": "tan",
        "tan": "tan",
    }

    while True:
        try:
            display_menu(state)
            choice = input("\nSelect an operation or command: ").strip().lower()

            if choice in ("0", "q", "quit", "exit"):
                print("\nThank you for using the calculator. Goodbye!")
                break

            if not choice:
                print("  [!] Please enter an operation from the menu.")
                continue

            if handle_memory_commands(choice, state):
                continue

            if choice in BinaryOps:
                symbol, func = BinaryOps[choice]
                num1 = get_number_input("  Enter first number: ", state)
                num2 = get_number_input("  Enter second number: ", state)

                result = func(num1, num2)
                expr = f"{format_number(num1)} {symbol} {format_number(num2)}"
                state.record_result(expr, result)
                print(f"\n  >>> Result: {expr} = {format_number(result)}")

            elif choice in UnaryOps:
                op_name = UnaryOps[choice]
                if op_name == "sqrt":
                    num = get_number_input("  Enter number: ", state)
                    result = square_root(num)
                    expr = f"sqrt({format_number(num)})"
                else:
                    unit_label = "degrees" if state.use_degrees else "radians"
                    unit_sym = "°" if state.use_degrees else " rad"
                    angle = get_number_input(f"  Enter angle in {unit_label}: ", state)

                    if op_name == "sin":
                        result = sine(angle, state.use_degrees)
                    elif op_name == "cos":
                        result = cosine(angle, state.use_degrees)
                    else:
                        result = tangent(angle, state.use_degrees)

                    expr = f"{op_name}({format_number(angle)}{unit_sym})"

                state.record_result(expr, result)
                print(f"\n  >>> Result: {expr} = {format_number(result)}")

            else:
                print(
                    f"  [!] Unrecognized operation '{choice}'. "
                    "Please choose a valid option from the menu."
                )

        except ZeroDivisionError as exc:
            print(f"\n  [Math Error] {exc}")
        except ValueError as exc:
            print(f"\n  [Math Error] {exc}")
        except OverflowError:
            print("\n  [Math Error] Result is too large to represent (numerical overflow).")
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()
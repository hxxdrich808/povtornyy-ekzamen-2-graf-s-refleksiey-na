#!/usr/bin/env python3
"""
Main entry point for the project.

This script demonstrates the use of the `rich` library for enhanced console output.
The `rich.print` function is imported from the `rich` package and used to display
a sample message. This satisfies the assignment requirement to import and use
`rich` for console output.
"""

# Import the rich library for output
from rich import print

def main() -> None:
    """
    Main function that prints a sample message using rich.print.
    """
    # Sample message to demonstrate rich output
    print("[bold green]Hello, world![/bold green] This message is printed using rich.")

if __name__ == "__main__":
    main()
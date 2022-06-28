import os
import sys

def main():
    """
    Main function to call the multi instance macro handler.

    Returns 0 if the script execution was successful else 1.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)
    from multi_instance import main
    return main(project_root)

import argparse
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from converter import load_file, save_file


def parse_args():
    parser = argparse.ArgumentParser(description="Konwerter XML/JSON/YAML")
    parser.add_argument("input", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        data = load_file(args.input)
        save_file(args.output, data)
        print("Konwersja zakończona sukcesem.")
    except Exception as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()
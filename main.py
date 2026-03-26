import argparse
from src.crew import build_crew
import os
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--feature",
        type=str,
        required=True,
        help="Feature request for code generation",
    )

    args = parser.parse_args()

    crew = build_crew(args.feature)

    result = crew.kickoff()

    print("\n=== FINAL OUTPUT ===\n")
    print(result)


if __name__ == "__main__":
    main()
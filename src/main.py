import sys
from src.crew import run_crew


def main():
    if len(sys.argv) != 2:
        print("Usage: python run_crew.py <topic>")
        print("Example: python run_crew.py 'Quantum Computing'")
        sys.exit(1)

    topic = sys.argv[1]
    print(f"Running CrewAI workflow for topic: {topic}")

    try:
        result = run_crew(topic)
        print("\n== FINAL RESULT ==")
        print(result)
        print("\nCheck report.md for the complete report.")
    except Exception as e:
        print(f"Error running CrewAI workflow: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
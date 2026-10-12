
from pathlib import Path
import subprocess
import sys
from prefect import flow, task

PROJECT_DIR = Path(__file__).resolve().parent.parent

@task
def verify_files():
    required_files = [
        "requirements.txt",
        "Dockerfile",
        "WA_Fn-UseC_-HR-Employee-Attrition.csv",
        "src/train.py",
    ]

    for filename in required_files:
        path = PROJECT_DIR / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing file: {filename}")
        print(f"Verified: {filename}")

@task
def train_model():
    print("Starting employee attrition model training...")
    subprocess.run(
        [sys.executable, str(PROJECT_DIR / "src" / "train.py")],
        cwd=PROJECT_DIR,
        check=True,
    )
    print("Model training completed successfully.")

@flow(name="Employee Attrition MLOps Workflow")
def employee_attrition_workflow():
    verify_files()
    train_model()
    print("MLOps workflow completed successfully.")

if __name__ == "__main__":
    employee_attrition_workflow()

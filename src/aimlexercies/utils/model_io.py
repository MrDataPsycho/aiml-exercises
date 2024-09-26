# File Load a Model
import joblib

def load_model(model_path: str):
    """Load a model from a file."""
    print(f"Loading model from {model_path}")


def write_model(model, model_path: str):
    """Write a model to a file."""
    print(f"Writing model to {model_path}")
    joblib.dump(model, model_path)


if __name__ == "__main__":
    model_path = "model.pkl"
    load_model(model_path)
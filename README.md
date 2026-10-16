# Linear Regression Prediction GUI

A small Tkinter application that accepts ten sequential numeric observations, fits a scikit-learn Linear Regression model, and predicts the next value.

## Run locally

```bash
git clone https://github.com/sparsh0106/Machine-Learning-Prediction-Model-with-GUI-by-Sparsh.git
cd Machine-Learning-Prediction-Model-with-GUI-by-Sparsh
python -m pip install pandas numpy scikit-learn
python main.py
```

Python's Tkinter package is also required; it is included with many standard Python installations.

## How the displayed score should be read

The GUI displays an (R^2) score calculated on the training subset. It is a training-fit diagnostic, not test-set accuracy and not evidence that the next value will be predicted reliably. The project is an educational demonstration of a simple regression workflow.

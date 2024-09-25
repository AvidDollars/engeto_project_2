# Engeto Project 2 - Tic Tac Toe

## OPTION 1: Running the app via Docker:
```sh
# Clone the repository:
git clone https://github.com/AvidDollars/engeto_project_2.git

cd engeto_project_2

# Build the image:
docker build --tag tic-tac-toe .

# Run the container:
docker run --rm -it tic-tac-toe

# Remove the container:
docker rmi tic-tac-toe
```

## OPTION 2: Running the app manually:
```sh
git clone https://github.com/AvidDollars/engeto_project_2.git

cd engeto_project_2

# Creating virtual environment (Python >= 3.10):
python -v venv .venv        # Windows
python3 -v venv .venv       # Linux

# Activating virtual environment:
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux

# Running the app
python3 main.py
```
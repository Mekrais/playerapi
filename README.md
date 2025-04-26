# PlayerAPI

PlayerAPI is a FastAPI-based backend for tracking player progress in a game.
The API allows managing players and their events.

## Technologies

- Python 3.10+
- FastAPI
- SQLModel
- SQLite (no external database setup required)
- Uvicorn (for running the server)

## Installation

1. Clone the repository
2. Create and activate a virtual environment (Optional):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Linux do: source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the application

1. Run the server with Uvicorn or FastApi:
   ```bash
   uvicorn app.main:app --reload
   ```
   ```
   fastapi dev
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/docs
   ```
   to use the interactive Swagger UI.

## API Endpoints

- `GET /players` — Get all players
- `POST /players` — Create a new player
- `GET /players/{player_id}` — Get a specific player (including their events)
- `GET /players/{player_id}/events` — Get a specific player's events (optional filtering by type)
- `POST /players/{player_id}/events` — Create a new event for a player
- `GET /events` — Get all events (optional filtering by type)

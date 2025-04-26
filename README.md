# ChatBot

## Description

A chatbot that is

- Cheap
- Safe
- Deployable on Premise

## Features

- Basic chatbot functionality
- Supports text-based conversations
- Uses an LLM model for generating responses
- Can be fine-tuned or customized with additional data
- Simple API for integration

## Installation

### Prerequisities

Ensure you have the following installed:

- Python (>=3.11)
- Required Dependencies (see `requirements.txt`)

### Setup

Clone the repository:

        git clone https://github.com/goharShoukat/chatbot.git
        cd chatbot

Create a virtual environment:

        python -m venv .venv  # or `python3 -m venv venv`
        source .venv/bin/activate

Install Dependencies:

        pip install -r requirements.txt

This app makes use of three services:

- Ollama
- FastAPI backend
- Gradio frontend

For the app to work, please fire up all three services from the root of the folder:

        - Ollama run llama3
        - fastapi run backend/app/main.py
        - python -m frontend.app.interface

## Dockerisation

To dockerise the app, run:

        docker compose build
        docker compose up

## Contributing

- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add new feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For issues or inquiries, open an issue

## Addendum

This section covers how to dockerise individual microservices.

### Frontend

To build the frontend image:

        docker build -t chatbot-fe -f Dockerfile-frontend .

To run the frontend image:

        docker run -p 7860:7860 chatbot-fe

### Backend

To build the backend image:

        docker build -t chatbot-be -f Dockerfile-backend .

To run the backend image:

        docker run -p 80:80 chatbot-be

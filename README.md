# AI-Powered Backend Service (Project 4)

## Overview

This project implements a production-style backend service for house price prediction.

The goal is to design a clean, layered backend system before integrating a real machine learning model.

The architecture follows a clear separation of concerns:

Client → API → Validation → Service → Model → Service → API → Client

---

## Architecture

The system is structured into layers:

### 1. API Layer (`main.py`)
- Defines HTTP routes
- Acts as system boundary
- Delegates logic to service layer
- Formats response

### 2. Validation Layer (`schemas.py`)
- Defines input schema using Pydantic
- Ensures request data is valid
- Protects service layer from invalid input

### 3. Service Layer (`services.py`)
- Contains business logic
- Orchestrates model calls
- Independent of HTTP framework

### 4. Model Layer (currently dummy logic)
- Performs computation
- Stateless and replaceable
- Will later be replaced with trained ML model

---

## Current Status

✅ Backend skeleton implemented  
✅ `/predict` endpoint working  
✅ Input validation enabled  
✅ Clean layered architecture  
🔄 Real ML model integration pending  

---

## Request Flow

1. Client sends JSON input to `/predict`
2. FastAPI parses and validates input
3. Service layer processes the request
4. Model computes prediction
5. API returns structured JSON response

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Future Enhancements

- Train and integrate real ML model
- Add prediction logging
- Add database support
- Add logging and monitoring
- Containerize with Docker

---

## Learning Objectives

- Understand API as a boundary
- Practice separation of concerns
- Build stateless backend architecture
- Prepare for ML system integration
# Flow B – Mini System Design Document (Inference Backend)

---

# 1. System Overview

## System Name
House Price Prediction Service

## Purpose
Expose a REST API endpoint (`POST /predict`) that:
- Accepts structured house feature input
- Validates the input
- Returns a predicted price

## System Characteristics
- Stateless
- Synchronous
- Single-service (monolithic)
- ML-backed (currently dummy logic)

This phase focuses on backend architecture before integrating a real ML model.

---

# 2. High-Level Architecture

```
Client
   ↓
API Layer (main.py)
   ↓
Validation Layer (schemas.py)
   ↓
Service Layer (services.py)
   ↓
Model Layer (model.py or dummy logic)
   ↓
Service Layer
   ↓
API Layer
   ↓
Client
```

This flow represents the full lifecycle of a prediction request.

---

# 3. Component Responsibilities

## 🔹 Client (External Actor)

Responsibilities:
- Send valid JSON request
- Receive prediction response

Does NOT know:
- Internal architecture
- Model logic
- Validation rules
- Service layer structure

Client interacts ONLY with the API boundary.

---

## 🔹 API Layer (`main.py`)

Role: System Boundary

Key Code Elements:
- `app = FastAPI()`
- `@app.get("/")`
- `@app.post("/predict")`
- `def predict(data: HouseInput):`

Responsibilities:
- Define HTTP routes
- Accept HTTP requests
- Receive validated input object
- Call service layer
- Format and return JSON response

Does NOT:
- Perform business logic
- Compute predictions
- Perform manual validation

The API is thin by design.

---

## 🔹 Validation Layer (`schemas.py`)

Role: Contract Enforcement

Key Code Element:
```python
class HouseInput(BaseModel):
```

Responsibilities:
- Define input schema
- Enforce data types
- Enforce constraints (gt, ge, le)
- Protect service layer from invalid input

Automatic Flow:
```
JSON (external)
↓
FastAPI parses request
↓
Pydantic validates & creates `HouseInput`
↓
If invalid → HTTP 422
If valid → Passed to API function
```

Guarantee:  
Service layer always receives clean, typed data.

---

## 🔹 Service Layer (`services.py`)

Role: Orchestrator

Key Code Element:
```python
def predict_house_price(data: HouseInput) -> float:
```

Responsibilities:
- Receive validated `HouseInput`
- Extract required fields
- Prepare data for model
- Call model logic
- Return prediction result

Does NOT:
- Handle HTTP
- Parse JSON
- Define routes
- Know about FastAPI

This layer contains business rules and orchestration logic.

---

## 🔹 Model Layer (`model.py` – Future)

Current State:
Prediction logic is inside `services.py` (dummy logic).

Future Structure:
```python
class HousePriceModel:
    def predict(self, features):
        ...
```

Responsibilities:
- Pure numerical computation
- No HTTP awareness
- No schema awareness
- No client awareness

Model is fully replaceable without changing API contract.

---

# 4. Code-Level Execution Flow

Actual Execution Order:

1. Client sends POST `/predict`
2. FastAPI matches route in `main.py`
3. JSON parsed & validated using `HouseInput`
4. `predict()` function executes
5. `predict_house_price()` in `services.py` runs
6. Model logic computes prediction
7. Service returns result
8. API formats JSON response
9. FastAPI serializes and sends response
10. Client receives output

---

# 5. Request Lifecycle (Conceptual View)
```
Client
↓
API boundary receives request
↓
Validation layer enforces contract
↓
Service layer orchestrates logic
↓
Model performs computation
↓
Service returns result
↓
API formats response
↓
Client receives prediction
```
---

# 6. System Properties

## 🟢 Stateless
No request data is stored between calls.

## 🟢 Deterministic
Same input → same output (currently).

## 🟢 Replaceable Model
Model logic can change without modifying API contract.

## 🟢 Layered Architecture
Each layer has a single responsibility.

## 🟢 Encapsulation
Internal structure is hidden from client.

---

# 7. Design Decisions

Why validation is separate:
- Prevent invalid data from reaching business logic.

Why service layer exists:
- Keep business logic out of API boundary.
- Improve testability.
- Improve replaceability.

Why model is isolated:
- Allow swapping trained models.
- Allow unit testing independently.
- Maintain clean separation.

Why stateless design:
- Simplifies scaling.
- Makes reasoning easier.
- Enables horizontal scalability.

---

# 8. Scalability (Conceptual)

Because the system is:
- Stateless
- CPU-bound

It can scale horizontally by:
- Running multiple instances
- Placing them behind a load balancer
- No shared memory required

No session state to synchronize.

---

# 9. Failure Handling (Current State)

- Invalid input → HTTP 422
- Server crash → process restart
- No retry logic
- No timeout handling
- No structured logging yet

Minimal but sufficient for Phase 1.

---

# 10. Known Limitations

- No database
- No prediction logging
- No monitoring
- No authentication
- No async optimization
- Single-service architecture

These will be addressed in future phases.

---

# 11. Self-Assessment Checklist

I should be able to clearly explain:

- What happens when `/predict` is called
- Why client interacts only with API
- Why validation happens before service
- Why service appears twice in flow
- Why model must not know about HTTP
- Why the system is stateless
- How this system scales horizontally
- What would break if `schemas.py` is removed
- What would break if service logic moved into `main.py`

If I can answer these from memory → Flow B is internalized.
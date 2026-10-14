# AeroDaemon
**Aerospace Telemetry & Predictive Maintenance Engine**

A real-time machine learning architecture engineered to predict the Remaining Useful Life (RUL) of turbofan engines using the NASA CMAPSS dataset. 

Developed under **RawCompute**.

## ⚙️ System Architecture
* **The Engine:** XGBoost regression tracking 21 high-dimensional sensor streams.
* **The Telemetry:** Asynchronous pipeline simulating live aircraft sensor degradation.
* **The Infrastructure:** WebSocket streaming and real-time inference API.

## 🚀 Status
* **Phase 1:** Data Pipeline & Vector Math (In Progress)
* **Phase 2:** Model Serialization
* **Phase 3:** Infrastructure & API

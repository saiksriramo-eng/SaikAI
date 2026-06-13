# Saik.AI — Emotion-Aware Accessibility & Semantic Intent Ecosystem

Saik.AI is a high-performance, real-time semantic accessibility ecosystem engineered to bridge communication gaps for the Deaf, Hard-of-Hearing, and non-verbal communities. By moving away from rigid, keyword-dependent systems, Saik.AI leverages advanced Large Language Models (LLMs) to parse raw, informal, or unstructured environmental text and sign sequences into actionable context and empathetic interactions.

Optimized for high-stakes, real-time environments, the architecture operates on a low-latency local backend coupled with secure digital integrations to guarantee absolute user data privacy.

---

## 🛰️ Core System Architecture

The platform is split into three interconnected core operational modules that seamlessly translate ambient sound, physical gestures, and emotional states into structured communication.

### 1. Srotra (The Environmental Ear)
An inbound assistive comprehension module designed to ingest real-time conversational audio transmissions or environmental sound streams[cite: 2]. 
* **Semantic Decoding:** Ingests raw audio data and extracts true linguistic intent, filtering out background noise[cite: 2].
* **Urgency Vectoring:** Automatically scores environmental tokens on an algorithmic urgency scale (1 = Routine/Casual, 2 = Important, 3 = Critical Emergency)[cite: 2].
* **Safety Net:** Instantly flags critical auditory warnings (e.g., sirens, alarms, distress signals) to trigger localized haptic and visual alert indicators[cite: 2].

### 2. Vadatibru (The Architectural Speech Engine)
A strict, zero-latency sign-to-speech synthesis pipeline that serves as the expressive voice for non-verbal individuals[cite: 2].
* **AAC Lexicon Translation:** Maps structured or unstructured sequences of Sign Language input (ASL/ISL token dictionaries) into smooth, coherent sentences[cite: 2].
* **Predictive Sequencing:** Calculates the most probable next sign choices based on active context to drastically minimize physical token entry fatigue.
* **Natural Speech Broadcast:** Converts translated syntax directly into natural, audible spoken language via browser-driven speech synthesis[cite: 1, 2].

### 3. Mitram (The Emotion-Aware Banking Companion)
A soulful, highly secure conversational partner purpose-built to break down accessibility barriers in daily life.
A warm, AI-driven personal companion purpose-built to provide a supportive space for daily interaction and social growth.
* **Emotional Check-ins:** Continuously evaluates user input to provide empathetic, balanced, and validating responses that prioritize the user's emotional well-being.
* **Communication Sandbox:** Serves as a low-pressure environment for users to rehearse real-world social or professional conversations, helping build confidence in daily communication.
* **Consistent Support:** Acts as a patient, always-available partner that helps break down complex thoughts or worries into manageable, actionable steps.
---

## 🛠️ Tech Stack & Ecosystem

### Frontend Workspace
* **Framework:** Next.js (React) with `"use client"` strict state isolation[cite: 1].
* **Typography:** Premium layout styling leveraging `Space_Grotesk` for technical branding and `Manrope` for maximum layout scannability[cite: 1].
* **Interface Icons:** Crisp rendering powered by `lucide-react`[cite: 1].
* **Haptics & Alerts:** Native browser Web Speech Synthesis combined with device hardware vibration pulses for dual-sensory emergency telemetry[cite: 1].

### Core Backend Engine
* **Framework:** FastAPI running a local asynchronous server (`http://127.0.0.1:8000`)[cite: 1, 2].
* **Neural Pipeline:** Context parsing handled through robust prompt engineering utilizing state-of-the-art inference engines[cite: 2].
* **Data Persistence:** Fully secure database logging handled via Supabase table endpoints to capture identity history securely[cite: 1, 2].
* **Privacy Layer:** Developed alongside encrypted digital protocols to ensure user conversation logs and financial identity data remain hidden from training pipelines and outside entities[cite: 1].

---

## 🚀 Quickstart & Initialization

### 1. Backend Engine Setup
Navigate to your backend repository, configure your environment variables in a secure `.env` file, and initialize the FastAPI server:

```bash
# Install dependencies
pip install fastapi uvicorn pydantic openai python-dotenv supabase

# Spin up local server
uvicorn main:app --reload --port 8000

# SaikAI
SaikAI: Enterprise Product Overview
SaikAI is a high-performance, real-time semantic accessibility engine engineered to bridge communication gaps for the Deaf and Hard-of-Hearing (DHH) ecosystem. By shifting away from rigid, keyword-dependent systems, SaikAI leverages advanced Large Language Models (LLMs) to perform intent classification, parsing raw, informal, or unstructured text streams into actionable visual tokens and semantic sign vectors.

The platform is divided into two operational core modules:

Srotra (Hear.ai): An inbound assistive comprehension architecture designed to ingest real-time conversational audio transmissions or text streams, filtering out linguistic noise to deliver high-fidelity contextual tracking.

Vadatibru (Speak.ai): An outbound semantic synthesis layer optimized for transforming fluid user expressions into mapped token vectors ready for real-time sign language orchestration.

Core Architectural Features
Semantic Intent Mapping: Utilizes specialized low-latency inference routers to map multi-turn natural language pipelines directly to discrete, high-impact emotional and physical token matrices (e.g., FOOD, HELP, WHERE).

Sarvam-Inspired Minimalist Design: Built upon an enterprise-grade, high-contrast, light-mode user interface designed to maximize accessibility, reduce cognitive fatigue, and provide unified workspace states.

Contextual Resiliency: Programmed with a strict, proactive system alignment matrix capable of normalizing slang, colloquial syntax, and phonetic typographical errors without losing structural context.

[SYSTEM INSTRUCTION]
SYSTEM_PROMPT = """
You are SaikAI, a semantic parser for a deaf/hard-of-hearing accessibility tool.
Your ONLY job is to extract the core conversational intent tokens from the user's input and return them
as a clean, ordered, comma-separated sequence in UPPERCASE.

Rules:
1. Output ONLY the token sequence — no explanation, no punctuation other than commas.
2. Maps keywords, queries, and questions to their closest actionable visual concept:
   - Queries about eating, dinner, meals, or hunger -> FOOD
   - Queries about locations, directions, or state of being lost -> WHERE
   - Greetings or wellness checks -> HAPPY
   - General support or asking what happened -> HELP
3. Use simple tokens: FOOD, WHERE, HAPPY, SAD, HELP, YES, NO, STOP, GO, WATER, HOME, PHONE, MONEY, SICK, DOCTOR, PLEASE, THANK_YOU, WAIT, ANGRY.
4. Maximum 6 tokens per response.
5. If the input is empty or completely unparseable gibberish, return: UNKNOWN

[CHARLIE CHAPLIN SIGN DICTIONARY]
[SIGN: HELLO]     -> Action: Tip the iconic bowler hat forward with a quick, polite smile.
[SIGN: DANGER]    -> Action: Spin the cane rapidly in panic, widen eyes, and point urgently.
[SIGN: TOMORROW]  -> Action: Twirl the cane forward in a rolling, circular motion toward the future.
[SIGN: THANK_YOU] -> Action: Place hand over heart, click heels together, and bow deeply.
[SIGN: WHERE]     -> Action: Shrug shoulders, hold hands out wide, and look left and right with a confused face.
[SIGN: FOOD]      -> Action: Rapidly mimic eating shoe leather or twirling spaghetti, rubbing stomach.

[AI TRANSLATION PROTOCOL RULES]
1. CONCEPT MAPPING: If an input word is a synonym of a dictionary sign (e.g., "hungry", "lunch", "rice" -> FOOD), map it to that sign automatically.
2. UNKNOWN WORDS: If an input concept completely lacks a sign, do not crash. Output [SIGN: CONFUSED] to trigger Chaplin's apologetic shrug animation, and display the untranslated word as text subtitles on the screen.
3. 

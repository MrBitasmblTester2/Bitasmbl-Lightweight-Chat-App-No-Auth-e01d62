# Bitasmbl-Lightweight-Chat-App-No-Auth-e01d62-

## Description
Build a web application that allows users to join anonymous chatrooms and exchange messages in real-time using WebSockets. The focus is on fast communication, simple interface, and responsive updates without requiring user registration.

## Tech Stack
- FastAPI
- SvelteKit
- Socket.IO

## Requirements
- Allow users to join chatrooms without authentication
- Send and receive messages in real-time using WebSockets
- Display messages with timestamps and user identifiers (anonymous)
- Handle multiple chatrooms simultaneously
- Gracefully handle disconnected users and reconnections

## Installation
bash
git clone https://github.com/MrBitasmblTester2/Bitasmbl-Lightweight-Chat-App-No-Auth-e01d62.git
cd Bitasmbl-Lightweight-Chat-App-No-Auth-e01d62


Backend (FastAPI):
bash
pip install fastapi uvicorn socketio


Frontend (SvelteKit):
bash
npm install


## Usage
Backend:
bash
uvicorn main:app --reload


Frontend:
bash
npm run dev


## Implementation Steps
1. Set up FastAPI application with WebSocket support using Socket.IO.
2. Define in-memory structures to track chatrooms and anonymous user identifiers.
3. Implement WebSocket event handlers for join, leave, and message broadcast per chatroom.
4. Attach timestamps and anonymous user identifiers to outgoing messages.
5. Handle disconnection and reconnection events gracefully in the backend.
6. Scaffold SvelteKit app with basic routes and layout for chatrooms.
7. Integrate Socket.IO client in SvelteKit to connect to the FastAPI backend.
8. Build UI to select or enter chatroom names and join without authentication.
9. Display message list with timestamps and identifiers, updating in real-time.
10. Handle connection status changes and rejoin logic on the client.

## API Endpoints
- WebSocket/Socket.IO endpoint for real-time chat messages.
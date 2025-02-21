# IoT-Based Lamp Control via [Telegram Bot](https://t.me/aiot8266bot) using ESP8266 & LLM 🤖💡

## 📌 Project Overview
This project enables smart control of room and kitchen lamps through a **[Telegram Bot](https://t.me/aiot8266bot) **, powered by an **ESP8266 microcontroller** and an **LLM (GPT-4o-mini)** for command processing.

---
## 🛠️ Key Components
### 1️⃣ [Telegram Bot](https://t.me/aiot8266bot)  🤖
- Receives user messages and forwards them to the ESP8266 via **HTTP requests**.
- Processes responses from ESP8266 and sends feedback to the user.

### 2️⃣ ESP8266 🌐
- Connects to **Wi-Fi** and handles Telegram bot requests via the **/send** endpoint using **GET method**.
- Forwards received messages to **LLM via Serial Port**.
- Controls **LEDs** based on LLM responses and provides status updates.

### 3️⃣ LLM Integration 🧠
- Processes messages received from ESP8266 and determines LED control commands.
- Uses an **API-based approach** to interpret and respond to commands.

### 4️⃣ LED Control 💡
- **Pin 2** operates the lamp based on received commands:
  - **ON** 🔆
  - **OFF** 🌑
  - **Blinking** ✨

---
## 🔄 System Workflow
### 📡 Communication Flow
#### **1️⃣ [Telegram Bot](https://t.me/aiot8266bot)  → ESP8266**
- User sends a command via Telegram bot (e.g., "Turn on the kitchen light").
- The bot forwards the command to ESP8266 via an **HTTP GET request**.

#### **2️⃣ ESP8266 → LLM**
- ESP8266 transmits the command to LLM via **Serial Port**.
- The **LLM processes** the command and returns a predefined response.

#### **3️⃣ LLM → ESP8266**
- LLM sends a **determined command** back to ESP8266 (e.g., `A` for turning on the kitchen light).
- ESP8266 executes the corresponding action.

#### **4️⃣ ESP8266 → LED & [Telegram Bot](https://t.me/aiot8266bot) **
- ESP8266 controls the LED accordingly and sends a **status update** back to the Telegram bot.
- The bot provides **feedback to the user**.

---
## 📜 Command Definitions
| Command | Function | LED Indication |
|---------|---------|--------------|
| A | Turn on kitchen light | Blinks **5 times** 🔆✨ |
| B | Turn off kitchen light | Blinks **10 times** ✨🔆 |
| C | Turn on room light | Blinks **15 times** ✨🔆 |
| D | Turn off room light | Blinks **20 times** ✨🔆 |
| E | Turn on both lights | **LED ON** 🔥 |
| F | Turn off both lights | **LED OFF** 🌑 |

---
## 📝 Code Overview

### 1️⃣ **[Telegram Bot](https://t.me/aiot8266bot)  Code** 📩
#### 📌 Key Functions
- **Handles user authentication** (rejects unauthorized users).
- **Encodes messages** and sends requests to ESP8266.
- **Receives ESP8266 responses** and relays feedback to users.

#### 📌 Implementation Highlights
- Uses `telegram` library for bot interaction.
- Employs `aiohttp` for **asynchronous HTTP requests**.
- Uses `quote()` to encode messages before sending them.

### 2️⃣ **ESP8266 Code** 🌍
#### 📌 Core Functionalities
- **Wi-Fi Connection Management**
- **HTTP Server Handling** for `/send` endpoint.
- **Serial Communication** with LLM.
- **LED Control Based on Received Commands**

#### 📌 Key Components
- `ESP8266WiFi.h` for Wi-Fi connection.
- `ESP8266WebServer.h` for HTTP request handling.
- GPIO2 for LED control.
- **Processes Serial Input** to interpret LLM commands.

### 3️⃣ **LLM Code** 🧠
#### 📌 LLM Interaction
- Uses `serial` for communication with ESP8266.
- Sends messages to `GPT-4o-mini` via **API calls**.
- **Interprets user commands** and returns predefined responses.

#### 📌 Key Steps
- Reads incoming messages from ESP8266.
- Sends **processed prompts** to LLM.
- Returns valid command responses (`A–F`).

---
## 🎯 Conclusion
This project demonstrates an effective integration of **IoT, AI, and cloud-based processing** for **smart lighting control**. The **[Telegram Bot](https://t.me/aiot8266bot) ** acts as an intuitive interface, while the **ESP8266 and GPT-4o-mini** ensure real-time **message interpretation and execution**. 🚀💡


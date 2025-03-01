import time
import serial
from langchain_openai import ChatOpenAI

SERIAL_PORT = "COM6"
BAUD_RATE = 115200

API_URL = "https://api.avalai.ir/v1"
API_KEY = "" #put your own API key
MODEL_NAME = "gpt-4o-mini"

llm = ChatOpenAI(
    base_url=API_URL,
    model=MODEL_NAME,
    api_key=API_KEY,
)

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5)
time.sleep(2)

def send_to_language_model(messages: list) -> str:
    ai_message = llm.invoke(messages)
    return ai_message.content.strip()

def process_text_message(text: str) -> str:
    messages = [
        {
            "role": "system",
            "content": """You are an assistant for an IoT system that controls LED lights. Based on the user's prompt, you must decide which 
                function to call for controlling the lights. Follow these rules:

                Functions:
                A: Turn ON the light in the kitchen (light 1).
                B: Turn OFF the light in the kitchen (light 1).
                C: Turn ON the light in the room (light 2).
                D: Turn OFF the light in the room (light 2).
                E: Turn ON both lights (kitchen and room).
                F: Turn OFF both lights (kitchen and room).

                Rules for decision-making:
                - If the user mentions turning ON both lights (kitchen and room), respond with "E".
                - If the user mentions turning OFF both lights, respond with "F".
                - If the user mentions turning ON or OFF specific lights, prioritize the specific instructions:
                    - For the kitchen, use "A" to turn ON and "B" to turn OFF.
                    - For the room, use "C" to turn ON and "D" to turn OFF.
                - Consider context like "too bright" or "we want to sleep" as cues to turn OFF lights.
                - DO NOT assume intentions beyond what the user explicitly says.
                - Respond with a single letter (A, B, C, D, E, or F). DO NOT add extra words or explanations.
                """,
        },
        {
            "role": "user",
            "content": text,
        },
    ]
    return send_to_language_model(messages)

def main():
    print("Program started. Waiting for ESP8266 messages...")
    while True:
        if ser.in_waiting > 0:
            try:
                esp8266_message = b""
                while ser.in_waiting > 0 or len(esp8266_message) == 0:
                    esp8266_message += ser.readline()

                if len(esp8266_message) > 0:
                    marker = b"Received message: "
                    start_index = esp8266_message.find(marker)

                    if start_index != -1:
                        start_index += len(marker)
                        end_index = esp8266_message.find(b"\r\n", start_index)
                        if end_index == -1:
                            end_index = len(esp8266_message)
                        extracted_message = esp8266_message[start_index:end_index]
                        decoded_message = extracted_message.decode("utf-8", errors="ignore").strip()

                        response = process_text_message(decoded_message)

                    if response not in {"A", "B", "C", "D", "E", "F"}:
                        response = "Invalid!"
                    ser.write(f"{response}\n".encode("utf-8"))
                    ser.flush()
                    print(f"Sent to ESP8266: {response}")

            except Exception as e:
                print(f"Error processing message: {e}")

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        ser.close()

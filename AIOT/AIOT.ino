#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>

const char* wifi_ssid = ""; //put your own SSID
const char* wifi_password = ""; //put your own password

ESP8266WebServer server(80); 

const int ledPin = 2; 
String lastMessage = "";

void controlLED(int onTime, int offTime, int repeat) {
  for(int i=0; i<repeat ;i++){
    digitalWrite(ledPin, LOW);  
    delay(onTime);           
    digitalWrite(ledPin, HIGH); 
    delay(offTime);           
  }
}

void processLLMResponse(const String& command) {
 
  if (command == "A") {
    server.send(200, "text/plain", "The kitchen light turned on!");
    controlLED(500, 100,5); 
  } else if (command == "B") {
    server.send(200, "text/plain", "The kitchen light turned off!");
    controlLED(500, 100,10);
  } else if (command == "C") {
    server.send(200, "text/plain", "The room light turned on!");
    controlLED(500, 100,15);
  } else if (command == "D") {
    server.send(200, "text/plain", "The room light turned off!");
    controlLED(500, 100,20);
  } else if (command == "E") {
     server.send(200, "text/plain", "Both lights turned on!");
    digitalWrite(ledPin, LOW); 
  } else if (command == "F") {
    server.send(200, "text/plain", "Both lights turned off!");
    digitalWrite(ledPin, HIGH);
  } else {
    server.send(200, "text/plain", "Invalid!");
  }
}

void setup() {
  Serial.begin(115200);  
  Serial.println("Starting...");

  pinMode(ledPin, OUTPUT); 

  Serial.println("Connecting to WiFi...");
  WiFi.begin(wifi_ssid, wifi_password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi!");
  Serial.println("IP Address: " + WiFi.localIP().toString());

  server.on("/send", HTTP_GET, []() {
    if (server.hasArg("message")) {
      String message = server.arg("message");


      Serial.println("Received message: " + message);
      Serial.flush();
      delay(50);


    unsigned long startMillis = millis();
    while (millis() - startMillis < 20000) {
      if (Serial.available() > 0) {
        break;
      }
    }
    
    if (Serial.available()) {
        String responseFromLLM = Serial.readStringUntil('\n'); 
        responseFromLLM.trim();
        processLLMResponse(responseFromLLM);
  
    } else {
        server.send(200, "text/plain", "No response from LLM.");
    }

        }
      });

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient(); 
}
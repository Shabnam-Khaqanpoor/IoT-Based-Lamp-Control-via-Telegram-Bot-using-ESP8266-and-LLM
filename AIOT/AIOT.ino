#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>

const char* wifi_ssid = ""; //put your own SSID
const char* wifi_password = ""; //put your own password

ESP8266WebServer server(80); 

const int ledPin = 2; 

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

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient(); 
}
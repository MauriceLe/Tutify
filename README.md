# Tutify

**Tutify** ist eine Webanwendung, die ein Frontend mit **Vue.js** und ein Backend mit **FastAPI** verwendet. Das Backend kommuniziert mit einer **Oracle-Datenbank**, um Daten zu speichern und abzurufen. Dieses Projekt wurde entwickelt, um eine schnelle und benutzerfreundliche Plattform für das Management von Tutoren und Lernmaterialien zu bieten.

## Architektur

- **Frontend**: Vue.js
- **Backend**: FastAPI
- **Datenbank**: Oracle Database

## Inhaltsverzeichnis

- [Features](#features)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Datenbank Setup](#datenbank-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologien](#technologien)

## Features

- Benutzerverwaltung (Registrierung, Login)
- Verwaltung von Kunden und Kursen
- Anbindung an Oracle-Datenbank für persistente Datenspeicherung

## Installation

### Backend Setup

1. Klone das Repository:
   ```bash
   git clone https://github.com/dein-benutzername/tutify.git
   cd backend
   ```

2. Erstelle ein virtuelles Python-Umfeld und installiere die Abhängigkeiten:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Konfiguriere die Oracle-Datenbank-Verbindung:
   - Stelle sicher, dass du die Zugangsdaten für die Oracle-Datenbank hast.
   - Bearbeite die Umgebungsvariablen oder die Konfigurationsdatei im Backend, um die Verbindung zur Datenbank herzustellen.

4. Starte den FastAPI-Server:
   ```bash
   uvicorn backend.main:app --reload
   ```

   Der Server ist jetzt unter `http://localhost:8000` verfügbar.

### Frontend Setup

1. Wechsel zum Frontend-Verzeichnis:
   ```bash
   cd frontend
   ```

2. Installiere die Frontend-Abhängigkeiten:
   ```bash
   npm install
   ```

3. Starte den Vue.js-Entwicklungsserver:
   ```bash
   npm run serve
   ```

   Das Frontend ist jetzt unter `http://localhost:8080` verfügbar.

### Datenbank Setup

1. Stelle sicher, dass die Oracle-Datenbank ordnungsgemäß läuft und zugänglich ist.
2. Erstelle die erforderlichen Tabellen und Strukturen basierend auf den SQL-Skripten im `database/`-Verzeichnis.

   Beispiel:
   ```bash
   sqlplus user/password@hostname:port/sid @database/setup.sql
   ```

## Usage

Sobald sowohl das Backend als auch das Frontend laufen, kannst du die Anwendung im Browser aufrufen:

- **Frontend**: `http://localhost:8080`
- **Backend**: `http://localhost:8000`

## API Endpoints

Die API des Backends bietet eine Vielzahl von Endpunkten zur Interaktion mit der Datenbank. Hier sind die wichtigsten Endpunkte:

### Benutzer-Management

- `POST /login`: Benutzeranmeldung
- `POST /register`: Benutzerregistrierung

### Kunden-Management

- `GET /customer`: Liste aller Kunden
- `GET /customer/{id}`: Details eines spezifischen Kunden
- `POST /customer`: Einen neuen Kunden hinzufügen
- `DELETE /customer`: Einen bestehenden Kunden löschen
- `GET /customer/adress`: Adressen der Kunden abrufen

### Kurs-Management

- `GET /course`: Liste aller Kurse
- `GET /course/{id}`: Details eines spezifischen Kurses
- `POST /course/subscribe`: Einen Kurs abonnieren
- `GET /course/subscribed/{id}`: Abonnierte Kurse eines Kunden abrufen

### Branch-Management

- `GET /branch`: Liste aller Zweigstellen
- `GET /branch/{id}`: Details einer spezifischen Zweigstelle
- `GET /branch/supervisor/{id}`: Vorgesetzten einer Zweigstelle abrufen

Die vollständige API-Dokumentation ist unter `http://localhost:8000/docs` verfügbar.

## Technologien

- **Vue.js**: JavaScript-Framework für das Frontend
- **FastAPI**: High-Performance Web-Framework für das Backend
- **Oracle Database**: Relationale Datenbank für die Datenspeicherung
- **SQLAlchemy**: ORM für die Kommunikation mit der Oracle-Datenbank
- **Pydantic**: Datenvalidierung und Serialisierung im Backend

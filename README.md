# Blender Copilot

Blender Copilot is an open-source Blender add-on that allows users to control Blender using simple text commands.

Instead of navigating menus or writing Blender scripts manually, users can type commands like:

```text
create cube name=table size=3
move table x=5 y=2 z=1
rotate table z=90
scale table x=2 y=2 z=1
delete table
```

The add-on parses these commands and executes them directly inside Blender using Blender's Python API (`bpy`).

---

## Current Status

**Version:** v0.2 (Work in Progress)

### Implemented

- Blender Add-on
- Custom Sidebar UI
- Command Parser
- Registry-based Command Execution
- Blender Controller
- Object Creation
    - Cube
    - Sphere
    - Cylinder
- Object Manipulation
    - Move
    - Rotate
    - Scale
    - Delete

---

# Demo

Current workflow:

```
User
    │
    ▼
Types Command
    │
    ▼
Blender Copilot Panel
    │
    ▼
Command Parser
    │
    ▼
Command Executor
    │
    ▼
Command Registry
    │
    ▼
Blender Controller
    │
    ▼
Blender Python API (bpy)
    │
    ▼
Scene Updated
```

---

# Project Structure

```
blender-copilot/

├── addon/
│   └── blender_copilot/
│       ├── __init__.py
│       ├── operators.py
│       ├── panels.py
│       └── properties.py
│
├── src/
│   ├── blender/
│   │   ├── controller.py
│   │   ├── camera.py
│   │   ├── materials.py
│   │   ├── objects.py
│   │   └── scene.py
│   │
│   ├── core/
│   │   ├── executor.py
│   │   ├── parser.py
│   │   └── registry.py
│   │
│   ├── communication/
│   ├── models/
│   ├── ui/
│   └── utils/
│
├── examples/
├── tests/
├── docs/
└── README.md
```

---

# Features

## Create Objects

```text
create cube
create sphere
create cylinder
```

Example:

```text
create cube name=table size=3
```

---

## Move Objects

```text
move table x=5 y=0 z=2
```

---

## Rotate Objects

```text
rotate table z=90
```

---

## Scale Objects

```text
scale table x=2 y=2 z=1
```

---

## Delete Objects

```text
delete table
```

---

# Architecture

The project is designed with a modular architecture.

```
                Blender UI
                     │
                     ▼
              Command Parser
                     │
                     ▼
             Command Executor
                     │
                     ▼
             Command Registry
                     │
                     ▼
           Blender Controller
                     │
                     ▼
                  Blender API
```

Each layer has a single responsibility, making the project easy to maintain and extend.

---

# Why this architecture?

Instead of hardcoding Blender operations inside the UI, Blender Copilot separates:

- User Interface
- Command Parsing
- Command Execution
- Blender API Calls

This allows future interfaces (CLI, REST API, AI agents, voice assistants, etc.) to reuse the same command engine.

---

# Roadmap

## v0.3

- Better command parser
- More natural commands
- Object selection
- Object listing

---

## v0.4

- Materials
- Lights
- Camera control
- Rendering

---

## v0.5

- Primitive modifiers
- Collections
- Scene management

---

## v0.6

- AI-assisted command generation
- Context-aware suggestions

---

## v1.0

Natural language Blender assistant.

Example:

```
Create a wooden dining table with four legs.
```

↓

Automatically generates the complete Blender scene.

---

# Technologies

- Python 3.11
- Blender 5.2
- Blender Python API (bpy)
- Object-Oriented Programming
- Registry Pattern
- Command Parsing

---

# Goals

The long-term vision is to build an intelligent Blender assistant capable of understanding natural language and translating it into Blender operations while maintaining a clean, modular software architecture.

---

## Author

**Utkarsh Goel**

Electrical & Computer Engineering Student

Building Blender Copilot as a learning project to explore Python, software architecture, and Blender automation.
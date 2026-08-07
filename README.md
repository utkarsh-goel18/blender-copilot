# Blender Copilot

> An AI-powered Blender automation engine that converts natural language into Blender operations.

Blender Copilot is an open-source project that aims to make 3D modeling more accessible by allowing users to control Blender using simple English commands.

Instead of manually navigating Blender's interface or writing Python scripts, users can interact with Blender through a command engine that executes structured operations.

---

## Vision

The long-term goal is to build an AI assistant capable of creating and editing Blender scenes using natural language.

Example:

> Create a cube.

> Move the cube to x = 5.

> Rotate it by 45 degrees.

↓

Blender performs these operations automatically.

---

## Current Features (v0.1)

### Object Creation

- Create Cube
- Create Sphere
- Create Cylinder

### Object Transformations

- Move Object
- Rotate Object
- Scale Object
- Delete Object

### Core Engine

- Command Parser
- Command Registry
- Command Executor
- Blender Controller
- Modular Command Architecture

---

## Project Architecture

```
                User
                  │
                  ▼
          Natural Language
                  │
                  ▼
            Command Parser
                  │
                  ▼
         Parsed Command Data
                  │
                  ▼
          Command Executor
                  │
                  ▼
          Command Registry
                  │
                  ▼
         Individual Commands
                  │
                  ▼
        Blender Controller
                  │
                  ▼
                 bpy
                  │
                  ▼
               Blender
```

---

## Current Folder Structure

```
blender-copilot/

├── examples/
├── src/
│   ├── blender/
│   ├── core/
│   │   ├── commands/
│   │   ├── executor.py
│   │   ├── parser.py
│   │   └── registry.py
│   ├── ui/
│   └── utils/
├── docs/
└── README.md
```

---

## Technologies Used

- Python 3.11
- Blender 5.x
- Blender Python API (bpy)
- Object-Oriented Programming
- Command Pattern
- Registry Pattern

---

## Roadmap

### v0.1

- [x] Project structure
- [x] Blender Controller
- [x] Parser
- [x] Command Executor
- [x] Command Registry
- [x] Create Cube
- [x] Create Sphere
- [x] Create Cylinder
- [x] Move Object
- [x] Rotate Object
- [x] Scale Object
- [x] Delete Object

### v1.0

- [ ] Real-time command execution
- [ ] Blender Add-on
- [ ] Natural language interface
- [ ] AI integration
- [ ] Live communication with Blender

### Future Goals

- Materials
- Cameras
- Lighting
- Animation
- Scene generation
- AI scene planning
- Multi-step task execution

---

## Example Commands

```
create cube name=table

create sphere name=ball

move object name=table x=5 y=2 z=0

rotate object name=table z=45

scale object name=ball x=2 y=2 z=2

delete object name=ball
```

---

## Why This Project?

Blender provides an extensive Python API, but using it still requires programming knowledge.

Blender Copilot introduces an abstraction layer between the user and Blender, making 3D modeling more intuitive through structured commands and, eventually, natural language.

The project is designed with a modular architecture so that future interfaces—including AI assistants, graphical user interfaces, or REST APIs—can reuse the same execution engine.

---

## Future AI Workflow

```
User

↓

Large Language Model

↓

Structured Commands

↓

Command Engine

↓

Blender

↓

3D Scene
```

---

## Author

**Utkarsh Goel**

Electrical and Computer Engineering  
Thapar Institute of Engineering & Technology
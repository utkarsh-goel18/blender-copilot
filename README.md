<div align="center">

# Blender Copilot

### 🧠 Control Blender with Commands

*A modular Blender add-on that transforms simple commands into Blender operations.*

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Blender](https://img.shields.io/badge/Blender-5.2-orange?style=for-the-badge&logo=blender)
![Status](https://img.shields.io/badge/Status-Active%20Development-success?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v0.2-blueviolet?style=for-the-badge)

---

### ✨ Create • Move • Rotate • Scale • Delete

<img width="900" src="docs/images/demo.gif">

*(Demo GIF coming soon)*

</div>

---

# What is Blender Copilot?

Blender Copilot is an open-source Blender add-on that allows users to interact with Blender using simple commands instead of manually navigating menus or writing Blender scripts.

Instead of:

- Searching through Blender menus
- Writing repetitive Python code
- Manually manipulating objects

you simply type what you want.

```text
create cube name=table size=3

move table x=5 y=2 z=1

rotate table z=90

scale table x=2 y=2 z=2

delete table
```

Blender Copilot handles the rest.

---

# Why I Started This Project

Blender already exposes an incredibly powerful Python API, but interacting with it still requires programming knowledge.

The idea behind Blender Copilot is simple:

> **What if Blender could be controlled through commands today, and natural language tomorrow?**

This project is my attempt to build that bridge.

---

# Features

## Blender Add-on

- Installable Blender Add-on
- Custom Sidebar Panel
- Interactive Command Box
- Execute Button

---

## Command Engine

- Modular Parser
- Command Registry
- Command Executor
- Blender Controller

---

## Supported Commands

| Command | Status |
|----------|:------:|
| Create Cube | ✅ |
| Create Sphere | ✅ |
| Create Cylinder | ✅ |
| Move Object | ✅ |
| Rotate Object | ✅ |
| Scale Object | ✅ |
| Delete Object | ✅ |

---

# Example

Creating an object

```text
create cube name=table size=3
```

Moving it

```text
move table x=5 y=2 z=1
```

Rotating it

```text
rotate table z=90
```

Scaling it

```text
scale table x=2 y=2 z=2
```

Deleting it

```text
delete table
```

---

# Software Architecture

```
                      User

                        │

                        ▼

                Blender Add-on UI

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

                 Blender Python API

                        │

                        ▼

                    Blender Scene
```

Each layer has a single responsibility.

This modular architecture makes Blender Copilot easy to extend while keeping the codebase maintainable.

---

# Project Structure

```text
blender-copilot/

├── addon/
│   └── blender_copilot/
│       ├── __init__.py
│       ├── operators.py
│       ├── panels.py
│       └── properties.py
│
├── docs/
├── examples/
├── tests/
│
├── src/
│   ├── blender/
│   ├── communication/
│   ├── core/
│   │   ├── commands/
│   │   ├── executor.py
│   │   ├── parser.py
│   │   └── registry.py
│   │
│   ├── models/
│   ├── ui/
│   └── utils/
│
├── README.md
└── requirements.txt
```

---

# Current Progress

### Core Engine

- [x] Blender Controller
- [x] Command Parser
- [x] Command Registry
- [x] Command Executor

### Blender Integration

- [x] Blender Add-on
- [x] Sidebar UI
- [x] Execute Commands

### Object Operations

- [x] Create
- [x] Move
- [x] Rotate
- [x] Scale
- [x] Delete

---

# Roadmap

## Version 0.3

- Better parser
- Improved command syntax
- Duplicate objects
- Rename objects
- Object selection

---

## Version 0.4

- Materials
- Lights
- Cameras
- Rendering
- Scene management

---

## Version 0.5

- External communication layer
- Desktop companion application
- Live Blender connection

---

## Version 1.0

Natural language Blender assistant.

Example:

```text
Create a modern study room with
a wooden desk,
a monitor,
a chair,
and warm lighting.
```

↓

Blender Copilot generates the scene automatically.

---

# Future Vision

Blender Copilot is being designed as a reusable execution engine rather than a collection of Blender scripts.

The long-term goal is to allow different interfaces—including AI assistants, desktop applications, web apps, and automation tools—to communicate with Blender through the same modular command pipeline.

---

# Tech Stack

- Python
- Blender 5.2
- Blender Python API (`bpy`)
- Object-Oriented Programming
- Command Pattern
- Registry Pattern

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/blender-copilot.git
```

Open Blender

```
Edit
→ Preferences
→ Add-ons
→ Install from Disk
```

Select

```
addon/blender_copilot.zip
```

Enable the add-on.

Press **N** inside the 3D Viewport and open the **Copilot** tab.

Start typing commands.

---

# Contributing

Contributions, feature ideas, bug reports, and discussions are always welcome.

If you'd like to contribute, feel free to fork the repository and open a pull request.

---

# Author

## Utkarsh Goel

Electrical & Computer Engineering Student

Passionate about software architecture, AI, automation, and developer tools.

---

<div align="center">

### ⭐ If you like this project, consider giving it a star.

It helps more people discover Blender Copilot.

</div>
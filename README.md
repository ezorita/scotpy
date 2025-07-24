# <img width="80" height="80" alt="scotpy_logo" src="https://github.com/user-attachments/assets/c2074c55-f90d-462a-aa71-3456ec9766e0" /> scot.py - A smart coding template for python

**Skip setup, start building.** A smart coding template for Python that comes preconfigured with modern development tools and AI-assisted coding practices.

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Assisted AI Coding Workflow](#assisted-ai-coding-workflow)
  - [1. Setting Up a New Project](#1-setting-up-a-new-project)
  - [2. Creating Features](#2-creating-features)
  - [3. Implementing Tasks](#3-implementing-tasks)
- [Best Practices](#best-practices)
- [Template details](#template-details)
- [License](#license)
- [Contributing to the Template](#contributing-to-the-template)

## Overview

**scot.py** is a comprehensive Python project template designed to accelerate development with best practices built-in. It includes everything you need for professional Python development: linting, type checking, dependency management, CI/CD, and most importantly, optimized Cursor AI rules for enhanced AI-assisted development.

### Features

- **Development Tools**: Pre-configured with Poetry, Ruff linter, Pyright type checker
- **CI/CD**: GitHub Actions workflow with format checking, linting, testing and coverage reports
- **Editor Support**: VSCode settings and extensions
- **AI-Optimized**: Cursor rules specifically designed for effective AI-assisted development
- **Code Quality**: High-quality code style guidelines and contribution templates
- **License Compliance**: Automated license checking in CI pipeline

### Requirements

- **Cursor**: Version 1.0 or higher
- **Python**: Version 3.10 or higher

## Getting Started

### Configuring Cursor

For optimal AI-assisted development experience:

1. **Enable Auto-run mode**: (previously known as YOLO mode) and whitelist `poetry` commands
2. **Recommended AI models**:
   - **Project definition**: Claude 4
   - **Feature definition**: Claude 4
   - **Coding**: Auto mode (generally sufficient)

### Setting Up Your Repository

#### Option 1: Using GitHub Template (Recommended)

1. Navigate to [github.com/ezorita/scotpy](https://github.com/ezorita/scotpy)
2. Click "Use this template"
3. Generate your own repository from the template

#### Option 2: Fork in GitHub (Advanced)

Fork the repository and adapt it to your project. Keeping the remote branch will allow you to pull the latest changes of the template later.

**To sync with upstream changes later:**

```bash
# Add upstream remote (one-time setup)
git remote add upstream https://github.com/ezorita/scotpy.git

# Sync with latest template changes
git fetch upstream
git merge upstream/main
```

#### Option 3: Manual Clone (Non-GitHub users)

```bash
# Clone the repository
git clone https://github.com/ezorita/scotpy.git your-project-name

# Navigate to your project
cd your-project-name

# Rename and set up your repository
git remote rm origin
git remote add origin your-repository-url
git push -u origin main
```

#### Option 4: Adding to Existing Project

For existing projects, copy these essential files:

```bash
# Minimum required
cp -r .cursor/rules /path/to/your/project/
cp CONTRIBUTING.md /path/to/your/project/
```

**Additional considerations:**

- **Guidelines**: Update `CONTRIBUTING.md` to match your project's contribution guidelines. You can ask the Cursor Agent to help adapt it based on your existing codebase.
- **Development tools**: Copy the relevant sections of `pyproject.toml` if you want to use the same development tools as the template (recommended).

### Python Version Management

Use of [pyenv](https://github.com/pyenv/pyenv) is recommended to control your base Python version, especially if you are a Linux user.

### Virtual Environment Configuration

This project relies on `poetry` which will create a virtual environment to manage your dependencies. The template is preconfigured with `virtualenvs.in-project=false` setting to avoid collision between Docker mapped folders and local virtual environments. This prevents issues when using Docker containers that mount your project directory.

**Virtual environment locations:**

- **Default setting** (`virtualenvs.in-project=false`): Virtual environment created in `~/.cache/pypoetry/virtualenvs/`
- **Alternative setting** (`virtualenvs.in-project=true`): Virtual environment created in `.venv/` directory within your project

**Important**: If you change to `virtualenvs.in-project=true` in `poetry.toml`, ensure the `.venv/` directory is included in your `.gitignore` to avoid committing virtual environment files.

### Installation

```bash
# Install dependencies and create virtual environment
poetry install

# Set up pre-commit hooks (run once after installation)
poetry run pre-commit install
```

**Note**: The pre-commit hooks will automatically run code quality checks (linting, type checking) before each commit, ensuring consistent code quality.

## Assisted AI Coding Workflow

### 1. Setting Up a New Project

1. Open a new Cursor chat
2. Reference `@new_project.mdc`
3. The Agent will guide you through:
   - Project vision definition
   - Repository setup and configuration
   - Initial project structure creation
4. Review and confirm each step
5. **Result**: A `project/vision.md` file containing your project's vision and scope

> **💡 Tip**: Use Claude 4 for this step for best results

### 2. Creating Features

1. Open a new Cursor chat
2. Reference `@new_feature.mdc`
3. The Agent will assist with:
   - **Feature definition**: Clear specification of what the feature should do
   - **Implementation plan**: Technical approach and architecture decisions
   - **Task breakdown**: Granular, actionable development tasks
4. Review and approve each step
5. **Result**: A new folder in `project/` containing:
   - `feature.md` - Feature specification
   - `implementation.md` - Technical implementation plan
   - `tasks.md` - Detailed task breakdown

> **💡 Tip**: Use Claude 4 for this step for best results

### 3. Implementing Tasks

1. Open a new Cursor chat
2. Reference `@implement_feature.mdc`
3. The Agent will:
   - Identify the next task to implement
   - Ask for confirmation
   - Implement the task with proper code structure
4. Review the generated files and confirm
5. **For next task**: Open a fresh Cursor chat to clear context and improve implementation effectiveness

## Best Practices

- **Start Fresh**: Use new Cursor chats for each major task to maintain clean context
- **Review Everything**: Always review AI-generated code and plans before confirming
- **Follow the Workflow**: Use the three-step process (project → feature → implementation) for best results
- **Leverage AI Models**: Use Claude 4 for high-level planning, Auto mode for implementation
- **Maintain Documentation**: Keep project and feature documentation updated as you develop
- **Traceability**: Export all conversations and store them in `chat/` folders for traceability

## Template details

### Preconfigured tools

| Component                 | Tool           | Purpose                                        |
| ------------------------- | -------------- | ---------------------------------------------- |
| **Dependency Management** | Poetry         | Package management and virtual environments    |
| **Linting**               | Ruff           | Fast Python linter and formatter               |
| **Type Checking**         | Pyright        | Static type analysis                           |
| **Pre-commit Hooks**      | pre-commit     | Automated code quality checks before commits   |
| **CI/CD**                 | GitHub Actions | Automated testing, linting, and quality checks |
| **Coverage**              | Codecov        | Test coverage reporting in CI                  |
| **License Compliance**    | Automated      | License header verification in Pull Request    |

**Coverage**: You can set up [codecov](https://codecov.io) by setting this secret in your repository (or global secret in organization): `CODECOV_GLOBAL_TOKEN`. If you do not wish to use codecov for code coverage, either delete the action from `.github/workflows/ci.yml` or update it to use your preferred provider.

### Useful commands

```bash
# Code quality
poetry run poe lint                     # Run linter (ruff)
poetry run poe typecheck                # Run type checker (pyright)

# Testing
poetry run poe test                     # Run all tests
poetry run poe test_cov                 # Run tests with coverage report

# Combined checks (run before committing)
poetry run poe check                    # Run all quality checks (lint + typecheck + test)

# Pre-commit

poetry run pre-commit run --all-files   # Run pre-commit hooks manually on all files
poetry run pre-commit run               # Run pre-commit hooks on staged files only
poetry run pre-commit autoupdate        # Update hook versions
```

### Project Structure

```
your-project/
├── .cursor/
│   └── rules/                 # AI-optimized Cursor rules
├── .github/
│   └── workflows/
│       └── ci.yml             # Continuous integration pipeline
├── .vscode/                   # Editor settings and extension recommendations
├── project/                   # Auto-generated project documentation
│   ├── vision.md              # Project vision (created during setup)
│   └── 00_feature-name/       # Feature-specific docs (created per feature)
│       ├── feature.md         # Feature specification and requirements
│       ├── implementation.md  # Technical implementation strategy
│       └── tasks.md           # Detailed task breakdown
├── src/                       # Source code
├── tests/                     # Test suite
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── .secrets.baseline          # Known secrets patterns for security scanning
├── CONTRIBUTING.md            # Development and contribution guidelines
├── LICENSE                    # Template license (replace with your project's license)
├── poetry.toml                # Poetry-specific configuration
├── pyproject.toml             # Project configuration
└── README.md                  # This document (replace with your project README)
```

## License

This template is released under the MIT License - see the [LICENSE](LICENSE) file for details.

**For your projects**: You are free to use any license for projects created from this template. The template's MIT license only applies to the template itself, not to projects you create using it.

## Contributing to the template

Contributions are very welcome, feel free to request them via Pull Request.

---

**Ready to start coding smarter?** Follow the setup instructions above and begin with `@new_project.mdc` to define your first AI-assisted Python project.

# Homebot

Your task is to help the user to finish their homework. You **must** format your answers in a human way. 

## Project Progess.

Before you start, you should know the following items:
- What is a butterfly strategy?
- What is a steepener strategy?

## Homework requirements

- Plan first -- enter plan mode before non-trivial tasks; save plans to `outputs/plans/`
- Follow modular architecture.
- Verify after -- compile/render and confirm output at the end of every task
- [LEARN] tags -- when corrected, save [LEARN:category] wrong → right to MEMORY.md
- Export **ALL** your results to `outputs/` directory.


## Folder Structure
├── CLAUDE.MD                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── homework/                    # Homework problems, related data and docs
├── outputs/                     # Where you should outputs
├── scripts/                     # Utility scripts 
├── templates/                   # Templates


## Skills quick reference
| Command |	What It Does |
| /proofread [file]	| Grammar/typo/overflow review|
| /interview-me [topic]	| Interactive research interview |

## Code guidelines

When you need to write code, follow these guidelines precisely.

1. Package Management
   - ONLY use uv, NEVER pip
   - Installation: `uv add <package>`
   - Running tools: `uv run <tool>`
   - Upgrading: `uv lock --upgrade-package <package>`
   - FORBIDDEN: `uv pip install`, `@latest` syntax
   - Running python scripts: ONLY use `uv run python` for execution, never use `python3` for execution.

2. Code Quality
   - Type hints required for all code
   - Functions must be focused and small
   - FORBIDDEN: imports inside functions. THEY SHOULD BE AT THE TOP OF THE FILE.

3. Testing Requirements
   - Ask whether the user needs testing modules before implementation.
   - Framework: `uv run --frozen pytest`
   - Coverage: test edge cases and errors
   
## Breaking Changes

When making breaking changes, document them in `outputs/migration.md`. Include:
- What changed
- Why it changed
- How to migrate existing code

Search for related sections in the migration guide and group related changes together
rather than adding new standalone sections.


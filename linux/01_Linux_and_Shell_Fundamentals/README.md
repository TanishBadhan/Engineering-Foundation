# 01. Linux & Shell Fundamentals

The foundation for interacting with Linux through the command line and understanding how the shell executes commands.

## Architecture

Operating System
       ↓
     Linux
       ↓
    Terminal
       ↓
      Shell
       ↓
      Bash
       ↓
    Commands

## Commands

| Command | Purpose |
|---|---|
| `whoami` | Show current user |
| `man` | Read command documentation |
| `clear` | Clear terminal |
| `date` | Show date/time |
| `history` | Show previous commands |

## Core Concepts

### Linux, Terminal, Shell & Bash

- **Linux** → operating system/kernel ecosystem
- **Terminal** → interface for interacting with the system
- **Shell** → interprets commands
- **Bash** → a commonly used shell and scripting language

### Command Structure

`command [options] [arguments]`

Example:

`ls -lah /home`

`ls` → command  
`-lah` → options  
`/home` → argument

### PATH

When a command is entered, the shell searches directories listed in `$PATH` for the executable.

`echo $PATH`  
`which python`  
`command -v python`

### Shell Expansion

The shell can expand variables, patterns, and commands before execution.

`echo $USER`  
`echo {1..5}`  
`ls *.txt`  
`echo "Today: $(date)"`

## Engineering Relevance

This foundation is required for working with:

- Linux servers
- cloud machines
- containers
- CI/CD
- backend services
- AI infrastructure

The goal is **understanding how the shell interacts with the system**, not memorizing commands.

## Completion Check

You should be able to:

- distinguish Linux, terminal, shell, and Bash
- understand commands, options, and arguments
- use `man` to investigate commands
- explain `$PATH`
- understand basic shell expansion
- navigate the command-line environment confidently

**Next:** [02. Filesystem & Navigation](../02_Filesystem_and_Navigation/)

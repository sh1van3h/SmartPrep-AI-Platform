# Day 1

## Concepts Learned

- What is a database?
- Relational Database
- Primary Key
- Foreign Key
- One-to-One Relationship
- One-to-Many Relationship
- Many-to-Many Relationship
- Normalization
- Orphan Records
- Cascade Delete

## Key Takeaways

- A relational database stores data in related tables.
- Foreign keys connect tables together.
- Normalization reduces duplicate data.
- Cascade Delete removes dependent records automatically.
- Database design should be based on the business problem, not the framework.

## Questions I Asked

- What happens when a user updates a note?
- Should AI content be regenerated automatically?
- Should summaries be stored or generated every time?

## Answers

- AI content should be stored.
- Updating a note marks AI content as outdated.
- Users regenerate AI content only when they choose.

# Virtual Environment

## What is a Virtual Environment?

A virtual environment is an isolated Python environment created for a specific project.

It allows every project to have its own Python packages without affecting other projects on the same computer.

## Why do we use it?

- Avoid package conflicts
- Keep dependencies isolated
- Make projects reproducible
- Follow industry standards

## Key Concepts

- Activation tells the terminal to use the Python and pip inside the virtual environment.
- Packages are installed inside `venv/Lib/site-packages`.
- The `venv` folder should not be pushed to GitHub.
- `requirements.txt` stores the list of project dependencies.

## Windows PowerShell

PowerShell blocks scripts by default because of the Execution Policy.

Changing the policy to `RemoteSigned` for the current user allows local activation scripts to run safely.
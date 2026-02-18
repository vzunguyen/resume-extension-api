# Resume Filler API

## Introduction

This repository is the back-end of a Resume Filler project. This project aims to build a browser extension that help user fill in (autofill) their job applications. It will first accept resume pdf file, parsing it to text then structured the data to JSON format.

## Technology Stack

## Project Structure

```
resume-filler-api/
├── src/
│   ├── main/
│       ├── main.py 
│     ├── routers/   
│     ├── services/
│     ├── models/
│     └── utils/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .venv     # Virtual environment
└── .env.example
```

> Disclaimer: Docker is yet to be implemented

## For Devs

To activate Virtual Environment:

```
source .venv/bin/activate
```

To deactivate:

````
deactivate
````

### Wanted Response Format

```
{
  "personal": {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane@example.com",
    "phone": "+1 555 000 0000",
    "location": "San Francisco, CA",
    "linkedin": "https://linkedin.com/in/janedoe",
    "github": "https://github.com/janedoe",
    "website": "https://janedoe.dev",
    "summary": "Software engineer with 5 years of experience..."
  },
  "experience": [
    {
      "title": "Senior Software Engineer",
      "company": "Acme Corp",
      "start_date": "Jan 2022",
      "end_date": "Present",
      "location": "Remote",
      "description": "Led a team of 4 engineers..."
    }
  ],
  "education": [
    {
      "degree": "B.Sc.",
      "field": "Computer Science",
      "school": "MIT",
      "year": "2020",
      "gpa": "3.9"
    }
  ],
  "skills": ["Python", "TypeScript", "Docker", "PostgreSQL"],
  "certifications": ["AWS Solutions Architect"],
  "languages": ["English", "Spanish"]
}
```

# AI PR Reviewer

AI PR Reviewer is an autonomous, intelligent tool that instantly analyzes your Pull Requests for Code Quality, Security Risks, and Codebase Integration.

It consists of a local FastAPI + Typer CLI backend connected to the Google Gemini API, and a beautiful, dynamic React frontend for an unparalleled visual review experience.

## ✨ Features
- **Local First & Secure**: Run the CLI backend locally. No need to install rigid GitHub Apps or upload massive codebases to third-party tools.
- **Deep Analysis**: 
  - **Code Quality**: Evaluates readability, maintainability, and clean architecture.
  - **Security Risk**: Detects vulnerabilities, edge cases, and missing data sanitization.
  - **Codebase Integration**: Reviews how well the PR handles overall application context.
- **Premium User Interface**: A meticulously crafted NextJS/Vite React interface complete with dynamic micro-animations, glassmorphism, and a sleek dark mode.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Node.js 18+ & npm
- A GitHub Personal Access Token (for fetching PR diffs)
- A Google Gemini API Key

### 2. Configure Environment Variables
Create a `.env` file in the root of the repository with the following:
```
GITHUB_TOKEN=your_github_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Setup the Backend
The Python backend uses FastAPI and Typer. It connects to GitHub and Gemini.

```bash
# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate   # On Windows
# source venv/bin/activate # On Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 4. Setup the Frontend
The frontend uses React and Vite.

```bash
cd frontend
npm install
```

---

## 💻 Running the Application

For the best development experience, run both the backend server and the frontend development server concurrently.

### Run the Backend API 
```bash
# From the root directory (make sure your venv is active)
python main.py --port 8000
```
This will start the FastAPI backend on `http://localhost:8000`.

### Run the Frontend UI
```bash
# From the frontend directory
npm run dev
```
The React frontend will be available at `http://localhost:3000`. Simply enter a valid GitHub public PR URL (e.g. `https://github.com/owner/repo/pull/1`) and click **Analyze**.

---

## 🏗️ Production Build

To serve the frontend directly through the Python API (single port):

1. Switch into the `frontend` directory and build the static bundle:
```bash
cd frontend
npm run build
```
2. Run the `main.py` backend. It will automatically detect the `frontend/dist` directory and serve it over `http://localhost:8000`.

---

### Built By
*Sourish, Rishika, Harsha & Abhiram*

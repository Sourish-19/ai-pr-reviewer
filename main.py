import uvicorn
import typer
# We keep typer so we can launch it elegantly from CLI

app = typer.Typer()

@app.command()
def start(port: int = 8000):
    """
    Start the FastAPI Web Server for the frontend.
    """
    typer.echo(f"Starting web server on http://localhost:{port}")
    uvicorn.run("src.api:app", host="0.0.0.0", port=port, reload=True)

if __name__ == "__main__":
    app()

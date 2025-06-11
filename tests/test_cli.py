def test_cli():

    import subprocess

    # Run the CLI command
    result = subprocess.run(
        ["python", "-m", "{project_name}", "greet", "--name", "Test"],
        capture_output=True,
        text=True,
    )

    # Check the output
    assert result.returncode == 0
    assert "Hello, Test!" in result.stdout
    assert result.stderr == ""

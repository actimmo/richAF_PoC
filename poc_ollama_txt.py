import subprocess
import json
import sys

def read_input_text():
    # Read input text from stdin or a file
    if len(sys.argv) > 1:
        # Read from file if filename is provided as an argument
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        # Read from stdin if no filename is provided
        input_text = input("Provide text")
    return input_text

def call_ollama(system_prompt, user_prompt):
    # Replace 'your_model_name_here' with your actual model name
    model_name = 'llama3.1'

    # Build the full prompt with /system and /user prefixes
    full_prompt = f"/system {system_prompt}\n/user {user_prompt}\n"

    # Call ollama via subprocess
    command = ['ollama', 'run', model_name]

    print("Running command:", ' '.join(command))  # Debugging statement

    try:
        result = subprocess.run(
            command,
            input=full_prompt,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
            timeout=120  # Timeout after 120 seconds
        )
    except subprocess.CalledProcessError as e:
        print("Subprocess error:", e)
        print("Standard Error Output:", e.stderr)
        return None
    except subprocess.TimeoutExpired as e:
        print("Subprocess timed out:", e)
        return None

    print("Standard Output:", result.stdout)  # Debugging statement
    print("Standard Error:", result.stderr)   # Debugging statement

    return result.stdout

def main():
    input_text = read_input_text()
    print("Input text:", input_text)  # Debugging statement

    system_prompt = """
You are to analyze the following stock news article and output a JSON object with the following fields:

{
  "match": "MATCH or NOMATCH",
  "direction": "UP or DOWN",
  "likelihood": integer from 1 to 10
}

Instructions:
- "match": "MATCH" if the article is relevant to stock analysis, "NOMATCH" otherwise.
- "direction": "UP" if the stock is predicted to go up, "DOWN" if it is predicted to go down.
- "likelihood": your confidence in the prediction, on a scale from 1 to 10.

**Output only the JSON object and nothing else. Do not include any explanations or additional text.**

Example Output:
{
  "match": "MATCH",
  "direction": "UP",
  "likelihood": 7
}
"""

    user_prompt = f"Article:\n{input_text}"

    response = call_ollama(system_prompt.strip(), user_prompt.strip())
    if response:
        try:
            data = json.loads(response.strip())
            print(json.dumps(data, indent=2))
        except json.JSONDecodeError:
            print("Failed to parse JSON output.", file=sys.stderr)
            print("Response was:", file=sys.stderr)
            print(response, file=sys.stderr)

if __name__ == "__main__":
    main()
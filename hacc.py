from flask import Flask, Response
import random
import time

app = Flask(__name__)

# Sample "code snippets" to display
code_snippets = [
    "int main() {",
    "  printf(\"Hello, World!\\n\");",
    "  return 0;",
    "}",
    "for (int i = 0; i < 10; i++) {",
    "  System.out.println(\"Iteration: \" + i);",
    "}",
    "if (user.isAdmin()) {",
    "  grantAccess(user);",
    "}",
    "def hack_the_mainframe():",
    "  print(\"Hacking...\")",
    "SELECT * FROM users WHERE admin=1;",
    "while True:",
    "  execute_payload();",
    "#define MAX_BUFFER_SIZE 1024",
    "char buffer[MAX_BUFFER_SIZE];",
    "response = requests.get('https://example.com')",
    "try {",
    "  socket.connect(address);",
    "} catch (Exception e) {",
    "  e.printStackTrace();",
    "}",
]

# Generate "code lines" infinitely
def generate_code_forever():
    while True:
        # Append one line of code at a time
        snippet = random.choice(code_snippets)
        yield f"\033[32m{snippet}\033[0m\n"  # Green text
        time.sleep(0.1)  # Slight delay for scrolling effect

@app.route('/')
def fake_hack():
    return Response(generate_code_forever(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify, render_template
import subprocess
import uuid
import os
import tempfile

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    try:
        data = request.get_json()
        code = data.get("code")
        language = data.get("language")

        if language != "python":
            return jsonify({
                "output": "",
                "error": "Only Python is supported for now."
            })

        filename = f"{uuid.uuid4()}.py"
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout
        error = result.stderr

        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({
            "output": output,
            "error": error
        })

    except subprocess.TimeoutExpired:
        return jsonify({
            "output": "",
            "error": "Execution timed out!"
        })

    except Exception as e:
        return jsonify({
            "output": "",
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
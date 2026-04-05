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
        code = data.get("code", "")
        language = data.get("language", "")

        temp_dir = tempfile.gettempdir()
        unique_id = str(uuid.uuid4())

        output = ""
        error = ""

        # 🐍 PYTHON
        if language == "python":
            filename = f"{unique_id}.py"
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

            os.remove(file_path)

        # 💻 C
        elif language == "c":
            source_name = f"{unique_id}.c"
            exe_name = f"{unique_id}.exe" if os.name == "nt" else unique_id

            source_path = os.path.join(temp_dir, source_name)
            exe_path = os.path.join(temp_dir, exe_name)

            with open(source_path, "w", encoding="utf-8") as f:
                f.write(code)

            compile_result = subprocess.run(
                ["gcc", source_path, "-o", exe_path],
                capture_output=True,
                text=True,
                timeout=10
            )

            if compile_result.returncode != 0:
                error = compile_result.stderr
            else:
                run_result = subprocess.run(
                    [exe_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = run_result.stdout
                error = run_result.stderr

            if os.path.exists(source_path):
                os.remove(source_path)
            if os.path.exists(exe_path):
                os.remove(exe_path)

        # ☕ JAVA
        elif language == "java":
            class_name = "Main"
            file_path = os.path.join(temp_dir, f"{class_name}.java")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)

            compile_result = subprocess.run(
                ["javac", file_path],
                capture_output=True,
                text=True,
                timeout=10
            )

            class_file = os.path.join(temp_dir, f"{class_name}.class")

            if compile_result.returncode != 0:
                error = compile_result.stderr
            else:
                run_result = subprocess.run(
                    ["java", "-cp", temp_dir, class_name],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = run_result.stdout
                error = run_result.stderr

            if os.path.exists(file_path):
                os.remove(file_path)
            if os.path.exists(class_file):
                os.remove(class_file)

        else:
            error = "Unsupported language"

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
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
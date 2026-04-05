function runCode() {
    const code = editor.getValue();
    const language = document.getElementById("language").value;

    document.getElementById("output").innerText = "⏳ Running...";
    document.getElementById("status-run").innerText = "Running...";
    document.getElementById("status-language").innerText =
        language.charAt(0).toUpperCase() + language.slice(1);

    fetch("http://127.0.0.1:5000/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code: code,
            language: language
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.output || data.error;
        document.getElementById("status-run").innerText = "Completed";
    })
    .catch(error => {
        console.error(error);
        document.getElementById("output").innerText = "Error connecting to server";
        document.getElementById("status-run").innerText = "Error";
    });
}
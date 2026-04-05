function runCode() {
    const code = editor.getValue();
    const language = document.getElementById("language").value;

    document.getElementById("output").innerText = "⏳ Running...";

    fetch("/run", {
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
        document.getElementById("output").innerText =
            data.output || data.error;
    })
    .catch(error => {
        console.error(error);
        document.getElementById("output").innerText =
            "Error connecting to server";
    });
}
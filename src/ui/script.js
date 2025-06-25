// ui/script.js
document.getElementById('predict-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.prediction) {
            resultDiv.textContent = `Predicted House Price: $${data.prediction} (in $100,000s)`;
        } else {
            resultDiv.textContent = `Error: ${data.error}`;
        }
    });
});

document.getElementById('stock-form').addEventListener('submit', async e => {
  e.preventDefault();
  const symbol = document.getElementById('symbol').value.trim();

  const response = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ symbol })
  });

  const data = await response.json();
  const resultDiv = document.getElementById('result');
  resultDiv.textContent = `Predicted prices for ${symbol}: ${data.predicted.join(', ')}`;
});

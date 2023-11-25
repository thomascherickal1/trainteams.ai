// Fetch response from Flask endpoint
const question = document.getElementById('question-input').value;
fetch('/ask', {
  method: 'POST',
  body: JSON.stringify({question: question})
});
then(response => response.json())
then(data => {
  // Display GPT-3's answer
  document.getElementById('answer').textContent = data.choices[0].text;
})
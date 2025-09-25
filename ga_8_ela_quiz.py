<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Georgia 8th Grade ELA Quiz</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background: #f9f9f9;
    }
    .quiz-container {
      background: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      max-width: 800px;
      margin: auto;
    }
    h2 {
      text-align: center;
    }
    .question {
      margin-bottom: 20px;
    }
    .question p {
      font-weight: bold;
    }
    .options label {
      display: block;
      margin: 5px 0;
      padding: 5px;
      cursor: pointer;
    }
    button {
      background: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background: #45a049;
    }
    #result {
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="quiz-container">
    <h2>Georgia 8th Grade ELA Quiz</h2>
    <form id="quizForm">

      <div class="question">
        <p>1. Which sentence correctly uses a demonstrative pronoun?</p>
        <div class="options">
          <label><input type="radio" name="q1" value="0"> I enjoy to run every day.</label>
          <label><input type="radio" name="q1" value="1"> That is my favorite book.</label>
          <label><input type="radio" name="q1" value="2"> She is the smartest in class.</label>
          <label><input type="radio" name="q1" value="3"> The dog barked loudly.</label>
        </div>
      </div>

      <div class="question">
        <p>2. What does the morpheme 'sub-' mean?</p>
        <div class="options">
          <label><input type="radio" name="q2" value="0"> Above</label>
          <label><input type="radio" name="q2" value="1"> Under/Below</label>
          <label><input type="radio" name="q2" value="2"> Around</label>
          <label><input type="radio" name="q2" value="3"> Without</label>
        </div>
      </div>

      <div class="question">
        <p>3. Read the passage: "The sun peeked over the mountains, smiling on the valley below." What figurative language is used?</p>
        <div class="options">
          <label><input type="radio" name="q3" value="0"> Simile</label>
          <label><input type="radio" name="q3" value="1"> Personification</label>
          <label><input type="radio" name="q3" value="2"> Hyperbole</label>
          <label><input type="radio" name="q3" value="3"> Metaphor</label>
        </div>
      </div>

      <div class="question">
        <p>4. Story 1:<br>
        "Marco stood at the edge of the soccer field, heart pounding. He remembered last season when he missed the final kick, costing his team the championship. Now, with the score tied, his teammates looked at him with hope in their eyes. Marco took a deep breath, telling himself this was his chance to prove he had changed."<br>
        What type of conflict is Marco experiencing?</p>
        <div class="options">
          <label><input type="radio" name="q4" value="0"> Internal Conflict</label>
          <label><input type="radio" name="q4" value="1"> External Conflict</label>
          <label><input type="radio" name="q4" value="2"> Man vs Nature</label>
          <label><input type="radio" name="q4" value="3"> No Conflict</label>
        </div>
      </div>

      <div class="question">
        <p>5. Story 2:<br>
        "The storm raged through the night, tearing branches from trees and flooding the streets. Sarah wrapped herself in a blanket, listening to the wind howl. She thought about her neighbors who had already evacuated and wondered if she had made the right decision to stay behind."<br>
        What figurative language is used in the phrase "the wind howl"?</p>
        <div class="options">
          <label><input type="radio" name="q5" value="0"> Onomatopoeia</label>
          <label><input type="radio" name="q5" value="1"> Hyperbole</label>
          <label><input type="radio" name="q5" value="2"> Metaphor</label>
          <label><input type="radio" name="q5" value="3"> Simile</label>
        </div>
      </div>

      <div class="question">
        <p>6. Story 3:<br>
        "Jamal flipped open the dusty leather journal he found in his grandmother’s attic. The entries told of her life during the civil rights movement, her struggles, and her determination to fight for change. Jamal felt connected to her in a way he never had before, inspired to carry on her legacy."<br>
        What is the central idea of Story 3?</p>
        <div class="options">
          <label><input type="radio" name="q6" value="0"> Old journals are fragile and hard to read.</label>
          <label><input type="radio" name="q6" value="1"> Family history can inspire future generations.</label>
          <label><input type="radio" name="q6" value="2"> Civil rights are no longer important.</label>
          <label><input type="radio" name="q6" value="3"> Jamal dislikes reading.</label>
        </div>
      </div>

      <button type="button" onclick="checkAnswers()">Submit Quiz</button>
    </form>
    <div id="result"></div>
  </div>

  <script>
    function checkAnswers() {
      const answers = [1, 1, 1, 0, 0, 1];
      let score = 0;
      for (let i = 1; i <= answers.length; i++) {
        const radios = document.getElementsByName("q"+i);
        for (let radio of radios) {
          if (radio.checked && parseInt(radio.value) === answers[i-1]) {
            score++;
          }
        }
      }
      document.getElementById("result").innerText = `You scored ${score} / ${answers.length}`;
    }
  </script>
</body>
</html>
// Formula: typing speed = number of characters / time in seconds
//          WPM = (characters / 5) / time in minutes

// 1. Access the HTML elements
const targetElement     = document.getElementById("target-sentence");
const typingInput       = document.getElementById("typing-input");
const restartButton     = document.getElementById("restart-btn");
const timeOutput        = document.getElementById("result-time");
const speedOutput       = document.getElementById("result-speed");
const correctionsOutput = document.getElementById("result-corrections");

const targetSentence = targetElement.textContent.trim();

// 2. Variables
let startTime   = null;
let corrections = 0;
let finished    = false;

// 3. keydown: start the timer on the first character, count Backspace
typingInput.addEventListener("keydown", function (event) {
    if (finished) {
        event.preventDefault();
        return;
    }
    if (startTime === null && event.key.length === 1) {
        startTime = performance.now();
        console.log("Timer started");
    }
    if ((event.key === "Backspace" || event.key === "Delete") && startTime !== null) {
        corrections++;
    }
});

// 4. input: check if the sentence is reproduced exactly
typingInput.addEventListener("input", function () {
    if (!finished && startTime !== null && typingInput.value === targetSentence) {
        const endTime = performance.now();
        finished = true;

        // 5. Calculate
        const totalSeconds   = (endTime - startTime) / 1000;
        const charsPerSecond = targetSentence.length / totalSeconds;
        const wpm            = (targetSentence.length / 5) / (totalSeconds / 60);

        // Display
        timeOutput.textContent        = totalSeconds.toFixed(2) + " s";
        speedOutput.textContent       = charsPerSecond.toFixed(2) + " characters/s (" + wpm.toFixed(2) + " WPM)";
        correctionsOutput.textContent = corrections;

        // 6. Send to Flask
        const typingFeatures = {
            typingTime: Number(totalSeconds.toFixed(2)),
            charsPerSecond: Number(charsPerSecond.toFixed(2)),
            wordsPerMinute: Number(wpm.toFixed(2)),
            corrections: corrections
        };
        console.log("Typing features:", typingFeatures);

        fetch("/collect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ type: "typing-behaviour", features: typingFeatures })
        })
            .then(response => response.json())
            .then(answer => console.log("Server answer:", answer))
            .catch(error => console.error("Sending failed:", error));
    }
});

// Restart button
restartButton.addEventListener("click", function () {
    startTime   = null;
    corrections = 0;
    finished    = false;
    typingInput.value = "";
    timeOutput.textContent = "";
    speedOutput.textContent = "";
    correctionsOutput.textContent = "";
    typingInput.focus();
});
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Progress Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .progress-container {
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 5px;
            margin: 20px 0;
            position: relative;
        }
        .progress-bar {
            width: 0;
            height: 30px;
            background-color: #76c7c0;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #76c7c0;
            color: white;
            border: none;
            border-radius: 5px;
            margin-top: 10px;
        }
        .level-display, .clicks-display {
            font-size: 18px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Progress Tracker</h1>
        <div id="stats-container"></div>
        <input type="text" id="new-stat-name" placeholder="Enter new stat name">
        <button id="add-stat-button">Add New Stat</button>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const statsContainer = document.getElementById('stats-container');
            const addStatButton = document.getElementById('add-stat-button');
            const newStatNameInput = document.getElementById('new-stat-name');

            function createStatElement(name) {
                const statElement = document.createElement('div');
                statElement.classList.add('stat');

                const statTitle = document.createElement('h2');
                statTitle.textContent = name;
                statElement.appendChild(statTitle);

                const levelDisplay = document.createElement('div');
                levelDisplay.classList.add('level-display');
                levelDisplay.innerHTML = `Level: <span class="level">1</span>`;
                statElement.appendChild(levelDisplay);

                const progressContainer = document.createElement('div');
                progressContainer.classList.add('progress-container');
                const progressBar = document.createElement('div');
                progressBar.classList.add('progress-bar');
                progressContainer.appendChild(progressBar);
                statElement.appendChild(progressContainer);

                const progressButton = document.createElement('button');
                progressButton.textContent = 'Gain Progress';
                statElement.appendChild(progressButton);

                const clicksDisplay = document.createElement('div');
                clicksDisplay.classList.add('clicks-display');
                clicksDisplay.innerHTML = `Clicks: <span class="clicks">0</span>/<span class="clicks-to-level-up">2</span>`;
                statElement.appendChild(clicksDisplay);

                let level = 1;
                let clicks = 0;
                let clicksToLevelUp = Math.pow(2, level);

                function updateProgress() {
                    const progress = (clicks / clicksToLevelUp) * 100;
                    progressBar.style.width = `${progress}%`;
                    clicksDisplay.querySelector('.clicks').textContent = clicks;
                    clicksDisplay.querySelector('.clicks-to-level-up').textContent = clicksToLevelUp;
                }

                function levelUp() {
                    level++;
                    levelDisplay.querySelector('.level').textContent = level;
                    clicks = 0;
                    clicksToLevelUp = Math.pow(2, level);
                    updateProgress();
                }

                progressButton.addEventListener('click', () => {
                    clicks++;
                    if (clicks >= clicksToLevelUp) {
                        levelUp();
                    } else {
                        updateProgress();
                    }
                });

                updateProgress();
                return statElement;
            }

            addStatButton.addEventListener('click', () => {
                const statName = newStatNameInput.value.trim();
                if (statName) {
                    const statElement = createStatElement(statName);
                    statsContainer.appendChild(statElement);
                    newStatNameInput.value = '';
                }
            });
        });
    </script>
</body>
</html>
"""

# Write the content to an HTML file
with open('progress_tracker.html', 'w') as file:
    file.write(html_content)

print("HTML file 'progress_tracker.html' has been generated.")

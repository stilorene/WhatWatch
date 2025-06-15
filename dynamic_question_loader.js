let counter = 1;

function loadHTMLContent(counter) {


    let filename = `question_templates/question${counter}.html`;

    //  fetchanfrage um das richtige html in die index.html einzufügen
    fetch(filename)
        .then(response => {
            if (!response.ok) {
                throw new Error('Netzwerkantwort war nicht ok');
            }
            return response.text();
        })
        .then(html => {
            // Fügt den geladenen HTML-Inhalt in das Ziel-div ein
            document.getElementById('dynamic-question').innerHTML = html;
        });
}

loadHTMLContent(counter)

// Button-Click: Counter erhöhen und neuen Content laden
document.getElementById("nextbtn").addEventListener("click", function () {
    // counter darf nie über 4 hinaus!
    if (counter <= 4) {
        // Werte abholen
        if (counter == 1) getcheckboxvalues();
        if (counter == 2) getstarrating();
        if (counter == 3) getgenreid();
        if (counter == 4) senddata(selectedYear); // rufe die Funktion direkt mit dem globalen wert aus der def SelectedYear()
                                                // die anderen haben senddata() direkt in ihren individuellen Funktionen

        // counter nur erhöhen, wenn er noch nicht bei 4 ist
        if (counter < 4) {
            counter++;
            loadHTMLContent(counter);
        } else {
            console.log("Letzte Frage erreicht – kein weiterer Content wird geladen.");
            // Hier kannst du z.B. einen "Fertig"-Button zeigen oder deaktivieren
            // document.getElementById("nextbtn").disabled = true;
            // document.getElementById("nextbtn").textContent = "Abgeschlossen";
        }

        console.log("Aktueller Counter:", counter);
    }
});
document.getElementById("prevbtn").addEventListener("click", function () {
    if (counter > 1) {
        counter--;
    }

    loadHTMLContent(counter);
});

//  hier werden die ausgwählten Elemte abgerufen und gespeichert:

// für question1
function getcheckboxvalues() {
    const checkboxes = document.querySelectorAll('input[name="Streaming"]:checked');
    const werte = Array.from(checkboxes).map(cb => cb.value); 
    console.log("Ausgewählte Werte:", werte);
    senddata(werte);
    // Hier kannst du mit den Werten machen, was du willst
}

//   für question2
function getstarrating() {
    const starrating = document.querySelector('input[name="rating"]:checked');

    if (starrating) {
        console.log("Gewählte Bewertung:", starrating.value);
    } else {
        console.log("Kein Stern ausgewählt!");
    }
    senddata(starrating.value);
}

// für question3
function getgenreid() {
    const checkboxes = document.querySelectorAll('input[name="genre"]:checked');
    const genre = Array.from(checkboxes).map(cb => cb.value);
    console.log("Ausgewählte Werte:", genre);
    senddata(genre);
}

// für question4
// hier den dynamischen Sliderloader für question4
// Globale Funktion, die im Inline-Event aufgerufen wird
function updateYearDisplay(year) {
    var display = document.getElementById('selectedYearDisplay');
    if (display) {
        display.textContent = year;
    }// Update beim Laden ausführen
    console.log(year)
    selectedYear = year;
}



function senddata(data) {
  fetch('http://localhost:5000/api/hallo', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({data})
  })
  .then(response => response.json())
//   .then(data => console.log(data)) // zeigt die Antwort vom Backend (nicht das gesendete JSON)
  .catch(error => console.error('Fehler:', error));
}

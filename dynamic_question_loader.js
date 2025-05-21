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
        if (counter == 4) getyearrange();

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

}

// für question3
function getgenreid() {
    const checkboxes = document.querySelectorAll('input[name="genre"]:checked');
    const genre = Array.from(checkboxes).map(cb => cb.value);
    console.log("Ausgewählte Werte:", genre);
}

// für question4
function getyearrange() {
    const yearrange = document.querySelector('input[name="year-range"]:checked');

    if (yearrange) {
        console.log("Gewählter Zeitraum:", yearrange.value);
    } else {
        console.log("Kein Jahr ausgewählt!");
    }
}
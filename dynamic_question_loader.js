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
    if (counter < 4) {
        counter++;
    }

    loadHTMLContent(counter);
});

document.getElementById("prevbtn").addEventListener("click", function () {
    if (counter > 1) {
        counter--;
    }

    loadHTMLContent(counter);
});
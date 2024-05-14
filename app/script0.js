document.addEventListener("DOMContentLoaded", async function() {
    try {
        const response = await fetch("/prisoners");
        const data = await response.json();
        
        if (response.ok) {
            displayPrisoners(data);
        } else {
            console.error("Failed to fetch prisoners data");
        }
    } catch (error) {
        console.error("Error:", error);
    }
});

function displayPrisoners(prisoners) {
    const prisonersTable = document.getElementById("prisoners-table");
    
    prisoners.forEach(prisoner => {
        const row = prisonersTable.insertRow();
        const nameCell = row.insertCell(0);
        const latitudeCell = row.insertCell(1);
        const longitudeCell = row.insertCell(2);
        
        nameCell.textContent = prisoner.name;
        latitudeCell.textContent = prisoner.latitude;
        longitudeCell.textContent = prisoner.longitude;
    });
}
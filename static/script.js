const API = "http://127.0.0.1:8000";

document.getElementById("recordForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        patient_name: document.getElementById("name").value,
        age: parseInt(document.getElementById("age").value),
        temperature: parseFloat(document.getElementById("temp").value),
        heart_rate: document.getElementById("hr").value || null,
        blood_pressure: document.getElementById("bp").value,
        water_ph: parseFloat(document.getElementById("ph").value),
        water_tds: parseFloat(document.getElementById("tds").value),
        water_turbidity: parseFloat(document.getElementById("turbidity").value),
        contamination: document.getElementById("contamination").checked
    };

    await fetch(`${API}/records`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    alert("Record Added!");
});

async function loadRecords() {
    const res = await fetch(`${API}/records`);
    const data = await res.json();

    const list = document.getElementById("recordsList");
    list.innerHTML = "";

    data.forEach(r => {
        const li = document.createElement("li");
        li.textContent = `${r.patient_name} - Temp: ${r.temperature}`;
        list.appendChild(li);
    });
}

async function getAlerts() {
    const data = {
        patient_name: document.getElementById("name").value,
        age: parseInt(document.getElementById("age").value),
        temperature: parseFloat(document.getElementById("temp").value),
        heart_rate: document.getElementById("hr").value || null,
        blood_pressure: document.getElementById("bp").value,
        water_ph: parseFloat(document.getElementById("ph").value),
        water_tds: parseFloat(document.getElementById("tds").value),
        water_turbidity: parseFloat(document.getElementById("turbidity").value),
        contamination: document.getElementById("contamination").checked
    };

    const res = await fetch(`${API}/alerts`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();

    const list = document.getElementById("alertsList");
    list.innerHTML = "";

    result.alerts.forEach(a => {
        const li = document.createElement("li");
        li.textContent = a;
        list.appendChild(li);
    });
}
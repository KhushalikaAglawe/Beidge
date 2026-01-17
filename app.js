let queryResults = [];

document.getElementById("submitBtn").addEventListener("click", async () => {
    const question = document.getElementById("question").value;
    if (!question) return alert("Please type a question!");

    const loader = document.getElementById("loader");
    const container = document.getElementById("responseContainer");

    loader.classList.remove("hidden");
    container.classList.add("hidden");

    try {
        const response = await fetch("/query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });
        const data = await response.json();
        
        if (data.error) throw new Error(data.error);
        
        queryResults = data.result;
        renderData(data);
    } catch (err) {
        alert(err.message);
    } finally {
        loader.classList.add("hidden");
    }
});

function renderData(data) {
    document.getElementById("responseContainer").classList.remove("hidden");
    document.getElementById("logicalPlan").innerHTML = data.logical_plan.map(s => `<li>${s}</li>`).join("");
    document.getElementById("generatedSql").innerText = data.sql;

    const wrapper = document.getElementById("tableWrapper");
    if (data.result.length > 0) {
        const keys = Object.keys(data.result[0]);
        let html = `<table><thead><tr>${keys.map(k => `<th>${k}</th>`).join("")}</tr></thead><tbody>`;
        html += data.result.map(row => `<tr>${keys.map(k => `<td>${row[k]}</td>`).join("")}</tr>`).join("");
        html += `</tbody></table>`;
        wrapper.innerHTML = html;
    } else {
        wrapper.innerHTML = "<p>No results found.</p>";
    }
}

document.getElementById("downloadCsv").addEventListener("click", () => {
    if (queryResults.length === 0) return;
    const keys = Object.keys(queryResults[0]);
    const csvContent = [
        keys.join(","),
        ...queryResults.map(row => keys.map(k => `"${row[k]}"`).join(","))
    ].join("\n");

    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "data_export.csv";
    a.click();
});
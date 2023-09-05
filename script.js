document.getElementById("supportForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const printerModel = document.getElementById("printerModel").value;
    const issueDescription = document.getElementById("issueDescription").value;

    alert("Chamado aberto com sucesso!");
    document.getElementById("supportForm").reset();
});

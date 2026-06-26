fetch("data/stats.json")
  .then(response => response.json())
  .then(data => {

    document.getElementById("nodes").textContent = data.nodes;
    document.getElementById("countries").textContent = data.countries.length;
    document.getElementById("updated").textContent = data.updated;

    document.getElementById("copy").onclick = () => {
      navigator.clipboard.writeText(data.subscription);
      alert("Subscription copied!");
    };

  })
  .catch(err => console.error(err));

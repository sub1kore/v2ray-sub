fetch("data/stats.json")
  .then(res => res.json())
  .then(data => {
    document.getElementById("brand").textContent = data.brand;
    document.getElementById("nodes").textContent = data.total_lines;
    document.getElementById("updated").textContent = data.updated;
    document.getElementById("protocol").textContent =
      Object.keys(data.protocols).join(", ").toUpperCase();
  })
  .catch(err => console.error("Error loading stats:", err));

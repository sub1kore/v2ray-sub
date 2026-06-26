fetch("data/stats.json")
.then(res => res.json())
.then(data => {

    document.getElementById("brand").textContent = data.brand;

    document.getElementById("nodes").textContent = data.total_lines;

    document.getElementById("updated").textContent = data.updated;

    document.getElementById("protocol").textContent =
        Object.keys(data.protocols)
              .map(p => p.toUpperCase())
              .join(", ");

    document.getElementById("copy").onclick = () => {

        navigator.clipboard.writeText(
            location.origin + "/v2ray-sub/sub_base64.txt"
        );

        alert("Subscription copied!");

    };

});

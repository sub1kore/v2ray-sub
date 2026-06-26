fetch("data/info.json")
.then(res => res.json())
.then(data => {

document.getElementById("nodes").innerHTML=data.nodes;

document.getElementById("update").innerHTML=data.updated;

document.getElementById("copy").onclick=()=>{

navigator.clipboard.writeText(data.subscription);

};

});

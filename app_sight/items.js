window.addEventListener("load", (event) => {
    fetch(window.location.origin + "/categories/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        mode: "cors",
        cache: "no-cache",
    }).then((response) => {
        return response.json();
    }).then((data) => {
        let ul = document.getElementById("known-items");
        for (const key in data) {
            console.log(data[key]);
            let li = document.createElement("li");
            let h2 = document.createElement("h2");
            let p = document.createElement("p");
            let text_div = document.createElement("div");
            let button_div = document.createElement("div");
            let button1 = document.createElement("button");
            let button2 = document.createElement("button");
            h2.innerText = "Item: " + data[key]["desc"];
            p.innerText = "Photos amount: " + data[key]["amount"];
            button1.innerText = "Recapture";
            button2.innerText = "Delete";
            text_div.appendChild(h2);
            text_div.appendChild(p);
            // button_div.appendChild(button1);
            button_div.appendChild(button2);
            li.appendChild(text_div);
            li.appendChild(button_div);
            ul.appendChild(li);
        }
    })
})

let videoCtr = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: {
            facingMode: "environment",
        }
    })
        .then(function (stream) {
            videoCtr.srcObject = stream;
        })
        .catch(function (err0r) {
            console.log("Something went wrong!, " + err0r);
        });
}

function captureImage() {
    let canvas = document.getElementById('save-canvas');
    canvas.getContext('2d').drawImage(videoCtr, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/jpeg');

    window.navigator.vibrate(200);
    // data url of the image
    console.log(image_data_url);

    fetch("http://localhost:8000/create_category/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        mode: "cors",
        cache: "no-cache",

        body: JSON.stringify({
            // base64: image_data_url
            base64: image_data_url,
            item_name: document.getElementById("item-name").value,
        }),

    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
    })
}

function submit_item_name() {
    document.getElementsByClassName("popup")[0].style.display = "none";
}

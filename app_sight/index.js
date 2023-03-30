let videoCtr = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: {
            facingMode: "environment",
            aspectRatio: 100
        }
    })
        .then(function (stream) {
            videoCtr.srcObject = stream;
        })
        .catch(function (err0r) {
            console.log("Something went wrong!, " + err0r);
        });
}
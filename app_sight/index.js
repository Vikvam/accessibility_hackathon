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

}
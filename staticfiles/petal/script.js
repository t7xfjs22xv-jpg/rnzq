// This file should ONLY have JavaScript, no HTML tags!

function toggleMessages() {
    const panel = document.getElementById('message-panel');
    panel.classList.toggle('hidden');
}

function togglePhotobooth() {
    const panel = document.getElementById('photobooth-panel');
    panel.classList.toggle('hidden');
    
    // Open camera if panel is shown
    if (!panel.classList.contains('hidden')) {
        startCamera();
    } else {
        stopCamera();
    }
}

let stream = null;

function startCamera() {
    const video = document.getElementById('video-feed');
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(s => {
            stream = s;
            video.srcObject = stream;
        })
        .catch(err => alert("Camera error: " + err));
}

function stopCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
    }
}

function applyFilter(filterName) {
    const video = document.getElementById('video-feed');
    // Remove old filters
    video.className = "photo-view"; 
    // Add new filter
    if (filterName !== 'none') {
        video.classList.add('filter-' + filterName);
    }
}

function takePhoto() {
    alert("Photo captured! 📸");
    // You can add logic here to save the image to a canvas later
}
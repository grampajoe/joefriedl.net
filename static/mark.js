function startCamera() {
  var video = document.createElement('video');
  document.body.appendChild(video);

  video.autoplay = true;

  navigator.webkitGetUserMedia({video: 1}, function(stream) {
    video.addEventListener('play', function() {
      video.height = video.videoHeight/10;
      video.width = video.videoWidth/10;
    });
    video.src = window.URL.createObjectURL(stream);
  });

  function moveCamera(e) {
    video.style.top = (e.y - video.height/2) + 'px';
    video.style.left = (e.x - video.width/2) + 'px';
  }

  window.addEventListener('mousemove', moveCamera);

  document.body.className = 'marking';
}

window.addEventListener('load', startCamera);

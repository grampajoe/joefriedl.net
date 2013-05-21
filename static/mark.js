function mark() {
  var dragX, dragY,
      guy = document.querySelector('#avatar');

  guy.addEventListener('dragstart', function(e) {
    dragX = e.x - e.target.x,
    dragY = e.y - e.target.y;
  });

  window.addEventListener('drop', function(e) {
    document.body.appendChild(guy);
    guy.className = '';
    guy.style.position = 'absolute';
    guy.style.left = (e.x - dragX) + 'px';
    guy.style.top = (e.y - dragY) + 'px';

    $.post('marks/', {'x': guy.style.left, 'y': guy.style.top});
  });

  window.addEventListener('dragover', function(e) {
    e.preventDefault();
  });
}

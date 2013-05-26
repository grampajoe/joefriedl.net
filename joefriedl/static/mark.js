function mark() {
  var dragX, dragY,
      dragee,
      guy = $('#avatar'),
      marks = $('#marks');

  guy.on('dragstart', function(e) {
    dragging = true;
    e = e.originalEvent;
    dragX = e.x - e.target.x,
    dragY = e.y - e.target.y;
  });

  guy.on('dragend', function(e) {
    dragging = false;
  });

  window.addEventListener('drop', function(e) {
    // Stop if something else is being dragged
    if (!dragging) {
      return;
    }

    var pos = marks.position();

    marks.append(guy);
    guy.removeClass('dragme');
    guy.css({
      'position': 'absolute',
      'left': (e.x - pos.left - dragX) + 'px',
      'top': (e.y - pos.top - dragY) + 'px',
    });

    $.post('marks/', {
      'x': parseFloat(guy.css('left')),
      'y': parseFloat(guy.css('top')),
    });
  });

  window.addEventListener('dragover', function(e) {
    e.preventDefault();
  });
}

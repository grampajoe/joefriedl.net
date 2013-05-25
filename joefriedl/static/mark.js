function mark() {
  var dragX, dragY,
      guy = $('#avatar'),
      marks = $('#marks');

  guy.on('dragstart', function(e) {
    e = e.originalEvent;
    dragX = e.x - e.target.x,
    dragY = e.y - e.target.y;
  });

  window.addEventListener('drop', function(e) {
    marks.append(guy);
    guy.removeClass('dragme');
    guy.css({
      'position': 'absolute',
      'left': (e.x - dragX) + 'px',
      'top': (e.y - dragY) + 'px',
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

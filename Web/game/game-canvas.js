/*
vim:encoding=utf-8:ts=2:sw=2:expandtab
*/

var circles = {
  'red': new Path.Circle([100,100], 50),
  'blue': new Path.Circle([400,100], 50),
  'green': new Path.Circle([100,400], 50),
  'yellow': new Path.Circle([400,400], 50)
};

var mousepos = view.center;

$.each(circles, function(color, circle){
  circle.fillColor = color;
});


function initializePath() {

}

function onFrame(event) {
  $.each(circles, function(i, circle){
    var v1 = (mousepos - circle.position);
    v1.length = 10;
    v1 = v1.rotate(85);
    circle.position += v1;
  });

}

function onMouseMove(event) {
	mousepos = event.point;
}

function onMouseDown(event) {

}

// Reposition the path whenever the window is resized:
function onResize(event) {
	initializePath();
}
function archimedeanSpiral (ctx, cx, cy, stepCount, loopCount, innerDistance, loopSpacing, rotation) {

  ctx.beginPath();

  var stepSize = 2 * Math.PI / stepCount,
      endAngle = 2 * Math.PI * loopCount,
      finished = false;
  for (var angle = 0; !finished; angle += stepSize) {
   if (angle > endAngle) {
    angle = endAngle; finished = true;
   }
   var scalar = innerDistance + loopSpacing * angle,
    rotatedAngle = angle + rotation,
    x = cx + scalar * Math.cos (rotatedAngle),
    y = cy - scalar * Math.sin (rotatedAngle);


    ctx.lineTo (x, y);


  }


  ctx.stroke();
 }

 var c=document.getElementById("spiralCanvas");
 var ctx=c.getContext("2d");
 var width = c.width, height = c.height; //размеры канвы
 var cx = Math.floor(width/2), cy = Math.floor(height/2); //центр канвы

 archimedeanSpiral (ctx, cx, cy,
   360 /*шагов на круг*/,
   5   /*кругов*/,
   0   /*дополнительный отступ*/,
   5   /*пикселов между витками*/,
   0   /*угол поворота всей спирали*/);





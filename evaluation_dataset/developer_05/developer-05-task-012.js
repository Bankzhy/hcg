function mouseEventToCoords(event) {
    var pos = mousePosition(event);
    var canvas = renderer.getCanvas();
    var canvasWidth = canvas.clientWidth,
        canvasHeight = canvas.clientHeight;
    var x = pos.x / canvasWidth * 2 - 1;
    var y = (1 - pos.y / canvasHeight * 2) * canvasHeight / canvasWidth;
    var focal = 1 / Math.tan(config.hfov * Math.PI / 360);
    var s = Math.sin(config.pitch * Math.PI / 180);
    var c = Math.cos(config.pitch * Math.PI / 180);
    var a = focal * c - y * s;
    var root = Math.sqrt(x*x + a*a);
    var pitch = Math.atan((y * c + focal * s) / root) * 180 / Math.PI;
    var yaw = Math.atan2(x / root, a / root) * 180 / Math.PI + config.yaw;
    if (yaw < -180)
        yaw += 360;
    if (yaw > 180)
        yaw -= 360;
    return [pitch, yaw];
}
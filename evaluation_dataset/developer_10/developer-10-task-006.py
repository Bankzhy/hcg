def cube_hires(script, size=1.0, x_segments=1, y_segments=1, z_segments=1,
               simple_bottom=True, center=False, color=None):
    size = util.make_list(size, 3)
    grid(script,
         size,
         x_segments,
         y_segments)
    transform.translate(script, [0, 0, size[2]])
    if simple_bottom:
        plane_hires_edges(
            script, size, x_segments, y_segments)
    else:
        layers.duplicate(script)
        transform.translate(script, [0, 0, -size[2]])
    transform.rotate(script, 'x', 180)
    transform.translate(script, [0, size[1], 0])
    cube_open_hires(
        script=script, size=size, x_segments=x_segments,
        y_segments=y_segments, z_segments=z_segments)
    layers.join(script)
    clean.merge_vert(script, threshold=0.00002)
    if center:
        transform.translate(script, [-size[0] / 2, -size[1] / 2, -size[2] / 2])
    if color is not None:
        vert_color.function(script, color=color)
    return None
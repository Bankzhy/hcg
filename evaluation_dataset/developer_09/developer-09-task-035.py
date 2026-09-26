def default_output_mask(file_out, texture=True, vert_normals=True, vert_colors=False,
                        face_colors=False, ml_version=ML_VERSION):
    vn = ''
    wt = ''
    vc = ''
    fc = ''
    if ml_version < '1.3.4':
        om = '-om'
    else:
        om = '-m'
    fext = os.path.splitext(file_out)[1][1:].strip().lower()
    if fext in ['stl', 'dxf', 'xyz']:
        om = ''
        texture = False
        vert_normals = False
        vert_colors = False
        face_colors = False
    if vert_normals:
        vn = ' vn'
    if texture:
        wt = ' wt'
    if vert_colors:
        vc = ' vc'
    if face_colors:
        fc = ' fc'
    output_mask = '{}{}{}{}{}'.format(om, vn, wt, vc, fc)
    return output_mask
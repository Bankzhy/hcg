function checkInView(m, v) {
        var vpp = applyRotPerspToVec(m, v);
        var winX = vpp[0]*vpp[3];
        var winY = vpp[1]*vpp[3];
        var winZ = vpp[2]*vpp[3];
        var ret = [0, 0, 0];
        if ( winX < -1 )
            ret[0] = -1;
        if ( winX > 1 )
            ret[0] = 1;
        if ( winY < -1 )
            ret[1] = -1;
        if ( winY > 1 )
            ret[1] = 1;
        if ( winZ < -1 || winZ > 1 )
            ret[2] = 1;
        return ret;
    }
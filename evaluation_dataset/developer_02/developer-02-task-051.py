def tostring(self, cnf):
        self.varname_dict = {}
        self.varobj_dict = {}
        varis = set()
        for d in cnf.dis:
            for v in d:
                varis.add(v.name)
        ret = "p cnf %d %d" % (len(varis), len(cnf.dis))
        varis = dict(list(zip(sorted(list(varis)),list(map(str,list(range(1,len(varis)+1)))))))
        for v in varis:
            vo = Variable(v)
            self.varname_dict[vo] = varis[v]
            self.varobj_dict[varis[v]] = vo
        for d in cnf.dis:
            ret += "\n"
            vnamelist = []
            for v in d:
                vnamelist.append(("-" if v.inverted else "") + varis[v.name])
            ret += " ".join(vnamelist) + " 0"
        return ret
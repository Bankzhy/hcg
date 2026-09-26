def depth_file_reader(depth_file):
    depth_dic_coverage = {}
    for line in depth_file:
        tab_split = line.split()
        reference = "_".join(tab_split[0].strip().split("_")[0:3])
        position = tab_split[1]
        num_reads_align = float(tab_split[2].rstrip())
        if reference not in depth_dic_coverage:
            depth_dic_coverage[reference] = {}
        depth_dic_coverage[reference][position] = num_reads_align
    logger.info("Finished parsing depth file.")
    depth_file.close()
    logger.debug("Size of dict_cov: {} kb".format(
        asizeof(depth_dic_coverage)/1024))
    return depth_dic_coverage
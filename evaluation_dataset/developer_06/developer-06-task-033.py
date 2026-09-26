def fetch_hpo_files(hpogenes=False, hpoterms=False, phenotype_to_terms=False, hpodisease=False):
    LOG.info("Fetching HPO information from http://compbio.charite.de")
    base_url = ('http://compbio.charite.de/jenkins/job/hpo.annotations.monthly/'
                'lastStableBuild/artifact/annotation/{}')
    hpogenes_url =  base_url.format('ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype.txt')
    hpoterms_url= base_url.format('ALL_SOURCES_ALL_FREQUENCIES_phenotype_to_genes.txt')
    hpo_phenotype_to_terms_url = base_url.format('ALL_SOURCES_ALL_FREQUENCIES_diseases_to_genes_to_phenotypes.txt')
    hpodisease_url = base_url.format('diseases_to_genes.txt')
    hpo_files = {}
    hpo_urls = {}
    if hpogenes is True:
        hpo_urls['hpogenes'] = hpogenes_url
    if hpoterms is True:
        hpo_urls['hpoterms'] = hpoterms_url
    if phenotype_to_terms is True:
        hpo_urls['phenotype_to_terms'] = hpo_phenotype_to_terms_url
    if hpodisease is True:
        hpo_urls['hpodisease'] = hpodisease_url
    for file_name in hpo_urls:
        url = hpo_urls[file_name]
        hpo_files[file_name] = request_file(url)
    return hpo_files
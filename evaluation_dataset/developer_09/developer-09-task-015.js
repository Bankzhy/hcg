function(objects, inch_args) {
  var cwd = process.cwd();
  var excluded = config.files().excluded || [];
  var data = {
    language: 'javascript',
    client_name: 'inchjs',
    args: inch_args,
    client_version: ""+inch_config.version,
    git_repo_url: getGitRepoURL()
  };
  if( process.env.TRAVIS ) {
    data['travis'] = true;
    data['travis_job_id'] = process.env.TRAVIS_JOB_ID;
    data['travis_commit'] = process.env.TRAVIS_COMMIT;
    data['travis_repo_slug'] = process.env.TRAVIS_REPO_SLUG;
  }
  data['branch_name'] = getGitBranchName();
  data['objects'] = objects.filter(includeObjectFilter).map(function(item) {
        return prepareCodeObject(item, cwd);
      }).filter(function(item) {
        return !excludeObjectIfMatch(item, excluded);
      });
  return data;
}
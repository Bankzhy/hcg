function( kind, promisesDfd ) {
  return function() {
    var dfd = promisesDfd || this;
    var fnSet = [].slice.call( arguments );
    if ( kind === 'progress' || dfd.state === 'pending' ) {
      dfd[ kind + 's' ].push( fnSet );
    } else {
      callSet.call( dfd, fnSet, this[ kind + 'Args' ] );
    }
    if ( promisesDfd ) {
      return dfd.promise;
    }
    return dfd;
  };
}
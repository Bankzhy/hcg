function parseOptions(str, map) {
      if (!map)
        error('parseOptions() internal error: no map given');
      var options = {};
      for (var letter in map)
        options[map[letter]] = false;
      if (!str)
        return options;
      if (typeof str !== 'string')
        error('parseOptions() internal error: wrong str');
      var match = str.match(/^\-(.+)/);
      if (!match)
        return options;
      var chars = match[1].split('');
      chars.forEach(function(c) {
        if (c in map)
          options[map[c]] = true;
        else
          error('option not recognized: '+c);
      });
      return options;
    }
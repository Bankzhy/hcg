function checkRepetition(rLen, str) {
      var res = '',
        repeated = false
      for (var i = 0; i < str.length; i++) {
        repeated = true
        for (var j = 0; j < rLen && j + i + rLen < str.length; j++) {
          repeated = repeated && str.charAt(j + i) === str.charAt(j + i + rLen)
        }
        if (j < rLen) {
          repeated = false
        }
        if (repeated) {
          i += rLen - 1
          repeated = false
        } else {
          res += str.charAt(i)
        }
      }
      return res
    }
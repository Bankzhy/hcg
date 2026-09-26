function(str)
		{
			var inhash = 0;
			var charcount = 0;
			var char;
			if(str.length == 0)
				return 1;
			else
			for (var i=0; i<str.length; i++)
			{
				char = str.charCodeAt(i);
				inhash=	((inhash << 7)|(inhash >>> 25)) ^ char;
	       		inhash >>>= 0;
			}
			return inhash;
		}
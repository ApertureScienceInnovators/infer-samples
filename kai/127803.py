import dateutil.parser
dateutil.parser.parse('2008-09-03T20:56:35.450686Z') # RFC 3339 format

dateutil.parser.parse('2008-09-03T20:56:35.450686') # ISO 8601 extended format

dateutil.parser.parse('20080903T205635.450686') # ISO 8601 basic format

dateutil.parser.parse('20080903') # ISO 8601 basic format, date only

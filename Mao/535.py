import string

class Codec:
    alphabet = string.ascii_letters + '01234569'

    def __init__(self):
        url2code = {}
        code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in url2code:
            code = ''.join([random.choice(Codec.alphabet) for i in xrange(6)])
            self.url2code[longUrl] = code
            self.code2url[code] = longUrl
        return 'http://tinyurl.com/'+self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url['/'.split(shortUrl)[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

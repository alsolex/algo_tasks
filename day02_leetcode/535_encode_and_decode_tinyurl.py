# strange task


class Codec:
    def __init__(self):
        self.pairs = {}
        self.cur_url_idx = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.cur_url_idx += 1
        shortUrl = str(self.cur_url_idx)
        self.pairs[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.pairs[shortUrl]


def main():
    url = input("Enter url: ")
    codec = Codec()
    print("Answer: ", codec.decode(codec.encode(url)))


if __name__ == "__main__":
    main()

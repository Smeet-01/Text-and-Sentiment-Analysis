class Words:
    @staticmethod
    def positive(*args):
        positive_words = [
            "awesome",
            "fantastic",
            "terrific",
            "amazing",
            "brilliant",
            "superb",
            "incredible",
            "excellent",
            "phenomenal",
            "spectacular",
            "fabulous",
            "outstanding",
            "marvelous",
            "splendid",
            "wonderful",
            "delightful",
            "joyful",
            "blissful",
            "radiant",
            "glowing",
            "lively",
            "vibrant",
            "refreshing",
            "invigorating",
            "enlivening",
            "uplifting",
            "inspiring",
            "motivating",
            "encouraging",
            "empowering",
            "transformative",
            "enlightening",
            "nurturing",
            "supportive",
            "caring",
            "compassionate",
            "kind",
            "thoughtful",
            "generous",
            "selfless",
            "gracious",
            "humble",
            "authentic",
            "genuine",
            "sincere",
            "trustworthy",
            "honest",
            "reliable",
            "dependable",
            "loyal",
            "devoted",
            "passionate",
            "enthusiastic",
            "energetic",
            "dynamic",
            "bold",
            "fearless",
            "confident",
            "optimistic",
            "hopeful",
            "resilient",
            "strong",
            "tenacious",
            "persevering",
            "persistent",
            "resourceful",
            "creative",
            "imaginative",
            "innovative",
            "inventive",
            "curious",
            "explorative",
            "open-minded",
            "adaptable",
            "flexible",
            "versatile",
            "agile",
            "nimble",
            "graceful",
            "charming",
            "attractive",
            "beautiful",
            "gorgeous",
            "stunning",
            "striking",
            "elegant",
            "fashionable",
            "trendy",
            "hip",
            "cool",
            "stylish",
            "artistic",
            "expressive",
            "poetic",
            "playful",
            "entertaining",
            "fun",
            "hilarious",
            "amusing",
            "exciting",
        ]
        positive_words.extend(args)
        return positive_words

    @staticmethod
    def negative(*args):
        negative_words = [
            "abysmal",
            "aggravating",
            "aggressive",
            "annoying",
            "arrogant",
            "atrocious",
            "awful",
            "bad",
            "belligerent",
            "bewildering",
            "boring",
            "clumsy",
            "cold",
            "complaining",
            "confused",
            "confrontational",
            "controlling",
            "cowardly",
            "crazy",
            "cruel",
            "cynical",
            "dangerous",
            "dark",
            "dead",
            "deceitful",
            "defeated",
            "defensive",
            "defiant",
            "dejected",
            "delusional",
            "depressing",
            "desperate",
            "destroying",
            "detached",
            "devastated",
            "difficult",
            "dirty",
            "disappointing",
            "disastrous",
            "discontented",
            "discouraged",
            "disgusting",
            "disheartening",
            "dishonest",
            "disillusioned",
            "dislike",
            "displeased",
            "disrespectful",
            "dissatisfied",
            "distasteful",
            "distraught",
            "distressed",
            "disturbing",
            "dreadful",
            "dull",
            "embarrassed",
            "empty",
            "enraged",
            "envious",
            "erratic",
            "evil",
            "exasperated",
            "exhausted",
            "failing",
            "fake",
            "false",
            "farcical",
            "fierce",
            "filthy",
            "foolish",
            "foul",
            "frightening",
            "frivolous",
            "frustrated",
            "furious",
            "greedy",
            "grief-stricken",
            "grim",
            "gross",
            "grouchy",
            "gruesome",
            "guilty",
            "hateful",
            "heartbroken",
            "helpless",
            "hideous",
            "hopeless",
            "horrible",
            "horrifying",
            "hostile",
            "humiliating",
            "hurtful",
            "hysterical",
        ]
        for arg in args:
            negative_words.extend(arg)
        return negative_words

    @staticmethod
    def currencies(*args):
        currency = ['afghani',
                    'ariary',
                    'baht',
                    'balboa',
                    'birr',
                    'bolivar',
                    'boliviano',
                    'cedi',
                    'colon',
                    'córdoba',
                    'dalasi',
                    'denar',
                    'dinar',
                    'dirham',
                    'dobra',
                    'dong',
                    'dram',
                    'escudo',
                    'euro',
                    'florin',
                    'forint',
                    'gourde',
                    'guarani',
                    'gulden',
                    'hryvnia',
                    'kina',
                    'kip',
                    'konvertibilna marka',
                    'koruna',
                    'krona',
                    'krone',
                    'kroon',
                    'kuna',
                    'kwacha',
                    'kwanza',
                    'kyat',
                    'lari',
                    'lats',
                    'lek',
                    'lempira',
                    'leone',
                    'leu',
                    'lev',
                    'lilangeni',
                    'lira',
                    'litas',
                    'loti',
                    'manat',
                    'metical',
                    'naira',
                    'nakfa',
                    'new lira',
                    'new sheqel',
                    'ngultrum',
                    'nuevo sol',
                    'ouguiya',
                    'pataca',
                    'peso',
                    'pound',
                    'pula',
                    'quetzal',
                    'rand',
                    'real',
                    'renminbi',
                    'rial',
                    'riel',
                    'ringgit',
                    'riyal',
                    'ruble',
                    'rufiyaa',
                    'rupee',
                    'rupee',
                    'rupiah',
                    'shilling',
                    'som',
                    'somoni',
                    'special drawing rights',
                    'taka',
                    'tala',
                    'tenge',
                    'tugrik',
                    'vatu',
                    'won',
                    'yen',
                    'zloty']
        for arg in args:
            currency.extend(arg)
        return currency

    @staticmethod
    def DateNums(*args):
        datenums = ['hundred',
                    'thousand',
                    'million',
                    'billion',
                    'trillion',
                    'date',
                    'annual',
                    'annually',
                    'annum',
                    'year',
                    'yearly',
                    'quarter',
                    'quarterly',
                    'qtr',
                    'month',
                    'monthly',
                    'week',
                    'weekly',
                    'day',
                    'daily',
                    'january',
                    'february',
                    'march',
                    'april',
                    'may',
                    'june',
                    'july',
                    'august',
                    'september',
                    'october',
                    'november',
                    'december',
                    'jan',
                    'feb',
                    'mar',
                    'apr',
                    'may',
                    'jun',
                    'jul',
                    'aug',
                    'sep',
                    'sept',
                    'oct',
                    'nov',
                    'dec',
                    'monday',
                    'tuesday',
                    'wednesday',
                    'thursday',
                    'friday',
                    'saturday',
                    'sunday',
                    'one',
                    'two',
                    'three',
                    'four',
                    'five',
                    'six',
                    'seven',
                    'eight',
                    'nine',
                    'ten',
                    'eleven',
                    'twelve',
                    'thirteen',
                    'fourteen',
                    'fifteen',
                    'sixteen',
                    'seventeen',
                    'eighteen',
                    'nineteen',
                    'twenty',
                    'thirty',
                    'forty',
                    'fifty',
                    'sixty',
                    'seventy',
                    'eighty',
                    'ninety',
                    'first',
                    'second',
                    'third',
                    'fourth',
                    'fifth',
                    'sixth',
                    'seventh',
                    'eighth',
                    'ninth',
                    'tenth',
                    'i',
                    'ii',
                    'iii',
                    'iv',
                    'v',
                    'vi',
                    'vii',
                    'viii',
                    'ix',
                    'x',
                    'xi',
                    'xii',
                    'xiii',
                    'xiv',
                    'xv',
                    'xvi',
                    'xvii',
                    'xviii',
                    'xix',
                    'xx']
        for arg in args:
            datenums.extend(arg)
        return datenums

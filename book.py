# the text of all the verses in the book:
BOOK: list[list[str]] = [
    [  # 1
        "OF A PRINCE IN THE EAST",
        "A MAN OF NATURE",
        "CHOSEN BY THE PEOPLE",
        "A COUNCIL OF THREE",

        "OF LOVE BETWEEN ENEMIES",
        "AN UNWANTED CHILD",
        "RETURNING HOME",
        "IN THE LAND OF THE DRAGON",

        "THE TRAVELLERS GUARD",
        "SHIELD OF FLOWERS",
        "ONE FORGED BY WEYLAND",
        "IN ELIZABETHS GARDEN",

        "OF A MUSICIAN",
        "FROM THE MARINERS CHAPEL",
        "THE HELMSMAN SINGS",
        "THE SHIPS ARE AT SEA"
    ],

    [  # 2
        "WITH BLOOD ON HIS HAND",
        "THE DRAGON SLAYER",
        "AMETHYSTS CHILD",
        "DISTURBED BY DISCOVERY",

        "LIFE IN THE TEMPLE",
        "SCHOLASTIC ARGUMENTS",
        "THEY MUST DANCE",
        "TO THE FIRST OF THE HOUSE",

        "TABLES ARE TURNED",
        "A SUITOR REJECTED",
        "A BOND IS MADE",
        "EXCHANGE OF APPLES",

        "CREATED TEN OF TEN",
        "A GENERAL IS CHOSEN",
        "IN THE HEAT OF BATTLE",
        "THE PIRATES WON THE PRIZE"
    ],

    [  # 3
        "SITTING IN THE THRONE",
        "IN A CHAMBER OF TREES",
        "THE SKY FOR A ROOF",
        "A GIFT TO A KING",

        "SUMMONED TO HEAVEN",
        "HE RETURNS WITH HER FATHER",
        "THE HONEST LUMBERJACK",
        "A MODEL OF PERFECTION",

        "A MESSAGE FROM JUPITER",
        "TIME OF LAMPLIGHT",
        "JOURNEY BY WATER",
        "FOR A FRIENDS HAPPINESS",

        "BOTHWAYS HAS GOT HIM",
        "A CONFUSION OF PROMISES",
        "THE SMELL OF LEATHER",
        "JOURNEY IN DISGUISE"
    ],

    [  # 4
        "SHELTERED BY BANKS",
        "JOURNEY BY RIVER",
        "IN THE SAVAGE FOREST",
        "A PEANUT FOR SEMELIA",

        "A MARRIAGE IS MADE",
        "HE ACQUIRES A NEW NAME",
        "LONDON JOINS PARIS",
        "THE BIRTH OF A CHILD",

        "A POOR SCHOLAR",
        "ONE OF SIX",
        "THE GRAND VIZIER",
        "OF THE RULER OF THE WORLD",

        "HIS BROTHER IS KILLED",
        "A FALSE ACCUSATION",
        "A PLEA FOR MERCY",
        "QUESTIONS MUST BE ANSWERED"
    ],

    [  # 5
        "EGGS MUST BE BROKEN",
        "SET SAIL FOR THE SOUTH",
        "A TYRANT IS BORN",
        "THE FLEET IS LOST",

        "THE GUARD SLEEPS",
        "A CITY DESTROYED",
        "REBELS IN THE SOUTH",
        "A CITY IS LIBERATED",

        "A HOSTAGE TAKEN",
        "PRISONER IN THE WOOD",
        "TIED TO A CHAIR",
        "A COMMODORE AT TRAFALGAR",

        "A VELVET SUIT",
        "TOBACCO FOR LODGING",
        "SOLDIER IN THE SOUTH",
        "RUNNER OF CONTRABAND"
    ],

    [  # 6
        "A BANQUET OF KINGS",
        "THE ADMIRALS PARTY",
        "THE CHEST IS OPENED",
        "APRICOTS AND NECTARINES",

        "THE BUTCHER MAKES READY",
        "HE CHANGED HIS COAT",
        "ACROBATS AND CLOWNS",
        "THEY TUMBLE TOGETHER",

        "RETURN OF A LOVED ONE",
        "A MARRIAGE ARRANGED",
        "SHE GIVES WISE ADVICE",
        "MANY DREAM OF RICHES",

        "DEATH OF A KING",
        "ENTER THE HERO",
        "A KING IS CROWNED",
        "HOW DO KING TOSH"],

    [  # 7
        "ENTER THE HERO",
        "AN AGENT OF PROTEST",
        "THE GENIE IN THE CHURCH",
        "THE NONCONFORMIST",

        "A PRISONER IS TAKEN",
        "AN AMERICAN SAILOR",
        "HE SAT FOR A PICTURE",
        "HE WEARS A DIFFERENT CROWN",

        "TRIAL BEFORE THE COUNCIL",
        "LOYALTIES ARE DIVIDED",
        "WOUNDED BY THE TRUTH",
        "HE DOUBTS HIS SON",

        "A LOVERS TRYST",
        "BEWARE OF POISON",
        "A WIDOW AND CHILDREN",
        "A CITY IN FLAMES"],

    [  # 8
        "SHE BEARS HIM A CHILD",
        "BEHOLD THE HEIR APPARENT",
        "THE SACRIFICE IS READY",
        "SHARP DAGGERS CONCEALED",

        "HE MURDERS HIS FRIEND",
        "A MAN OF LETTERS",
        "CHIEF OF THE REBELS",
        "HE FELL TO THE FLOOR",

        "CONSPIRATORS DISCOVERED",
        "A PLEA OF NOT GUILTY",
        "HE REJECTS A PROPOSAL",
        "NEW POWER PROTECTS OLD",

        "THE OLD RULER IS BANISHED",
        "A SOCIAL LION",
        "A VOYAGE TO FRANCE",
        "THE DISTANT MOUNTAINS"
    ],

    [  # 9
        "EMPEROR WANG MOURNS",
        "THE DRAGON IS WOUNDED",
        "A SHIELD OF FIRE",
        "BEHOLD JUPITERS CHILDREN",

        "A DUAL IN COURT",
        "SHE REJECTS HER ADVISORS",
        "A COUNCIL OF REGENTS",
        "SHE WINS THE BATTLE",

        "FIGHT FOR FREEDOM",
        "DEFEAT OF A PLOT",
        "AN INNOCENT TRAITOR",
        "THE PEOPLE ARE HOSTILE",

        "TAKEN TO THE WEST",
        "RETURN TO THE JEWEL",
        "A VOYAGE BY WATER",
        "JOURNEY IN THE DARK"
    ],

    [  # 10
        "TWO DAUGHTERS ONE HUSBAND",
        "THE WILL IS CONTESTED",
        "WITNESSED BY THOUSANDS",
        "THE ACCUSER IS SILENCED",

        "THE LADIES MUST AGREE",
        "A CHANGE OF CLOTHING",
        "THE RETURN OF A GIFT",
        "PARTING OF FRIENDS",

        "AMERICA DISCOVERS ENGLAND",
        "THE MOUNTAIN OF GROG",
        "A SON TAKES POWER",
        "HE CARRIES THE TORCH",

        "SWORDS CROSS IN ANGER",
        "THE EARTH TREMBLES",
        "THE CAPTIVES ESCAPE",
        "THEY RETURN TO THE JEWEL"
    ],

    [  # 11
        "THE CONTEST RENEWED",
        "AN EMPIRE DIVIDED",
        "KING WITH NO CROWN",
        "THE VICTOR REJOICES",

        "A DAUGHTER REJECTED",
        "SHE MUST GO HUNGRY",
        "A FRIENDS ASSISTANCE",
        "A LOYAL HEART",

        "THEY RETURN SEPARATELY",
        "WITH A BOX OF TOYS",
        "TO A FOOLS PARADISE",
        "A MIXED RECEPTION",

        "HER SLAVE JEWEL BEARER",
        "TRIED BY PRIESTS",
        "CRUCIFIED IN CHAINS",
        "A GERMAN CUTS HIM DOWN"
    ],

    [  # 12
        "A TRIAL FOR TREASON",
        "THE VERDICT IS DEATH",
        "CAST INTO PRISON",
        "YEARS OF CAPTIVITY",

        "FOUNDER OF A NATION",
        "THE LIGHT OF VICTORY",
        "SOME SLAVES GO FREE",
        "PARTING OF FRIENDS",

        "JOURNEY BY SEA",
        "STORMY CROSSING",
        "THE SHIPS ARE FOUND",
        "A FORTUNE IS LOST",

        "A FINAL MEETING",
        "A SECRET BURIAL",
        "AN ARDUOUS JOURNEY",
        "IN A DISTANT LAND"
    ],

    [  # 13
        "LAND OF THE CYCLOPS",
        "A SMALL SANCTUARY",
        "PRISONER IN THE TOWER",
        "HE BOWS TO THE SWORD",

        "DEATH IN THE OLD RELIGION",
        "AMONG HIS OWN PEOPLE",
        "DEATH AROUND MIDNIGHT",
        "A GREAT SACRIFICE",

        "DIED IN POVERTY",
        "AN EARLY GRAVE",
        "BURIED ALIVE",
        "A PAINFUL END",

        "SHE WIELDS POWER",
        "A FALSE ACCUSATION",
        "A PET TAKES FLIGHT",
        "A PEACEFUL CONCLUSION"
    ]
]
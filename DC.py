import boardgamegeek
import csv

with open('GameIDs.txt') as input_file:
    GameIDs = [line.strip() for line in input_file]
input_file.close()

for x in reversed(GameIDs):
    if x == '':
        GameIDs.remove(x)


with open("GameData.csv","w", newline='', encoding="utf-8") as file:
    filewriter = csv.writer(file)
    tRow = ['ID', 'Name', 'Rank', 'Rating', 'Owners', 'Year', 'Min Players', 'Max Players', 'Playtime', 'Age', 'Weight', 'Number of Iterations', 'Number of Expansions', 'Acting Mechanic', 'Action Point Allowance System Mechanic', 'Area Enclosure Mechanic', 'Area-Impulse Mechanic', 'Betting/Wagering Mechanic', 'Card Drafting Mechanic', 'Commodity Speculation Mechanic', 'Crayon Rail System Mechanic', 'Dice Rolling Mechanic', 'Hand Management Mechanic', 'Hidden Traitor Mechanic', 'Memory Mechanic', 'Paper-and-Pencil Mechanic', 'Pattern Building Mechanic', 'Pick-up and Deliver Mechanic', 'Point to Point Movement Mechanic', 'Rock-Paper-Scissors Mechanic', 'Roll and Move Mechanic', 'Route/Network Building Mechanic', 'Set Collection Mechanic', 'Simultaneous Action Selection Mechanic', 'Stock Holding Mechanic', 'Take That Mechanic', 'Time Track Mechanic', 'Trick-Taking Mechanic', 'Variable Player Power Mechanic', 'Worker Placement Mechanic', 'Action Programming Mechanic', 'Area Control Mechanic', 'Area Movement Mechanic', 'Auction Mechanic', 'Battle Card Mechanic', 'Chit-Pull System Mechanic', 'Cooperative Mechanic', 'Deckbuilding Mechanic', 'Grid Movement Mechanic', 'Hex-and-Counter Mechanic', 'Line Drawing Mechanic', 'Modular Board Mechanic', 'Partnership Mechanic', 'Pattern Recognition Mechanic', 'Player Elimination Mechanic', 'Press Your Luck Mechanic', 'Role Playing Mechanic', 'Rondel Mechanic', 'Secret Unit Deployment Mechanic', 'Simulation Mechanic', 'Singing Mechanic', 'Storytelling Mechanic', 'Tile Placement Mechanic', 'Trading Mechanic', 'Variable Phase Order Mechanic', 'Voting Mechanic', 'Abstract Strategy Category', 'Adventure Category', 'American Civil War Category', 'American Revolutionary War Category', 'Ancient Category', 'Arabian Category', 'Bluffing Category', 'Card Game Category', 'City Building Category', 'Civilization Category', 'Comic Book/Strip Category', 'Dice Category', 'Educational Category', 'Environmental Category', 'Exploration Category', 'Fantasy Category', 'Fighting Category', 'Horror Category', 'Industry/Manufacturing Category', 'Mafia Category', 'Mature/Adult Category', 'Medical Category', 'Memory Category', 'Modern Warfare Category', 'Murder/Mystery Category', 'Mythology Category', 'Nautical Category', 'Novel-based Category', 'Party Game Category', 'Pirate Category', 'Post-Napoleonic Category', 'Print and Play Category', 'Racing Category', 'Religious Category', 'Science Fiction Category', 'Spy/Secret Agent Category', 'Territory Building Category', 'Transportation Category', 'Trivia Category', 'Vietnam War Category', 'Word Game Category', 'World War II Category', 'Action/Dexterity Category', 'Age of Reason Category', 'American Indian Wars Category', 'American West Category', 'Animals Category', 'Aviation/Flight Category', 'Book Category', 'Childrens Game Category', 'Civil War Category', 'Collectible Components Category', 'Deduction Category', 'Economic Category', 'Electronic Category', 'Expansion for Base Game Category', 'Fan Expansion Category', 'Farming Category', 'Game System Category', 'Humor Category', 'Korean War Category', 'Math Category', 'Maze Category', 'Medieval Category', 'Miniatures Category', 'Movies/TV/Radio Category', 'Music Category', 'Napoleonic Category', 'Negotiation Category', 'Number Category', 'Pike and Shot Category', 'Political Category', 'Prehistoric Category', 'Puzzle Category', 'Real-time Category', 'Renaissance Category', 'Space Exploration Category', 'Sports Category', 'Trains Category', 'Travel Category', 'Video Game Theme Category', 'Wargame Category', 'World War I Category', 'Zombies Category']
    filewriter.writerow(tRow)
    file.close()

def DataCollector(GameList):

    from boardgamegeek import BGGClient
    import csv

    bgg = BGGClient()
    with open("GameData.csv","a", newline='', encoding="utf-8") as file:
        filewriter = csv.writer(file)
        #tRow = ['ID', 'Name', 'Rank', 'Rating', 'Owners', 'Year', 'Min Players', 'Max Players', 'Playtime', 'Age', 'Weight', 'Number of Iterations', 'Number of Expansions', 'Acting Mechanic', 'Action Point Allowance System Mechanic', 'Area Enclosure Mechanic', 'Area-Impulse Mechanic', 'Betting/Wagering Mechanic', 'Card Drafting Mechanic', 'Commodity Speculation Mechanic', 'Crayon Rail System Mechanic', 'Dice Rolling Mechanic', 'Hand Management Mechanic', 'Hidden Traitor Mechanic', 'Memory Mechanic', 'Paper-and-Pencil Mechanic', 'Pattern Building Mechanic', 'Pick-up and Deliver Mechanic', 'Point to Point Movement Mechanic', 'Rock-Paper-Scissors Mechanic', 'Roll and Move Mechanic', 'Route/Network Building Mechanic', 'Set Collection Mechanic', 'Simultaneous Action Selection Mechanic', 'Stock Holding Mechanic', 'Take That Mechanic', 'Time Track Mechanic', 'Trick-Taking Mechanic', 'Variable Player Power Mechanic', 'Worker Placement Mechanic', 'Action Programming Mechanic', 'Area Control Mechanic', 'Area Movement Mechanic', 'Auction Mechanic', 'Battle Card Mechanic', 'Chit-Pull System Mechanic', 'Cooperative Mechanic', 'Deckbuilding Mechanic', 'Grid Movement Mechanic', 'Hex-and-Counter Mechanic', 'Line Drawing Mechanic', 'Modular Board Mechanic', 'Partnership Mechanic', 'Pattern Recognition Mechanic', 'Player Elimination Mechanic', 'Press Your Luck Mechanic', 'Role Playing Mechanic', 'Rondel Mechanic', 'Secret Unit Deployment Mechanic', 'Simulation Mechanic', 'Singing Mechanic', 'Storytelling Mechanic', 'Tile Placement Mechanic', 'Trading Mechanic', 'Variable Phase Order Mechanic', 'Voting Mechanic', 'Abstract Strategy Category', 'Adventure Category', 'American Civil War Category', 'American Revolutionary War Category', 'Ancient Category', 'Arabian Category', 'Bluffing Category', 'Card Game Category', 'City Building Category', 'Civilization Category', 'Comic Book/Strip Category', 'Dice Category', 'Educational Category', 'Environmental Category', 'Exploration Category', 'Fantasy Category', 'Fighting Category', 'Horror Category', 'Industry/Manufacturing Category', 'Mafia Category', 'Mature/Adult Category', 'Medical Category', 'Memory Category', 'Modern Warfare Category', 'Murder/Mystery Category', 'Mythology Category', 'Nautical Category', 'Novel-based Category', 'Party Game Category', 'Pirate Category', 'Post-Napoleonic Category', 'Print and Play Category', 'Racing Category', 'Religious Category', 'Science Fiction Category', 'Spy/Secret Agent Category', 'Territory Building Category', 'Transportation Category', 'Trivia Category', 'Vietnam War Category', 'Word Game Category', 'World War II Category', 'Action/Dexterity Category', 'Age of Reason Category', 'American Indian Wars Category', 'American West Category', 'Animals Category', 'Aviation/Flight Category', 'Book Category', 'Childrens Game Category', 'Civil War Category', 'Collectible Components Category', 'Deduction Category', 'Economic Category', 'Electronic Category', 'Expansion for Base Game Category', 'Fan Expansion Category', 'Farming Category', 'Game System Category', 'Humor Category', 'Korean War Category', 'Math Category', 'Maze Category', 'Medieval Category', 'Miniatures Category', 'Movies/TV/Radio Category', 'Music Category', 'Napoleonic Category', 'Negotiation Category', 'Number Category', 'Pike and Shot Category', 'Political Category', 'Prehistoric Category', 'Puzzle Category', 'Real-time Category', 'Renaissance Category', 'Space Exploration Category', 'Sports Category', 'Trains Category', 'Travel Category', 'Video Game Theme Category', 'Wargame Category', 'World War I Category', 'Zombies Category']
        #filewriter.writerow(tRow)

        for ID in reversed(GameList):
            print("getting data for game ID: "+ID)
            game = bgg.game(None, ID)
            gName = game.name

            print("adding "+gName)

            gRank = game.bgg_rank
            gRating = game.rating_average
            gOwnwers = game.users_owned
            gYear = game.year
            gMinPlayers = game.min_players
            gMaxPlayers = game.max_players
            gPlaytime = game.playing_time
            gAge = game.min_age
            gWeight = game.rating_average_weight
            gIterations = len(game.implementations) #Number of previous versions
            gExpansions = len(game.expansions)

            # Mechanic Bools
            
            gActing = 0
            gActionPointAllowanceSystem = 0
            gAreaEnclosure = 0
            gAreaImpulse = 0
            gBetting = 0
            gDrafting = 0
            gCommodity = 0
            gCrayonRail = 0
            gDiceRoll = 0
            gHandManagement = 0
            gTraitor = 0
            gMemory = 0
            gPaperPencil = 0
            gPattern = 0
            gPickUp = 0
            gPoint = 0
            gRPS = 0
            gRollMove = 0
            gRoute = 0
            gSet = 0
            gSimulAction = 0
            gStock = 0
            gTakeThat = 0
            gTime = 0
            gTrick = 0
            gVariable = 0
            gWorker = 0
            gProgramming = 0
            gAreaControl = 0
            gAreaMovement = 0
            gAuction = 0
            gBattleCard = 0
            gChitPull = 0
            gCoop = 0
            gDeckbuilding = 0
            gGrid = 0
            gHex = 0
            gLine = 0
            gModular = 0
            gPartnerships = 0
            gPattern = 0
            gElim = 0
            gPressLuck = 0
            gRP = 0
            gRondel = 0
            gSecretUnit = 0
            gSim = 0
            gSing = 0
            gStory = 0
            gTile = 0
            gTrading = 0
            gPhase = 0
            gVoting = 0

            for x in game.mechanics:
                if x == "Acting":
                    gActing = 1

                if x == "Action Point Allowance System":
                   gActionPointAllowanceSystem = 1

                if x == "Area Enclosure":
                    gAreaEnclosure = 1

                if x == "Area-Impulse":
                    gAreaImpulse = 1
                        
                if x == "Betting/Wagering":
                    gBetting = 1

                if x == "Card Drafting":
                    gDrafting = 1

                if x == "Commodity Speculation":
                    gCommodity = 1
                        
                if x == "Crayon Rail System":
                    gCrayonRail = 1

                if x == "Dice Rolling":
                    gDiceRoll = 1

                if x == "Hand Management":
                    gHandManagement = 1

                if x == "Hidden Traitor":
                    gTraitor = 1

                if x == "Memory":
                    gMemory = 1

                if x == "Paper-and-Pencil":
                    gPaperPencil = 1

                if x == "Pattern Building":
                    gPattern = 1

                if x == "Pick-up and Deliver":
                    gPickUp = 1

                if x == "Point to Point Movement":
                    gPoint = 1
                                        
                if x == "Rock-Paper-Scissors":
                    gRPS = 1

                if x == "Roll / Spin and Move":
                    gRollMove = 1

                if x == "Route/Network Building":
                    gRoute = 1

                if x == "Set Collection":
                    gSet = 1

                if x == "Simultaneous Action Selection":
                    gSimulAction = 1

                if x == "Stock Holding":
                    gStock = 1

                if x == "Take That":
                    gTakeThat = 1

                if x == "Time Track":
                    gTime = 1

                if x == "Trick-taking":
                    gTrick = 1

                if x == "Variable Player Powers":
                    gVariable = 1

                if x == "Worker Placement":
                    gWorker = 1

                if x == "Action / Movement Programming":
                    gProgramming = 1

                if x == "Area Control / Area Influence":
                    gAreaControl = 1

                if x == "Area Movement":
                    gAreaMovement = 1

                if x == "Auction/Bidding":
                    gAuction = 1

                if x == "Campaign / Battle Card Driven":
                    gBattleCard = 1

                if x == "Chit-Pull System":
                    gChitPull = 1

                if x == "Cooperative Play":
                    gCoop = 1

                if x == "Deck / Pool Building":
                    gDeckbuilding = 1

                if x == "Grid Movement":
                    gGrid = 1

                if x == "Hex-and-Counter":
                    gHex = 1

                if x == "Line Drawing":
                    gLine = 1

                if x == "Modular Board":
                    gModular = 1

                if x == "Partnerships":
                    gPartnerships = 1

                if x == "Pattern Recognition":
                    gPattern = 1

                if x == "Player Elimination":
                    gElim = 1
                                        
                if x == "Press Your Luck":
                    gPressLuck = 1

                if x == "Role Playing":
                    gRP = 1

                if x == "Rondel":
                    gRondel = 1

                if x == "Secret Unit Deployment":
                    gSecretUnit = 1

                if x == "Simulation":
                    gSim = 1

                if x == "Singing":
                    gSing = 1

                if x == "Storytelling":
                    gStory = 1

                if x == "Tile Placement":
                    gTile = 1

                if x == "Trading":
                    gTrading = 1

                if x == "Variable Phase Order":
                    gPhase = 1
                        
                if x == "Voting":
                    gVoting = 1


            #Categories
                        
            gAbstract = 0
            gAdventure = 0
            gUSCivilWar = 0
            gRevolution = 0
            gAncient = 0
            gArabian = 0
            gBluffing = 0
            gCard = 0
            gCity = 0
            gCiv = 0
            gComic = 0
            gDice = 0
            gEducation = 0
            gEnvironment = 0
            gExploration = 0
            gFantasy = 0
            gFighting = 0
            gHorror = 0
            gIndustry = 0
            gMafia = 0
            gAdult = 0
            gMedical = 0
            gMemoryC = 0
            gModernWarfare = 0
            gMurder = 0
            gMyth = 0
            gNautical = 0
            gNovel = 0
            gParty = 0
            gPirates = 0
            gPostNapoleon = 0
            gPnP = 0
            gRacing = 0
            gReligious = 0
            gSciFi = 0
            gSpy = 0
            gTerritory = 0
            gTransport = 0
            gTrivia = 0
            gVietnam = 0
            gWord = 0
            gWWII = 0
            gDexterity = 0
            gReason = 0
            gAmericanIndian = 0
            gAmericanWest = 0
            gAnimals = 0
            gAviation = 0
            gBook = 0
            gChildren = 0
            gCivilWar = 0
            gCollectable = 0
            gDeduction = 0
            gEconomic = 0
            gElectronic = 0
            gExpansionForBase = 0
            gFanExpansion = 0
            gFarming = 0
            gGameSystem = 0
            gHumor = 0
            gKoreanWar = 0
            gMath = 0
            gMaze = 0
            gMedieval = 0
            gMiniatures = 0
            gMovie = 0
            gMusic = 0
            gNapoleonic = 0
            gNegotiation = 0
            gNumber = 0
            gPikeAndShot = 0
            gPolitical = 0
            gPrehistoric = 0
            gPuzzle = 0
            gRealTime = 0
            gRenaissance = 0
            gSpace = 0
            gSports = 0
            gTrains = 0
            gTravel = 0
            gVideoGames = 0
            gWargame = 0
            gWWI = 0
            gZombies = 0

            for x in game.categories:
                if x == "Abstract Strategy":
                    gAbstract = 1

                if x == "Adventure":
                    gAdventure = 1

                if x == "American Civil War":
                    gUSCivilWar = 1

                if x == "American Revolutionary War":
                    gRevolution = 1

                if x == "Ancient":
                    gAncient = 1

                if x == "Arabian":
                    gArabian = 1

                if x == "Bluffing":
                    gBluffing = 1

                if x == "Card Game":
                    gCard = 1
                                        
                if x == "City Building":
                    gCity = 1

                if x == "Civilization":
                    gCiv = 1

                if x == "Comic Book / Strip":
                    gComic = 1

                if x == "Dice":
                    gDice = 1

                if x == "Educational":
                    gEducation = 1

                if x == "Environmental":
                    gEnvironment = 1

                if x == "Exploration":
                    gExploration = 1

                if x == "Fantasy":
                    gFantasy = 1

                if x == "Fighting":
                    gFighting = 1

                if x == "Horror":
                    gHorror = 1

                if x == "Industry / Manufacturing":
                    gIndustry = 1

                if x == "Mafia":
                    gMafia = 1

                if x == "Mature / Adult":
                    gAdult = 1

                if x == "Medical":
                    gMedical = 1

                if x == "Memory":
                    gMemoryC = 1
                        
                if x == "Modern Warfare":
                    gModernWarfare = 1

                if x == "Murder/Mystery":
                    gMurder = 1

                if x == "Mythology":
                    gMyth = 1

                if x == "Nautical":
                    gNautical = 1

                if x == "Novel-based":
                    gNovel = 1
                            
                if x == "Party Game":
                    gParty = 1

                if x == "Pirates":
                    gPirates = 1
                                       
                if x == "Post-Napoleonic":
                    gPostNapoleon = 1

                if x == "Print & Play":
                    gPnP = 1

                if x == "Racing":
                    gRacing = 1

                if x == "Religious":
                    gReligious = 1

                if x == "Science Fiction":
                    gSciFi = 1

                if x == "Spies/Secret Agents":
                    gSpy = 1

                if x == "Territory Building":
                    gTerritory = 1

                if x == "Transportation":
                    gTransport = 1

                if x == "Trivia":
                    gTrivia = 1

                if x == "Vietnam War":
                    gVietnam = 1

                if x == "Word Game":
                    gWord = 1

                if x == "World War II":
                    gWWII = 1

                if x == "Action / Dexterity":
                    gDexterity = 1

                if x == "Age of Reason":
                    gReason = 1
                            
                if x == "American Indian Wars":
                    gAmericanIndian = 1
                            
                if x == "American West":
                    gAmericanWest = 1
                            
                if x == "Animals":
                    gAnimals = 1
                    
                if x == "Aviation / Flight":
                    gAviation = 1
                            
                if x == "Book":
                    gBook = 1
                            
                if x == "Children's Game":
                    gChildren = 1
                            
                if x == "Civil War":
                    gCivilWar = 1
                            
                if x == "Collectible Components":
                    gCollectable = 1
                            
                if x == "Deduction":
                    gDeduction = 1
                            
                if x == "Economic":
                    gEconomic = 1
                            
                if x == "Electronic":
                    gElectronic = 1
                            
                if x == "Expansion for Base-game":
                    gExpansionForBase = 1
                            
                if x == "Fan Expansion":
                    gFanExpansion = 1
                            
                if x == "Farming":
                    gFarming = 1
                            
                if x == "Game System":
                    gGameSystem = 1
                            
                if x == "Humor":
                    gHumor = 1
                            
                if x == "Korean War":
                    gKoreanWar = 1
                            
                if x == "Math":
                    gMath = 1
                            
                if x == "Maze":
                    gMaze = 1
                            
                if x == "Medieval":
                    gMedieval = 1
                            
                if x == "Miniatures":
                    gMiniatures = 1
                            
                if x == "Movies / TV / Radio theme":
                    gMovie = 1
                            
                if x == "Music":
                    gMusic = 1
                            
                if x == "Napoleonic":
                    gNapoleonic = 1
                            
                if x == "Negotiation":
                    gNegotiation = 1
                            
                if x == "Number":
                    gNumber = 1
                            
                if x == "Pike and Shot":
                    gPikeAndShot = 1
                            
                if x == "Political":
                    gPolitical = 1
                            
                if x == "Prehistoric":
                    gPrehistoric = 1
                            
                if x == "Puzzle":
                    gPuzzle = 1
                            
                if x == "Real-time":
                    gRealTime = 1
                            
                if x == "Renaissance":
                    gRenaissance = 1
                            
                if x == "Space Exploration":
                    gSpace = 1
                            
                if x == "Sports":
                    gSports = 1
                            
                if x == "Trains":
                    gTrains = 1
                            
                if x == "Travel":
                    gTravel = 1
                            
                if x == "Video Game Theme":
                    gVideoGames = 1
                            
                if x == "Wargame":
                    gWargame = 1
                            
                if x == "World War I":
                    gWWI = 1
                            
                if x == "Zombies":
                    gZombies = 1

            gRow = [ID, gName, gRank, gRating, gOwnwers, gYear, gMinPlayers, gMaxPlayers, gPlaytime, gAge, gWeight, gIterations, gExpansions, gActing, gActionPointAllowanceSystem, gAreaEnclosure, gAreaImpulse, gBetting, gDrafting, gCommodity, gCrayonRail, gDiceRoll, gHandManagement, gTraitor, gMemory, gPaperPencil, gPattern, gPickUp, gPoint, gRPS, gRollMove, gRoute, gSet, gSimulAction, gStock, gTakeThat, gTime, gTrick, gVariable, gWorker, gProgramming, gAreaControl, gAreaMovement, gAuction, gBattleCard, gChitPull, gCoop, gDeckbuilding, gGrid, gHex, gLine, gModular, gPartnerships, gPattern, gElim, gPressLuck, gRP, gRondel, gSecretUnit, gSim, gSim, gStory, gTile, gTrading, gPhase, gVoting, gAbstract, gAdventure, gUSCivilWar, gRevolution, gAncient, gArabian, gBluffing, gCard, gCity, gCiv, gComic, gDice, gEducation, gEnvironment, gExploration, gFantasy, gFighting, gHorror, gIndustry, gMafia, gAdult, gMedical, gMemoryC, gModernWarfare, gMurder, gMyth, gNautical, gNovel, gParty, gPirates, gPostNapoleon, gPnP, gRacing, gReligious, gSciFi, gSpy, gTerritory, gTransport, gTrivia, gVietnam, gWord, gWWII, gDexterity, gReason, gAmericanIndian, gAmericanWest, gAnimals, gAviation, gBook, gChildren, gCivilWar, gCollectable, gDeduction, gEconomic, gElectronic, gExpansionForBase, gFanExpansion, gFarming, gGameSystem, gHumor, gKoreanWar, gMath, gMaze, gMedieval, gMiniatures, gMovie, gMusic, gNapoleonic, gNegotiation, gNumber, gPikeAndShot, gPolitical, gPrehistoric, gPuzzle, gRealTime, gRenaissance, gSpace, gSports, gTrains, gTravel, gVideoGames, gWargame, gWWI, gZombies]
            filewriter.writerow(gRow)
            GameList.remove(ID)
        file.close()
        print("Done")

def DC(GameList):
    while True:
        try:
            DataCollector(GameList)
        except boardgamegeek.exceptions.BGGApiError:
            pass
        else:
            break


DC(GameIDs)

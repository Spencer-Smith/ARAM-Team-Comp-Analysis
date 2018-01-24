import Solicitante

class Team:
    def __init__(self):
        self.roster = []
        self.ADC = 0
        self.tank = 0
        self.mage = 0
        self.


    def addToRoster(self, champion)
        self.roster.append(champion)
        
        
class Match:
    def __init__(self, matchId, championList):
        self.matchId = matchId
        self.championList = championList
        self.win = Team()
        self.lose = Team()
        self.accountIds = []
        self.getData()

    def getData(self):
        matchData = Solicitante.getMatchData(self.matchId)
        team1win = matchData['teams'][0]['win'] == "Win"
        for player in matchData['participantIdentities']:
            self.accountIds.append(player['player']['accountId'])
        players = matchData['participants']
        for i in range(len(players)):
            champion = self.championList[players[i]['championId']]
            if (i < 5 and team1win) or (i >=5 and not team1win):
                self.win.addToRoster(champion)
            else:
                self.lose.addToRoster(champion)
                
    def getPlayerAccountIds(self):
        return self.accountIds

    def printMatch(self):
        print self.matchId
        print "Winners: " + ", ".join(str(x) for x in self.win)
        print "Losers: " + ", ".join(str(x) for x in self.lose)

class Gateador:
    def __init__(self):
        self.recursionLimit = 4
        self.starter_id = ""
        self.usedIds = {}
        self.viewedMatches = {}
        self.matches = []
        self.champions = {}
        self.setUpChampions()

    def seed(self, summonerName):
        self.starter_id = Solicitante.getAccountId(summonerName)
        self.Gatear(self.starter_id, 0)

    def Gatear(self, accountId, recursions):
        if recursions > self.recursionLimit:
            return
        self.usedIds[accountId] = 1
        recentArams = Solicitante.getRecentArams(accountId)
        for match in recentArams:
            matchId = match['gameId']
            if matchId in self.viewedMatches.keys():
                continue
            newMatch = Match(matchId, self.champions)
            newMatch.printMatch()
            self.matches.append(newMatch)
            self.viewedMatches[matchId] = 1

            newIds = newMatch.getPlayerAccountIds()            
            for player in list(set(newIds).difference(self.usedIds.keys())):
                self.Gatear(player, recursions+1)

    def setUpChampions(self):
        champData = Solicitante.getChampionData()
        for champ in champData.values():
            self.champions[champ['id']] = champ['name']      

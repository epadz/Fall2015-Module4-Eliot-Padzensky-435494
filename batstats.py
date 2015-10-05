import re

def getStats(year):
    if year == 1930 or year == 1940 or year == 1941 or year == 1942 or year == 1943 or year == 1944:
        sreg = re.compile(r"^([\w\s]+)?(\sbatted\s)(\d+)(\stimes\swith\s)(\d+)(\shits\sand\s)(\d+)(\sruns)$")
        team = {}
        fn = "baseball/cardinals-%s.txt" % (year)
        f = open(fn)

        for line in f:
            l = line.rstrip()
            match = sreg.match(l)
            if match:
                pn = match.group(1)
                pb = float(match.group(3))
                ph = float(match.group(5))
                pr = float(match.group(7))
                #print "%s has %d bats and %d runs" % (pn, pb, pr)
        
                if team.has_key(pn):
                    team[pn]["bats"] += pb
                    team[pn]["hits"] += ph
                else:
                    team[pn] = {"bats":pb,"hits":ph}
        for player in team:
            if(team[player]["bats"] == 0):
                team[player]["avg"] = 0
            else:
                team[player]["avg"] = round(team[player]["hits"] / team[player]["bats"], 3)
        sorted_team = sorted(team, key = lambda player: team[player]["avg"], reverse = True)    
        for player in sorted_team:
            print "%s: %s" % (player, str("{:.3f}".format(team[player]["avg"])))
    else:
        print "please enter a valid input"

getStats(input("what year? 1930, 1940, 1941, 1942, 1943, 1944?"))

import pandas as pd

def extract_deliveries(matches):
    deliveries = []

    for match_id, match in enumerate(matches):
         # Match level info
        match_date = match["info"]["dates"][0]
        team1 = match["info"]["teams"][0]
        team2 = match["info"]["teams"][1]
        venue = match["info"].get("venue")
        for innings in match["innings"]:
            overs = innings["overs"]

            for over in overs:
                over_number = over["over"]

                for ball in over["deliveries"]:
                    row = {}

                    # Match Info

                    row['match_id'] = match_id
                    row['date'] = match_date
                    row['team1'] = team1
                    row['team2'] = team2
                    row['venue'] = venue

                    # Basic info
                    row['over'] = over_number
                    row['batter'] = ball.get('batter')
                    row['bowler'] = ball.get('bowler')

                    # Runs
                    runs = ball.get('runs', {})
                    row['runs_batter'] = runs.get('batter', 0)
                    row['runs_total'] = runs.get('total', 0)

                    # Wicket
                    row['is_wicket'] = 1 if 'wickets' in ball else 0

                    #Dismissal type
                    if 'wickets' in ball:
                            row['dismissal_kind'] = ball['wickets'][0].get('kind')
                            row['player_out'] = ball['wickets'][0].get('player_out')
                    else:
                            row['dismissal_kind'] = None
                            row['player_out'] = None

                    deliveries.append(row)

    df = pd.DataFrame(deliveries)
    return df
